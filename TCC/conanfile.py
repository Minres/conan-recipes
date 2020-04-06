from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class TccConan(ConanFile):
    name = "tcc"
    version = "0.9.27"
    license = "GNU Lesser General Public License"
    author = "Eyck Jentzsch <eyck@minres.com>"
    url = "https://github.com/Minres/conan-recipes/tree/master/TCC"
    description = "TinyCC (aka TCC) is a small but hyper fast C compiler. Unlike other C compilers, it is meant to be self-relying: you do not need an external assembler or linker because TCC does that for you."
    topics = ("compiler", "c")
    settings = "os", "compiler", "build_type", "arch"
    default_options = {}

    source_tar = "http://download.savannah.gnu.org/releases/tinycc/tcc-%s.tar.bz2" % version
    #generators = "cmake"
    sub_folder = "tcc-%s" % version
    exports_sources = "tcc-%s/*" % version

    def source(self):
        self.output.info("Downloading %s" %self.source_tar)
        tools.download(self.source_tar, "tcc.tar.bz2")
        tools.unzip("tcc.tar.bz2")
        os.remove("tcc.tar.bz2")

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.fpic = True
        with tools.chdir("%s/%s" % (self.source_folder, self.sub_folder)):
            autotools.configure()
            autotools.make()
            autotools.make(target="install")

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["tcc"]
