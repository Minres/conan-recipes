from conans import ConanFile, CMake
import os
import pprint

class SystemcverificationTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "stdcxx":[98,11,14]}
    default_options = "shared=True","stdcxx=98"
    generators = "cmake"
    requires = "SystemC/2.3.3@minres/stable"

    def configure(self):
        self.options["SystemCVerification"].stdcxx = self.options.stdcxx
        #if self.settings.compiler == 'gcc' and self.settings.compiler.version > 5:
            #self.output.info("Forcing use of libstdc++11")
            #self.settings.compiler.libcxx='libstdc++11'

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(
                args=[
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx
                ])
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
