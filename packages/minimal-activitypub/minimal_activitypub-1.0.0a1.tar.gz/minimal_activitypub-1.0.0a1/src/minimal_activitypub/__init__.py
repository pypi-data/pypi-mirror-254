"""Package 'minimal_activitypub' level definitions."""
import sys
from importlib.metadata import version
from typing import Any
from typing import Dict
from typing import Final

__display_name__: Final[str] = "Minimal-ActivityPub"
__version__: Final[str] = version(__package__)

USER_AGENT: Final[str] = f"{__display_name__}_v{__version__}_Python_{sys.version.split()[0]}"

Status = Dict[str, Any]
