from conans import ConanFile, CMake, tools


class SeasocksConan(ConanFile):
    name = "Seasocks"
    version = "1.3.2"
    license = "BSD 2-clause \"Simplified\" License"
    url = "https://github.com/Minres/conan-recipes/blob/master/Seasocks"
    description = "Simple, small, C++ embeddable webserver with WebSockets support"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "src/main/c/*"
    #requires = "zlib/1.2.11@conan/stable"


    def source(self):
        self.run("git clone https://github.com/mattgodbolt/seasocks.git")
        self.run("cd seasocks && git checkout tags/v1.3.2")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file("seasocks/CMakeLists.txt", "project(Seasocks VERSION 1.3.2)", '''project(Seasocks VERSION 1.3.2)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
        tools.replace_in_file("seasocks/src/CMakeLists.txt", 'add_subdirectory("app/c")', '#add_subdirectory("app/c")')

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(source_folder="seasocks", args=["-DCMAKE_INSTALL_LIBDIR=lib"])
        cmake.build()
        cmake.install()

    #def package(self):
        # nothing to do here now

    def package_info(self):
        self.cpp_info.libs = ["seasocks"]
