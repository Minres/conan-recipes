from conans import ConanFile, CMake
import os

class SeasocksTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    build_requires = "Catch/1.9.2@uilianries/stable"

    def configure(self):
        self.options["Seasocks"].shared = self.options.shared
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        os.chdir("bin")
        self.run(".%sServerTests" % os.sep)
