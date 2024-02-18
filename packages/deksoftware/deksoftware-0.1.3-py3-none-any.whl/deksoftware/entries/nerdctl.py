import os
from pathlib import Path
from dektools.shell import shell_wrapper
from dektools.file import sure_dir, merge_assign, remove_path
from dektools.zip import decompress_files
from .base import EntryBase, register


@register('nerdctl')
class NerdctlEntry(EntryBase):
    homepage = 'https://github.com/containerd/nerdctl/releases'
    release = 'https://github.com/containerd/nerdctl/releases/download/v{version}/nerdctl-{version}-linux-amd64.tar.gz'
    name_src = 'nerdctl-full-'

    def install(self):
        path_out = Path(decompress_files(self.paths_src[0])).resolve()
        path_bin = path_out / 'bin'
        for exe in os.listdir(path_bin):
            shell_wrapper(f"install {path_bin / exe} /usr/local/bin/{exe}")
        sure_dir('/opt/cni/bin')
        sure_dir('/etc/systemd/system')
        path_bin = path_out / 'libexec/cni'
        for exe in os.listdir(path_bin):
            shell_wrapper(f"install {path_bin / exe} /opt/cni/bin/{exe}")
        merge_assign('/etc/systemd/system', path_out / 'lib/systemd/system')
        shell_wrapper('systemctl enable buildkit containerd')
        shell_wrapper('systemctl restart buildkit containerd')
        shell_wrapper('systemctl --no-pager status buildkit.service')
        shell_wrapper('systemctl --no-pager status containerd.service')
        remove_path(path_out)
