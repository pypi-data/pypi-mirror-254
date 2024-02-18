# https://askubuntu.com/questions/426435/how-to-completely-remove-virsh-from-ubuntu

set -e

sudo apt-get remove --purge libvirt-bin kvm qemu qemu-system-x86
sudo apt-get purge libvirt* kvm qemu*
sudo apt-get autoremove
