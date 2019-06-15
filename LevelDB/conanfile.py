from conans import ConanFile, CMake, tools
import os


class LevelDBConan(ConanFile):
    name = "LevelDB"
    version = "1.21"
    license = "https://github.com/google/leveldb/blob/master/LICENSE"
    url = "https://github.com/Minres/conan-recipes/LevelDB"
    use_master = True
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "leveldb/*"
    
    @property
    def source_subfolder(self):
        if self.use_master:
            return "leveldb-master"
        else:
            return "leveldb-%s" % self.version
    
    @property
    def download_url(self):
        if self.use_master:
            return "https://github.com/google/leveldb/archive/master.zip"
        else:
            return "https://github.com/google/leveldb/archive/v%s.zip" % self.version
                    
    def source(self):
        tools.download(self.download_url, "leveldb.zip")
        tools.unzip("leveldb.zip")
#        self.run("git clone https://github.com/google/leveldb.git %s" % self.source_subfolder)

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder=self.source_subfolder,
                args=[
                    "-DBUILD_SHARED_LIBS=ON" if self.options.shared else "-DBUILD_SHARED_LIBS=OFF",
                    "-DCMAKE_INSTALL_LIBDIR=lib" 
                    ]
                )
        cmake.build()
        cmake.install()

#    def package(self):
#        self.copy("*", dst="include", src="%s/include" % self.zipped_folder, keep_path=True)
#        self.copy("*.lib", dst="lib", keep_path=False)
#        self.copy("LICENSE", src=self.zipped_folder, dst="", keep_path=False)
           
#        if self.options.shared:
#            self.copy("*.dll", dst="bin", keep_path=False)
#            self.copy("*.so*", dst="lib", keep_path=False)
#        else:
#            self.copy("*.a", dst="lib", keep_path=False)


    def package_info(self):
        self.cpp_info.libs = ["leveldb"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
