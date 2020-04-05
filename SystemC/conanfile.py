from conans import ConanFile, CMake


class SystemCConan(ConanFile):
    name = "SystemC"
    version = "2.3.3"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemC"
    description = "SystemC is a set of C++ classes and macros which provide an event-driven simulation interface (see also discrete event simulation)."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared":[True, False], "stdcxx":[98,11,14], "phase_cb":[True, False]}
    default_options = "shared=True","stdcxx=11","phase_cb=False"
    generators = "cmake"
    source_subfolder = "systemc-2.3.3"
    exports_sources = "systemc-2.3.3/*"


    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder=self.source_subfolder,
                args=[
                    '-DCMAKE_CXX_FLAGS:="-D_GLIBCXX_USE_CXX11_ABI=%d"' % (0 if self.settings.compiler.libcxx == 'libstdc++' else 1),
                    '-DBUILD_SHARED_LIBS=%s' % ('ON' if self.options.shared else 'OFF'),
                    '-DCMAKE_INSTALL_LIBDIR=lib', 
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx,
                    '-DENABLE_PHASE_CALLBACKS=%s' % ('ON' if self.options.phase_cb else 'OFF'),
                    '-DENABLE_PHASE_CALLBACKS_TRACING=%s' % ('ON' if self.options.phase_cb else 'OFF')
                    ]
                )
        cmake.build()
        cmake.install()

    def package(self):
        pass
        # Headers
        #self.copy(pattern="*.h", dst="include", src="package/include", keep_path=True)
        # Libs
        #self.copy(pattern="*", dst="lib", src="package/lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["systemc"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

