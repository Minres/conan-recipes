from conans import ConanFile, CMake, tools
import os

class SystemCComponentsConan(ConanFile):
    name = "scc"
    version = "1.0.0"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/SystemC-Components"
    description = "light weight productivity library for SystemC and TLM 2.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "stdcxx":[11,14,17], "fPIC":[True, False]}
    default_options = "shared=True", "stdcxx=11", "fPIC=True"
    generators = ["cmake", "cmake_find_package"]

    requires = (
        "boost/1.70.0@conan/stable",
        "SystemC/2.3.3@minres/stable",
        "SystemCVerification/2.0.1@minres/stable",
        "SystemC-CCI/1.0.0@minres/stable"
    )

    def source(self):
        self.run("git clone --recursive --branch %s https://github.com/Minres/SystemC-Components.git src" % self.version)

    def configure(self):
        self.options["SystemC"].stdcxx = self.options.stdcxx
        self.options["SystemCVerification"].stdcxx = self.options.stdcxx
        self.options["SystemC-CCI"].stdcxx = self.options.stdcxx

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder='src',
                args=[
                    '-DCMAKE_CXX_FLAGS:="-D_GLIBCXX_USE_CXX11_ABI=%d"' % (0 if self.settings.compiler.libcxx == 'libstdc++' else 1),
                    '-DBUILD_SHARED_LIBS=ON' if self.options.shared else '-DBUILD_SHARED_LIBS=OFF',
                    '-DCMAKE_POSITION_INDEPENDENT_CODE=%s' % ('ON' if self.options.fPIC else 'OFF'),
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx,
                    '-DSYSTEMC_PREFIX=%s' % self.deps_cpp_info["SystemC"].rootpath,
                    '-DSCV_PREFIX=%s' % self.deps_cpp_info["SystemCVerification"].rootpath,
                    '-DCCI_PREFIX=%s' % self.deps_cpp_info["SystemC-CCI"].rootpath,
                    ]
                )
        cmake.build()
        cmake.install()

    def package_info(self):
        pass
    
    def package_info(self):
        self.cpp_info.libs = ["scc"]
