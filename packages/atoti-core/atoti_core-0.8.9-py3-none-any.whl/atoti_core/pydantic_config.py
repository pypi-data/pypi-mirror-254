from pydantic import ConfigDict

PYDANTIC_CONFIG: ConfigDict = {
    "allow_inf_nan": False,
    "arbitrary_types_allowed": True,
    "extra": "forbid",  # Consistent with the standard library dataclasses.
    "validate_default": True,
}
