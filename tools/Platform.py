class PlatformHardware:
    # brand, chip, arch, abi, libc/musl
    def __init__(self, brand: str, chip: str, arch: str, abi: str = None, libc: str = 'glibc'):
        self.brand = brand
        self.chip = chip
        self.arch = arch
        self.abi = abi
        self.libc = libc
    def __str__(self):
        return f"{self.brand} {self.chip} ({self.arch}, {self.abi}, {self.libc})"
    def __repr__(self):
        return f"PlatformHardware(brand={self.brand}, chip={self.chip}, arch={self.arch}, abi={self.abi}, libc={self.libc})"

class PlatformSystem:
    # Linux, Windows, macOS, iOS, Android, JNI(Linux), FreeRTOS
    def __init__(self, name: str, version: str = None):
        self.name = name
        self.version = version

class Platform:
    def __init__(self, hardware: PlatformHardware, system: PlatformSystem):
        self.hardware = hardware
        self.system = system

    def __str__(self):
        return f"{self.hardware} on {self.system.name} {self.system.version if self.system.version else ''}"

    def __repr__(self):
        return f"Platform(hardware={self.hardware}, system={self.system})"
    def is_linux(self):
        return self.system.name.lower() == 'linux'
    def is_windows(self):
        return self.system.name.lower() == 'windows'
    def is_macos(self):
        return self.system.name.lower() == 'macos'
    def is_ios(self):
        return self.system.name.lower() == 'ios'
    def is_android(self):
        return self.system.name.lower() == 'android'
    def is_freertos(self):
        return self.system.name.lower() == 'freertos'
    def is_jni(self):
        return self.system.name.lower() == 'jni' and self.system.version.lower() == 'linux'
    def is_mobile(self):
        return self.is_ios() or self.is_android()
