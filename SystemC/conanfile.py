from conans import ConanFile, CMake


class SeasocksConan(ConanFile):
    name = "SystemC"
    version = "2.3.2"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemC"
    description = "SystemC is a set of C++ classes and macros which provide an event-driven simulation interface (see also discrete event simulation)."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "stdcxx":[98,11,14]}
    default_options = "shared=True","stdcxx=98"
    generators = "cmake"
    exports_sources = "systemc-2.3.2/*"


#    def build_id(self):
#        self.info_build.settings.build_type = "Any"

#    def source(self):
#        self.run("git clone https://github.com/Minres/SystemCLanguage.git")
#        self.run("cd SystemCLanguage && git checkout master")

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(source_dir="%s/systemc-2.3.2" % self.source_folder)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else "-DBUILD_SHARED_LIBS=OFF"
        self.run('cmake systemc-2.3.2 %s %s -DCMAKE_CXX_STANDARD=%s' % (cmake.command_line, shared, self.options.stdcxx))
        # self.run("cmake --build . %s" % cmake.build_config)
        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package_info(self):
        self.cpp_info.libs = ["systemc"]

