import os
from dektools.shell import shell_wrapper
from dektools.py import get_whl_name
from .base import InstallerBase, register_installer


@register_installer('whl')
class WhlInstaller(InstallerBase):
    def run(self):
        if os.path.isdir(self.path):
            for whl_file in self.path:
                if whl_file.endswith('.whl'):
                    shell_wrapper(
                        f'bash -c "python3 -m pip uninstall -y {get_whl_name(whl_file)} 2>&1 || true;'
                        f'python3 -m pip install {whl_file}"'
                    )
