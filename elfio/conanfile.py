from conans import ConanFile, CMake, tools


class ElfioConan(ConanFile):
    name = "elfio"
    version = "1.3.2"
    license = "MIT License"
    url = "http://git.code.sf.net/p/elfio/code"
    description = "ELFIO is a header-only C++ library intended for reading and generating files in the ELF binary format"
    no_copy_source = True

    def source(self):
        self.run("git clone http://git.code.sf.net/p/elfio/code")

    def package(self):
        self.copy("elfio/*.hpp", dst="include", src="code")

    def package_info(self):
        self.info.header_only()

