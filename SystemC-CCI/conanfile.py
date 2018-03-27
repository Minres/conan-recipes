from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os

class SystemC_CCIConan(ConanFile):
    name = "SystemC-CCI"
    version = "0.9.0"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemC-CCI"
    description = "The SystemC Configuration, Control and Inspection (CCI) allows tools to seamlessly and consistently interact with models to provide essential capabilities."
    settings = "os", "compiler", "build_type", "arch"
    options = {"stdcxx":[98,11,14]}
    default_options = "stdcxx=98"
    generators = "gcc"
    source_subfolder = "cci-0.9.0_pub_rev_20171219"
    exports_sources = "cci-0.9.0_pub_rev_20171219/*"
    requires = "SystemC/2.3.2@minres/stable"

    def configure(self):
        self.options["SystemC"].stdcxx = self.options.stdcxx
                
    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        if self.options.stdcxx == "14":
            env_build.cxx_flags = "-std=gnu++14"
        elif self.options.stdcxx == "11":
            env_build.cxx_flags = "-std=gnu++11"
        elif self.options.stdcxx == "98":
            env_build.cxx_flags = "-std=gnu++98"
        env_build.fpic = True
        with tools.chdir(os.path.join(self.source_subfolder, 'src')):
            env_build.make(args=[ 'clean', 'SYSTEMC_HOME=%s' % self.deps_cpp_info["SystemC"].rootpath])
            env_build.make(args=[ 'AT_CXX=', 'SYSTEMC_HOME=%s' % self.deps_cpp_info["SystemC"].rootpath])

    def package(self):
        # Headers
        inc_dir = os.path.join(self.source_subfolder, 'src')
        self.copy(pattern="cci_configuration", dst="include", src=inc_dir, keep_path=True)
        self.copy(pattern="*.h", dst="include", src=inc_dir, keep_path=True)
        # Libs
        lib_dir = os.path.join(self.source_subfolder, 'lib')
        self.copy(pattern="*", dst="lib", src=lib_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cciapi"]
