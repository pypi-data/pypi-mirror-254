from .base import InstallerBash, register_installer


@register_installer('libvirt')
class LibvirtInstaller(InstallerBash):
    pass
