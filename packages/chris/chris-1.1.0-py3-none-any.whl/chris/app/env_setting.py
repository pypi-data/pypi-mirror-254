"""App settings."""

import os
from typing import Optional


class EnvSetting:
    """App setting backed by an environment variable."""

    def __init__(self, variable: str, default: Optional[str] = None, required: bool = False):
        """Construct an EnvSetting."""
        self._variable = variable
        self._default = default
        self._required = required

    @property
    def var(self) -> str:
        """Get the variable name property."""
        return self._variable

    @property
    def default(self) -> Optional[str]:
        """Get the default variable value property."""
        return self._default

    @property
    def value(self) -> Optional[str]:
        """Get the variable value property."""
        variable_value = os.getenv(self._variable, self._default)
        if variable_value is None and self._required:
            raise EnvironmentError(f"Environment variable {self.var} is not set")
        return variable_value
