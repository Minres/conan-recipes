from conans import ConanFile, CMake


class SystemCConan(ConanFile):
    name = "SystemC"
    version = "2.3.2"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemC"
    description = "SystemC is a set of C++ classes and macros which provide an event-driven simulation interface (see also discrete event simulation)."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "stdcxx":[98,11,14]}
    default_options = "shared=True","stdcxx=98"
    generators = "cmake"
    source_subfolder = "systemc-2.3.2"
    exports_sources = "systemc-2.3.2/*"


    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder=self.source_subfolder,
                args=[
                    "-DBUILD_SHARED_LIBS=ON" if self.options.shared else "-DBUILD_SHARED_LIBS=OFF",
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx
                    ]
                )
        cmake.build()
        cmake.install()

    #def package(self):
        # Headers
        #self.copy(pattern="*.h", dst="include", src="package/include", keep_path=True)
        # Libs
        #self.copy(pattern="*", dst="lib", src="package/lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["systemc", "pthread"]

