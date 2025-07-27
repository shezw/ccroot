# This file is used to manage the toolchain for the project
# There are two types of toolchains: cross-compiler and native compiler
# User also can use the default compiler in the system
# or use the compiler for the specific target
from tools import Platform, Archive
import json


class ToolchainBinaries:
    def __init__(self, host:str, cc:str, cxx:str, cpp:str, ar:str, assem:str, ld:str, objcopy:str, objdump:str, strip:str, nm:str, ranlib:str):
        self.host = host
        self.cc = cc
        self.cxx = cxx
        self.cpp = cpp
        self.assem = assem # as
        self.ld = ld
        self.objcopy = objcopy
        self.objdump = objdump
        self.strip = strip
        self.ar = ar
        self.nm = nm
        self.ranlib = ranlib

        self.addr2line = None
        self.readelf = None
        self.gdb = None
        self.gcov = None
        self.gprof = None
        self.windres = None

        self.elfedit = None
        self.dwp = None

    def set_extra_binaries(self, addr2line=None, readelf=None, gdb=None, gcov=None, gprof=None, windres=None, elfedit=None, dwp=None):
        if addr2line:
            self.addr2line = addr2line
        if readelf:
            self.readelf = readelf
        if gdb:
            self.gdb = gdb
        if gcov:
            self.gcov = gcov
        if gprof:
            self.gprof = gprof
        if windres:
            self.windres = windres
        if elfedit:
            self.elfedit = elfedit
        if dwp:
            self.dwp = dwp


    def __str__(self):
        return f"ToolchainBinaries(cc={self.cc}, cxx={self.cxx}, cpp={self.cpp}, ar={self.ar}, assem={self.assem}, ld={self.ld}, objcopy={self.objcopy}, objdump={self.objdump}, strip={self.strip}, nm={self.nm}, ranlib={self.ranlib})"

    def to_json(self):
        _toolchain_bins = {
            'host': self.host,
            'cc': self.cc,
            'cxx': self.cxx,
            'cpp': self.cpp,
            'ar': self.ar,
            'assem': self.assem,
            'ld': self.ld,
            'objcopy': self.objcopy,
            'objdump': self.objdump,
            'strip': self.strip,
            'nm': self.nm,
            'ranlib': self.ranlib
        }
        if self.addr2line:
            _toolchain_bins['addr2line'] = self.addr2line
        if self.readelf:
            _toolchain_bins['readelf'] = self.readelf
        if self.gdb:
            _toolchain_bins['gdb'] = self.gdb
        if self.gcov:
            _toolchain_bins['gcov'] = self.gcov
        if self.gprof:
            _toolchain_bins['gprof'] = self.gprof
        if self.windres:
            _toolchain_bins['windres'] = self.windres
        if self.elfedit:
            _toolchain_bins['elfedit'] = self.elfedit
        if self.dwp:
            _toolchain_bins['dwp'] = self.dwp
        return _toolchain_bins

    def to_json_str(self):
        return json.dumps(self.to_json(), indent=4)

    @classmethod
    def from_json(cls, data_json:json = None, json_str: str = None):
        if data_json:
            data = data_json
        elif json_str:
            data = json.loads(json_str)
        else:
            data = None
        if not data:
            return None
        if isinstance(data, str):
            data = json.loads(data)
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON data for ToolchainBinaries")
        binaries = cls(
            host=data.get('host'),
            cc=data.get('cc'),
            cxx=data.get('cxx'),
            cpp=data.get('cpp'),
            ar=data.get('ar'),
            assem=data.get('assem'),
            ld=data.get('ld'),
            objcopy=data.get('objcopy'),
            objdump=data.get('objdump'),
            strip=data.get('strip'),
            nm=data.get('nm'),
            ranlib=data.get('ranlib')
        )
        if 'addr2line' in data and data['addr2line']:
            binaries.addr2line = data.get('addr2line')
        if 'readelf' in data and data['readelf']:
            binaries.readelf = data.get('readelf')
        if 'gdb' in data and data['gdb']:
            binaries.gdb = data.get('gdb')
        if 'gcov' in data and data['gcov']:
            binaries.gcov = data.get('gcov')
        if 'gprof' in data and data['gprof']:
            binaries.gprof = data.get('gprof')
        if 'windres' in data and data['windres']:
            binaries.windres = data.get('windres')
        if 'elfedit' in data and data['elfedit']:
            binaries.elfedit = data.get('elfedit')
        if 'dwp' in data and data['dwp']:
            binaries.dwp = data.get('dwp')

        return binaries




class Toolchain:
    def __init__(self, name: str, version:str, platform:Platform, binaries:ToolchainBinaries, archive:Archive):
        self.name = name
        self.version = version
        self.platform = platform
        self.archive = archive
        self.binaries = binaries


    def __str__(self):
        return f"Toolchain(name={self.name}, compiler={self.compiler}, linker={self.linker}, assembler={self.assembler})"

    def to_json(self):
        _toolchain = {
            'name': self.name,
            'version': self.version,
            'platform': self.platform.to_json(),
            'binaries': self.binaries.to_json(),
            'archive': self.archive.to_json()
        }
        return _toolchain

    def to_json_str(self):
        return json.dumps(self.to_json(), indent=4)

    @classmethod
    def from_json(cls, data_json:json = None, json_str: str = None):
        if data_json:
            data = data_json
        elif json_str:
            data = json.loads(json_str)
        else:
            data = None
        if not data:
            return None
        if isinstance(data, str):
            data = json.loads(data)
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON data for Toolchain")

        platform = Platform.from_json(data.get('platform'))
        binaries = ToolchainBinaries.from_json(data.get('binaries'))
        archive = Archive.from_json(data.get('archive'))

        toolchain = cls(
            name=data.get('name'),
            version=data.get('version'),
            platform=platform,
            binaries=binaries,
            archive=archive
        )
        return toolchain