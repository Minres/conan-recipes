from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "minres")


class LeveldbTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    requires = "LevelDB/1.20@%s/%s" % (username, channel)
    generators = "cmake"

    def configure(self):
        self.options["LevelDB"].shared = self.options.shared

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.so", "lib", "bin")
        self.copy("*.dylib", "lib", "bin")

    def test(self):
        os.chdir("bin")
        self.run("LD_LIBRARY_PATH=$(pwd) && .%sexample" % os.sep)
