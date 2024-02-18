from napari_potential_field_navigation.geometries import Box2D, Box3D

import taichi as ti
import taichi.math as tm
import numpy as np

from typing import Union, List
from abc import ABC, abstractmethod


@ti.func
def lerp(a: float, b: float, t: float):
    return a + (b - a) * t


@ti.func
def map_value_to_idx(
    value: float, x_min: float, x_max: float, step_size: float
) -> int:
    """Map a physical value to the index of the corresponding cell in the field.

    Args:
        value (float): value to map
        x_min (float): minimum value of the field
        x_max (float): maximum value of the field
        step_size (float): step size of the field

    Returns:
        int: The index of the lower cell in the field that contains the value.
        If the value is under the lower bound of the field, return -1.
        If the value is greater than the upper bound of the field, return -1.
    """
    assert step_size > 0, "Expected step_size to be positive. Get {}".format(
        step_size
    )
    idx = 0
    if value < x_min:
        idx = -1
    elif value > x_max:
        idx = -2
    else:
        idx = int((value - x_min) / step_size)
    return idx


@ti.data_oriented
class SampledField(ABC):
    @abstractmethod
    def __init__(
        self,
        values: np.ndarray,
        bounds: Union[Box2D, Box3D],
    ) -> None:
        if not isinstance(values, np.ndarray):
            raise TypeError(
                f"Expected values to be a numpy array. Get {type(values)}"
            )
        self._values: ti.Field = None
        self._bounds: Union[Box2D, Box3D] = None
        self._step_sizes: np.ndarray = None
        self.ndim: int = None

    @abstractmethod
    @ti.func
    def at(self, pos: ti.template()) -> ti.template():
        raise NotImplementedError

    @ti.func
    def contains(self, pos: ti.template()) -> bool:
        return self._bounds.contains(pos)

    @property
    def values(self) -> np.ndarray:
        return self._values.to_numpy()

    @property
    def bounds(self) -> Union[Box2D, Box3D]:
        return self._bounds

    @property
    def shape(self):
        return self._values.shape

    @property
    def step_sizes(self):
        if self._step_sizes is None:
            self._step_sizes = np.array(
                [
                    (self._bounds.max[i] - self._bounds.min[i])
                    / (self._values.shape[i] - 1)
                    for i in range(self.ndim)
                ],
                dtype=np.float32,
            )
        return self._step_sizes

    @property
    def resolution(self):
        return self._values.shape

    @property
    def linspace(self) -> List[np.ndarray]:
        return [
            np.linspace(
                self._bounds.min[i],
                self._bounds.max[i],
                self._values.shape[i],
            )
            for i in range(self.ndim)
        ]

    @property
    def meshgrid(self) -> np.ndarray:
        return np.meshgrid(*self.linspace, indexing="ij")

    ## Dunder method
    def __getitem__(self, idx: ti.template()) -> float:
        return self._values[idx]


class SampledField2D(SampledField):
    @abstractmethod
    def __init__(
        self,
        values: np.ndarray,
        bounds: Union[Box2D, Box3D],
    ) -> None:
        super().__init__(values, bounds)
        ## Bounds and step sizes
        if not isinstance(bounds, Box2D):
            raise TypeError(f"Expected bounds to be 2D. Get {type(bounds)}")
        self._bounds = bounds
        self.ndim = 2

    @ti.func
    def at(self, pos: ti.template()) -> ti.template():
        idx = tm.ivec2([0, 0])
        toi = tm.vec2([0, 0])
        for i in ti.static(range(2)):
            temp_idx = map_value_to_idx(
                pos[i],
                self._bounds.min[i],
                self._bounds.max[i],
                self.step_sizes[i],
            )
            # Handle extrapolation
            if temp_idx == -1:
                idx[i] = 0
                toi[i] = 0.0
            elif temp_idx == -2:
                idx[i] = self._values.shape[i] - 2
                toi[i] = 1.0
            else:
                idx[i] = temp_idx
                toi[i] = (
                    pos[i] - self._bounds.min[i] - idx[i] * self.step_sizes[i]
                )
        # Interpolation along x-axis
        s0 = lerp(
            self._values[idx], self._values[idx + tm.ivec2([1, 0])], toi[0]
        )
        s1 = lerp(
            self._values[idx + tm.ivec2([0, 1])],
            self._values[idx + tm.ivec2([1, 1])],
            toi[0],
        )
        # Interpolation along y-axis
        return lerp(s0, s1, toi[1])


