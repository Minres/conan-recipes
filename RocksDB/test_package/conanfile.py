from conans import ConanFile, CMake
import os

class RocksdbTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"stdcxx":[11,14], "fPIC":[True, False]}
    default_options = "stdcxx=14", "fPIC=True"
    generators = "cmake"

    def configure(self):
        self.options["rocksdb"].stdcxx = self.options.stdcxx
        self.options["rocksdb"].fPIC = self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_CXX_STANDARD"] = self.options["rocksdb"].stdcxx
        cmake.definitions["CMAKE_CXX_FLAGS"]="-D_GLIBCXX_USE_CXX11_ABI=%d" %(0 if self.settings.compiler.libcxx == 'libstdc++' else 1)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        os.chdir("bin")
        self.run(".%srocks_sample" % os.sep)
