#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
import platform
import sys

__version__ = '0.1.5'


def version_info() -> str:
    """Use when creating an issue against sts-libs.

    `python -c "import sts.__about__; print(sts.__about__.version_info())"`
    """
    return f"""
    {__package__}: {__version__}
    Python: {sys.version.split(" ", maxsplit=1)[0]}
    Platform: {platform.platform()}
    """
