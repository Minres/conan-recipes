from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os
import shutil

class TccConan(ConanFile):
    name = "tcc"
    revision = "1645616843"
    version = "0.9.27"
    license = "GNU Lesser General Public License"
    author = "Eyck Jentzsch <eyck@minres.com>"
    url = "https://github.com/Minres/conan-recipes/tree/master/TCC"
    description = "TinyCC (aka TCC) is a small but hyper fast C compiler. Unlike other C compilers, it is meant to be self-relying: you do not need an external assembler or linker because TCC does that for you."
    topics = ("compiler", "c")
    settings = "os", "compiler", "build_type", "arch"
    default_options = {}
    git_repo = "git://repo.or.cz/tinycc.git"
    #generators = "cmake"
    sub_folder = "tcc-%s" % version
    exports_sources = "tcc-%s/*" % version

    def source(self):
        self.output.info("Cloning from %s" % self.git_repo)
        git = tools.Git(folder=self.sub_folder)
        if os.path.exists(self.sub_folder):
            shutil.rmtree(self.sub_folder) 
        git.clone(self.git_repo)
        git.checkout(self.revision)

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
