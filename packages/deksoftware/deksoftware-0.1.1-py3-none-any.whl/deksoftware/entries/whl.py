from dektools.shell import shell_wrapper
from dektools.py import get_whl_name
from .base import EntryBase, register


@register('whl')
class WhlEntry(EntryBase):
    name_src = '.whl'

    def install(self):
        for whl_file in self.paths_src:
            shell_wrapper(
                f'bash -c "python3 -m pip uninstall -y {get_whl_name(whl_file)} 2>&1 || true;'
                f'python3 -m pip install {whl_file}"'
            )
