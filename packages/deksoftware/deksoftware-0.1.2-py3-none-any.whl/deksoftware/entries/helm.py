import os
from pathlib import Path
from dektools.shell import shell_wrapper
from dektools.file import remove_path
from dektools.zip import decompress_files
from .base import EntryBase, register


@register('helm')
class HelmEntry(EntryBase):
    homepage = 'https://github.com/helm/helm/releases'
    release = 'https://get.helm.sh/helm-v{version}-linux-amd64.tar.gz'
    name_src = 'helm-v'

    def install(self):
        path_out = Path(decompress_files(self.paths_src[0])).resolve()
        path_bin = path_out / 'linux-amd64/helm'
        shell_wrapper(f"install {path_bin} /usr/local/bin/{os.path.basename(path_bin)}")
        remove_path(path_out)