class ScalarField2D(SampledField2D):
    def __init__(self, values: np.ndarray, bounds: Box2D) -> None:
        super().__init__(values, bounds)
        ## Dimension and values
        if values.ndim != 2:
            raise ValueError(
                f"Expected sampled field to be a 2D-array. Get {values.ndim} dimensions"
            )
        self._values = ti.field(
            dtype=ti.float32, shape=values.shape, needs_grad=True
        )
        self._values.from_numpy(values.astype(np.float32))

    def spatial_gradient(self) -> "VectorField2D":
        grad_values = np.stack(
            np.gradient(
                self._values.to_numpy(), *self.step_sizes, edge_order=2
            ),
            dtype=np.float32,
            axis=-1,
        )
        return VectorField2D(grad_values, self._bounds)

    ## Dunder method
    def __repr__(self) -> str:
        return f"ScalarField2D(values.shape={self._values.shape}, bounds={self._bounds})"

    def __mul__(self, factor: float) -> "ScalarField2D":
        if not isinstance(factor, (float, int)):
            raise TypeError(
                f"Can not multiply ScalarField {type(factor)}. Expected float or int"
            )
        return ScalarField2D(self.values * factor, self._bounds)

    def __neg__(self) -> "ScalarField2D":
        return ScalarField2D(-self.values, self._bounds)


class VectorField2D(SampledField2D):
    def __init__(
        self,
        values: np.ndarray,
        bounds: Union[Box2D, Box3D],
    ) -> None:
        ## Bounds and step sizes
        super().__init__(values, bounds)
        ## Dimension and values
        if values.ndim != 3 or values.shape[2] != 2:
            raise ValueError(
                f"Expected sampled field to be 3D-array with first dimension of size 2. Get {values.ndim} dimensions and first dimension of size {values.shape[0]}"
            )
        self._values = ti.Vector.field(
            n=self.ndim,
            dtype=ti.float32,
            shape=values.shape[:-1],
            needs_grad=True,
        )
        self._values.from_numpy(values.astype(np.float32))

    @ti.kernel
    def norm_clip(self, value: float):
        assert value > 0, "Expected value to be positive. Get {}".format(value)
        for I in ti.grouped(self._values):
            if tm.length(self._values[I]) > value:
                self._values[I] = (
                    self._values[I] / tm.length(self._values[I]) * value
                )

    ## Dunder method
    def __repr__(self) -> str:
        return f"VectorField2D(values.shape={self._values.shape}, bounds={self._bounds})"

    def __mul__(self, factor: float) -> "VectorField2D":
        if not isinstance(factor, (float, int)):
            raise TypeError(
                f"Can not multiply VectorField {type(factor)}. Expected float or int"
            )
        return VectorField2D(self.values * factor, self._bounds)

    def __neg__(self) -> "VectorField2D":
        return VectorField2D(-self.values, self._bounds)


