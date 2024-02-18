from .augment import *
from .document import *
from .storage import *
from lightning_utilities.core.imports import RequirementCache

pydantic_cache = bool(RequirementCache("pydantic < 2.0.0"))
if not pydantic_cache:
    assert pydantic_cache, "pydantic < 2.0.0 is required"
