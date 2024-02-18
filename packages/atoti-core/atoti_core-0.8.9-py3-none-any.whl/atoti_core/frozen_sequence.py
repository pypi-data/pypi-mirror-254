from collections.abc import Sequence
from typing import Annotated, TypeVar

from pydantic import AfterValidator

_ElementT_co = TypeVar("_ElementT_co", covariant=True)

FrozenSequence = Annotated[
    Sequence[_ElementT_co],
    # Reducing to a `tuple` to ensure runtime immutability of `FrozenSequence` fields on frozen dataclasses.
    # This allows such dataclasses to be hashed and used as keys in a mapping.
    AfterValidator(tuple),
]
