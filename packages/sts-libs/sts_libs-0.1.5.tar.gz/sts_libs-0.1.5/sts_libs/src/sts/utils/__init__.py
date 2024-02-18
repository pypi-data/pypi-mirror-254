#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


def remove_prefix(text: str, prefix: str) -> str:
    """Compatibility function for py38.

    Remove when going Python >= 3.9
    """
    if hasattr(text, 'removeprefix'):
        return text.removeprefix(prefix)
    return text[len(prefix) :] if text.startswith(prefix) else text