class SampledField3D(SampledField):
    @abstractmethod
    def __init__(
        self,
        values: np.ndarray,
        bounds: Box3D,
    ) -> None:
        super().__init__(values, bounds)
        ## Bounds and ndim
        if not isinstance(bounds, Box3D):
            raise TypeError(f"Expected bounds to be 3D. Get {type(bounds)}")
        self._bounds = bounds
        self.ndim = 3

    @ti.func
    def at(self, pos: ti.template()) -> ti.template():
        idx = tm.ivec3([0, 0, 0])
        toi = tm.vec3([0, 0, 0])
        for i in ti.static(range(3)):
            idx = tm.ivec3([0, 0, 0])
        toi = tm.vec3([0, 0, 0])
        for i in ti.static(range(3)):
            temp_idx = map_value_to_idx(
                pos[i],
                self._bounds.min[i],
                self._bounds.max[i],
                self.step_sizes[i],
            )
            # Handle extrapolation
            if temp_idx == -1:
                idx[i] = 0
                toi[i] = 0.0
            elif temp_idx == -2:
                idx[i] = self._values.shape[i] - 2
                toi[i] = 1.0
            else:
                idx[i] = temp_idx
                toi[i] = (
                    pos[i] - self._bounds.min[i] - idx[i] * self.step_sizes[i]
                )
        # Interpolation along x-axis
        s0 = lerp(
            self._values[idx],
            self._values[idx + tm.ivec3([1, 0, 0])],
            toi[0],
        )
        s1 = lerp(
            self._values[idx + tm.ivec3([0, 1, 0])],
            self._values[idx + tm.ivec3([1, 1, 0])],
            toi[0],
        )
        s2 = lerp(
            self._values[idx + tm.ivec3([0, 0, 1])],
            self._values[idx + tm.ivec3([1, 0, 1])],
            toi[0],
        )
        s3 = lerp(
            self._values[idx + tm.ivec3([0, 1, 1])],
            self._values[idx + tm.ivec3([1, 1, 1])],
            toi[0],
        )
        # Interpolation along y-axis
        s4 = lerp(s0, s1, toi[1])
        s5 = lerp(s2, s3, toi[1])
        # Interpolation along z-axis
        return lerp(s4, s5, toi[2])


class ScalarField3D(SampledField3D):
    def __init__(self, values: np.ndarray, bounds: Box3D) -> None:
        super().__init__(values, bounds)
        ## Dimension and values
        if values.ndim != 3:
            raise ValueError(
                f"Expected sampled field to be a 3D-array. Get {values.ndim} dimensions"
            )
        self._values = ti.field(
            dtype=ti.float32, shape=values.shape, needs_grad=True
        )
        self._values.from_numpy(values.astype(np.float32))

    def spatial_gradient(self) -> "VectorField3D":
        grad_values = np.stack(
            np.gradient(
                self.values,
                *self.step_sizes,
                edge_order=2,
            ),
            dtype=np.float32,
            axis=-1,
        )
        return VectorField3D(grad_values, self._bounds)

    ## Dunder method
    def __repr__(self) -> str:
        return f"ScalarField3D(values.shape={self._values.shape}, bounds={self._bounds})"

    def __mul__(self, factor: float) -> "ScalarField3D":
        if not isinstance(factor, (float, int)):
            raise TypeError(
                f"Can not multiply ScalarField {type(factor)}. Expected float or int"
            )
        return ScalarField3D(self.values * factor, self._bounds)

    def __neg__(self) -> "ScalarField3D":
        return ScalarField3D(-self.values, self._bounds)


