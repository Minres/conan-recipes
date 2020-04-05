from conans import ConanFile, CMake, tools
import os

class RocksDBConan(ConanFile):
    name = "rocksdb"
    version = "6.6.4"
    license = "Apache 2.0 License"
    url = "https://github.com/facebook/rocksdb/"
    description = "A library that provides an embeddable, persistent key-value store for fast storage."
    settings = "os", "compiler", "build_type", "arch"
    options = {"stdcxx":[11,14], "fPIC":[True, False]}
    default_options = "stdcxx=14", "fPIC=True"
    generators = ["cmake", "cmake_find_package", "cmake_paths"]
    source_subfolder = "rocksdb-%s"% version
    exports_sources = "rocksdb/*"

    source_tgz = "https://github.com/facebook/rocksdb/archive/v%s.tar.gz" % version
    
    requires = (
        "zlib/1.2.11",
        "bzip2/1.0.8",
        "lz4/1.8.0@bincrafters/stable",
        "gflags/2.2.2"
        #"zlib/1.2.11@conan/stable",
        #"bzip2/1.0.8@conan/stable",
        #"lz4/1.8.0@bincrafters/stable",
        #"gflags/2.2.2@bincrafters/stable"
        # TODO snappy, zstandard
    )


    def source(self):
        self.output.info("Downloading %s" %self.source_tgz)
        tools.download(self.source_tgz, "rocksdb.tar.gz")
        tools.unzip("rocksdb.tar.gz")
        os.remove("rocksdb.tar.gz")

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(
                source_folder=self.source_subfolder,
                args=[
                    '-DCMAKE_CXX_FLAGS:="-D_GLIBCXX_USE_CXX11_ABI=%d"' % (0 if self.settings.compiler.libcxx == 'libstdc++' else 1),
                    #'-DROCKSDB_BUILD_SHARED=%s' % ('ON' if self.options.shared else 'OFF'),
                    '-DCMAKE_POSITION_INDEPENDENT_CODE=%s' % ('ON' if self.options.fPIC else 'OFF'),
                    '-DCMAKE_CXX_STANDARD=%s' % self.options.stdcxx,
                    '-DWITH_LZ4=ON -DWITH_ZLIB=ON -DWITH_BZ2=ON -DDISABLE_STALL_NOTIF=ON -DWITH_TESTS=OFF',
                    #'-DWITH_LZ4=ON -DWITH_ZLIB=ON -DWITH_BZ2=ON -DDISABLE_STALL_NOTIF=ON -DWITH_TOOLS=OFF -DWITH_TESTS=OFF',
                    #'-DWITH_BENCHMARK_TOOLS=OFF -DWITH_CORE_TOOLS=OFF -DWITH_TOOLS=OFF -DWITH_TESTS=OFF'
                    ]
                )
        cmake.build(target='rocksdb')
        #cmake.install()

    def package(self):
        self.copy("LICENSE.Apache", src=self.source_subfolder, keep_path=False)
        self.copy("LICENSE.leveldb", src=self.source_subfolder, keep_path=False)
        self.copy("*.h", dst="include", src=("%s/include" % self.source_subfolder))
        self.copy("librocksdb.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rocksdb"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
