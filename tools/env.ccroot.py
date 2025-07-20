import os

from tools.Platform import Platform, PlatformSystem, PlatformHardware

default_target = Platform(
    system=PlatformSystem(name='Linux', version=''),
    hardware=PlatformHardware(brand='Generic', chip='Generic', arch='x86_64', abi=None, libc='glibc')
)

class CCRootEnv:
    def __init__(self, host:Platform, target:Platform = default_target, sysroot:str = None):
        self.host = host
        self.target = target
        self.sysroot = sysroot
        self.is_host = self.target.system.name.lower() == self.host.system.name.lower() and \
            self.target.hardware.arch.lower() == self.host.hardware.arch.lower()