class VectorField3D(SampledField3D):
    def __init__(self, values: np.ndarray, bounds: Box3D) -> None:
        super().__init__(values, bounds)
        ## Dimension and values
        if values.ndim != 4 or values.shape[3] != 3:
            raise ValueError(
                f"Expected sampled field to be 4D-array with first dimension of size 3. Get {values.ndim} dimensions and first dimension of size {values.shape[3]}"
            )
        self._values = ti.Vector.field(
            n=self.ndim,
            dtype=ti.float32,
            shape=values.shape[:-1],
            needs_grad=True,
        )
        self._values.from_numpy(values.astype(np.float32))

    @ti.kernel
    def norm_clip(self, value: float):
        assert value > 0, "Expected value to be positive. Get {}".format(value)
        for I in ti.grouped(self._values):
            if tm.length(self._values[I]) > value:
                self._values[I] = (
                    self._values[I] / tm.length(self._values[I]) * value
                )

    ## Dunder method
    def __repr__(self) -> str:
        return f"VectorField3D(values.shape={self._values.shape}, bounds={self._bounds})"

    def __mul__(self, factor: float) -> "VectorField3D":
        if not isinstance(factor, (float, int)):
            raise TypeError(
                f"Can not multiply ScalarField {type(factor)}. Expected float or int"
            )
        return VectorField3D(self.values * factor, self._bounds)

    def __neg__(self) -> "VectorField3D":
        return VectorField3D(-self.values, self._bounds)

    # @property
    # @ti.kernel
    # def max(self) -> float:
    #     max_val = -tm.inf
    #     for I in ti.grouped(self._values):
    #         max_val = ti.max(max_val, tm.length(self._values[I]))
    #     return max_val

    # def __repr__(self) -> str:
    #     return f"VectorField(values={self._values.shape}, bounds={self._bounds}, extrapolation={self._extrapolation})"

    # @ti.kernel
    # def clip(self, value: float):
    #     for I in ti.grouped(self._values):
    #         if tm.length(self._values[I]) > value:
    #             self._values[I] = (
    #                 self._values[I] / tm.length(self._values[I]) * value
    #             )


class SampledFieldFactory:
    @staticmethod
    def create_vector_field(
        values: np.ndarray, bounds: Union[Box2D, Box3D]
    ) -> Union[VectorField2D, VectorField3D]:
        if isinstance(bounds, Box2D):
            if values.ndim != 3 or values.shape[2] != 2:
                raise ValueError(
                    f"Expected values to be 3D-array with first dimension of size 2. Get {values.ndim} dimensions and first dimension of size {values.shape[0]}"
                )
            return VectorField2D(values, bounds)
        elif isinstance(bounds, Box3D):
            if values.ndim != 4 or values.shape[3] != 3:
                raise ValueError(
                    f"Expected values to be 4D-array with first dimension of size 3. Get {values.ndim} dimensions and first dimension of size {values.shape[0]}"
                )
            return VectorField3D(values, bounds)
        else:
            raise TypeError(
                f"Expected bounds to be Box2D or Box3D. Get {type(bounds)}"
            )

    @staticmethod
    def create_scalar_field(
        values: np.ndarray, bounds: Union[Box2D, Box3D]
    ) -> Union[ScalarField2D, ScalarField3D]:
        if isinstance(bounds, Box2D):
            if values.ndim != 2:
                raise ValueError(
                    f"Expected values to be 2D-array. Get {values.ndim} dimensions"
                )
            return ScalarField2D(values, bounds)
        elif isinstance(bounds, Box3D):
            if values.ndim != 3:
                raise ValueError(
                    f"Expected values to be 3D-array. Get {values.ndim} dimensions"
                )
            return ScalarField3D(values, bounds)
        else:
            raise TypeError(
                f"Expected bounds to be Box2D or Box3D. Get {type(bounds)}"
            )


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ti.init(arch=ti.cpu)

    space = np.linspace(-1, 1, 100)
    values = space[:, None] * space[None, :]
    vector = np.stack(np.gradient(values), dtype=np.float32)

    bounds = Box2D(tm.vec2([-1, -1]), tm.vec2([1, 1]))

    field = ScalarField2D(values, bounds)
    vector_field = -field.spatial_gradient()
    # vector_field = VectorField2D(vector, bounds)

    print("res", field.resolution, "step", field.step_sizes)

    @ti.kernel
    def print_field():
        print(
            field.at(tm.vec2([0, 0])),
            field.at(tm.vec2([1, 1])),
            field.at(tm.vec2([1, 0])),
            field.at(tm.vec2([0, 1])),
        )
        print(
            vector_field.at(tm.vec2([0, 0])),
            vector[:, 50, 50],
            vector[:, 49, 49],
        )
        print(np.max(np.linalg.norm(vector_field._values, axis=-1)))

    # print_field()
    plt.figure()
    plt.imshow(values, origin="lower")
    plt.quiver(
        vector_field.values[:, :, 0],
        vector_field.values[:, :, 1],
        color="k",
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    plt.show()
