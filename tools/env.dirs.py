import os

class EnvDir:
    def __init__(self, proj_dir, debug=True):
        self.proj_dir = proj_dir
        self.is_debug = debug
        _deb_dir = self.proj_dir + '/debug' if debug else '/release'

        self.build_dir = os.path.join(self.proj_dir, 'cc_build')
        self.target_dir = os.path.join(self.proj_dir, 'cc_target')

        self.bin_dir = os.path.join(_deb_dir, 'cc_bin')

        self.bin_dir = os.path.join(_deb_dir, 'bin')
        self.lib_dir = os.path.join(_deb_dir, 'lib')
        self.include_dir = os.path.join(_deb_dir, 'include')
        self.host_dir = os.path.join(_deb_dir, 'host')
        self.build_dir = os.path.join(_deb_dir, 'build')
        self.target_dir = os.path.join(_deb_dir, 'target')

