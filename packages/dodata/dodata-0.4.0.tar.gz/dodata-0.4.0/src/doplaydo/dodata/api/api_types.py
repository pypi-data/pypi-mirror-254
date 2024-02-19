"""Type hints module for the API."""
from typing import TypeAlias

Attributes: TypeAlias = "dict[str, int | float | str | Attributes]"
"""Use a metadict that is compatible with JSON."""
