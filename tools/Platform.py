from enum import Enum
import json

class PlatformArch(Enum):
    X86 = 'x86'
    i386 = 'i386'
    X86_64 = 'x86_64'
    ARM = 'arm'
    ARM64 = 'arm64'
    aarch64 = 'aarch64'
    MIPS = 'mips'
    MIPS64 = 'mips64'
    RISCV32 = 'riscv32'
    RISCV64 = 'riscv64'
    POWERPC = 'powerpc'
    POWERPC64 = 'powerpc64'
    WASM32 = 'wasm32'

    def __str__(self):
        return self.value


class PlatformABI(Enum):
    NONE = 'none'
    EABI = 'eabi'
    EABIHF = 'eabihf'

    def __str__(self):
        return self.value

class PlatformLibC(Enum):
    GLIBC = 'glibc'
    MUSL = 'musl'

    def __str__(self):
        return self.value

class PlatformBrand(Enum):
    GENERIC = 'generic'
    INTEL = 'intel'
    AMD = 'amd'
    ARM = 'arm'
    APPLE = 'apple'
    QUALCOMM = 'qualcomm'
    MEDIATEK = 'mediatek'
    BROADCOM = 'broadcom'
    ROCKCHIP = 'rockchip'

    def __str__(self):
        return self.value

class PlatformSystemName(Enum):
    LINUX = 'Linux'
    WINDOWS = 'Windows'
    MACOS = 'MacOS'
    DARWIN = 'Darwin'
    IOS = 'iOS'
    ANDROID = 'Android'
    FREERTOS = 'FreeRTOS'
    JNI = 'jni'
    WASM = 'WebAssembly'

    def __str__(self):
        return self.value


class PlatformHardware:
    # brand, chip, arch, abi, libc/musl
    def __init__(self, arch: PlatformArch, brand: PlatformBrand, chip: str = None, abi: PlatformABI = PlatformABI.NONE, libc: PlatformLibC = PlatformLibC.GLIBC):
        self.brand = brand
        self.chip = chip
        self.arch = arch
        self.abi = abi
        self.libc = libc
    def __str__(self):
        return f"{self.brand} {self.arch} ({self.chip}, {self.abi}, {self.libc})"
    def __repr__(self):
        return f"PlatformHardware(brand={self.brand}, arch={self.arch}, chip={self.chip}, abi={self.abi}, libc={self.libc})"

    @classmethod
    def from_json(cls, data):
        if not data:
            return None
        if isinstance(data, str):
            data = json.loads(data)

        if 'arch' not in data or not data['arch']:
            raise ValueError("Missing 'arch' in platform data. It's necessary to specify the architecture.")

        hardware = PlatformHardware(
            arch=PlatformArch(data.get('arch')),
            brand=PlatformBrand.GENERIC,
            chip=None,
            abi=PlatformABI.NONE,
            libc=PlatformLibC.GLIBC
        )

        if 'brand' in data and data['brand']:
            hardware.brand = PlatformBrand(data.get('brand'))
        if 'chip' in data and data['chip']:
            hardware.chip = data.get('chip')
        if 'abi' in data and data['abi']:
            hardware.abi = PlatformABI(data.get('abi'))
        if 'libc' in data and data['libc']:
            hardware.libc = PlatformLibC(data.get('libc'))

        return hardware

    def to_json(self):
        json = {
            'arch': str(self.arch)
        }
        if self.brand:
            json['brand'] = str(self.brand)
        if self.chip:
            json['chip'] = self.chip
        if self.abi:
            json['abi'] = str(self.abi)
        if self.libc:
            json['libc'] = str(self.libc)
        return json


class PlatformSystem:
    # Linux, Windows, macOS, iOS, Android, JNI(Linux), FreeRTOS
    def __init__(self, name: PlatformSystemName, version: str = None):
        self.name = name
        self.version = version

    def __str__(self):
        return f"{self.name} {self.version if self.version else ''}"

    def __repr__(self):
        return f"PlatformSystem(name={self.name}, version={self.version})"

    def to_json(self):
        if self.version is None:
            return {
                'name': str(self.name)
            }
        return {
            'name': str(self.name),
            'version': self.version
        }

    def to_json_str(self):
        return json.dumps(self.to_json(), indent=4)

    @classmethod
    def from_json(cls, data):
        if not data:
            return None
        if isinstance(data, str):
            data = json.loads(data)

        if 'name' not in data or not data['name']:
            raise ValueError("Missing 'name' in platform system data")

        name = PlatformSystemName(data.get('name'))
        version = data.get('version')

        return PlatformSystem(name=name, version=version)


class Platform:
    def __init__(self, hardware: PlatformHardware, system: PlatformSystem):
        self.hardware = hardware
        self.system = system

    def __str__(self):
        return f"{self.hardware} on {self.system.name} {self.system.version if self.system.version else ''}"

    def __repr__(self):
        return f"Platform(hardware={self.hardware}, system={self.system})"

    @classmethod
    def from_json(cls, data):
        if not data:
            return None
        if isinstance(data, str):
            data = json.loads(data)

        _hw = None
        _os = None

        if 'hardware' in data and data['hardware']:
            _hw = PlatformHardware.from_json(data.get('hardware'))
        if 'hw' in data and data['hw']:
            _hw = PlatformHardware.from_json(data.get('hw'))

        if 'system' in data and data['system']:
            _os = PlatformSystem.from_json(data.get('system'))
        if 'os' in data and data['os']:
            _os = PlatformSystem.from_json(data.get('os'))

        if not _hw or not _os:
            raise ValueError("Missing 'hardware' or 'system' in platform data. Both are required.")

        return Platform(hardware=_hw, system=_os)

    def is_linux(self):
        return self.system.name == PlatformSystemName.LINUX or self.system.name == 'linux'
    def is_windows(self):
        return self.system.name == PlatformSystemName.WINDOWS or self.system.name == 'windows'
    def is_macos(self):
        return self.system.name == PlatformSystemName.MACOS or self.system.name == PlatformSystemName.DARWIN or self.system.name == 'macos' or self.system.name == 'darwin'
    def is_ios(self):
        return self.system.name == PlatformSystemName.IOS or self.system.name == 'ios'
    def is_android(self):
        return self.system.name == PlatformSystemName.ANDROID or self.system.name == 'android'
    def is_freertos(self):
        return self.system.name == PlatformSystemName.FREERTOS
    def is_jni(self):
        return self.system.name == PlatformSystemName.JNI
    def is_mobile(self):
        return self.is_ios() or self.is_android()


    def to_json(self):
        return {
            'hw': self.hardware.to_json(),
            'os': self.system.to_json()
        }