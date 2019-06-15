from conans import ConanFile, CMake

class SystemC_CCIConan(ConanFile):
    name = "SystemC-CCI"
    version = "1.0.0"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemC-CCI"
    description = "The SystemC Configuration, Control and Inspection (CCI) allows tools to seamlessly and consistently interact with models to provide essential capabilities."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "stdcxx":[98,11,14]}
    default_options = "shared=True","stdcxx=98"
    generators = "cmake"
    source_subfolder = "cci-1.0.0"
    exports_sources = "cci-1.0.0/*"
    requires = "SystemC/2.3.3@minres/stable"

    def configure(self):
        self.options["SystemC"].stdcxx = self.options.stdcxx

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder=self.source_subfolder,
                args=[
                    '-DBUILD_SHARED_LIBS=ON' if self.options.shared else '-DBUILD_SHARED_LIBS=OFF',
                    '-DCMAKE_INSTALL_LIBDIR=lib', 
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx,
                    '-DSYSTEMC_ROOT=%s' % self.deps_cpp_info["SystemC"].rootpath
                    ]
                )
        cmake.build()
        cmake.install()
                
    def package(self):
        pass
        # Headers
        #inc_dir = os.path.join(self.source_subfolder, 'src')
        #self.copy(pattern="cci_configuration", dst="include", src=inc_dir, keep_path=True)
        #self.copy(pattern="*.h", dst="include", src=inc_dir, keep_path=True)
        # Libs
        #lib_dir = os.path.join(self.source_subfolder, 'lib')
        #self.copy(pattern="*", dst="lib", src=lib_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cciapi"]
