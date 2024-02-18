from .pyoliteutils import load_file_into_in_mem_filesystem, get_file_from_url
from .mermaid import mm, mermaid
from .lessonsurvey import lessonsurvey

from . import _version
__version__ = _version.get_versions()['version']
