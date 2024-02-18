from dektools.shell import shell_wrapper
from .base import EntryBase, register


@register('libvirt')
class LibvirtEntry(EntryBase):
    name_res = 'libvirt'

    def install(self):
        shell_wrapper(f"bash {self.path_res / 'install.sh'}")
