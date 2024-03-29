from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os

class SystemcverificationConan(ConanFile):
    name = "systemc-scv"
    version = "2.0.1"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemCVerification"
    description = "The SystemC Verification (SCV) library provides a common set of APIs that are used as a basis to verification activities with SystemC"
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "gcc"
    source_subfolder = "scv-2.0.1"
    exports_sources = "scv-2.0.1/*"
    requires = "systemc/2.3.3"

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        if self.settings.cppstd == "14":
            if self.settings.compiler.libcxx == 'libstdc++11':
                env_build.cxx_flags = "-std=gnu++14 -D_GLIBCXX_USE_CXX11_ABI=1"
            else:
                env_build.cxx_flags = "-std=gnu++14 -D_GLIBCXX_USE_CXX11_ABI=0"
        elif self.settings.cppstd == "11":
            if self.settings.compiler.libcxx == 'libstdc++11':
                env_build.cxx_flags = "-std=gnu++11 -D_GLIBCXX_USE_CXX11_ABI=1"
            else:
                env_build.cxx_flags = "-std=gnu++11 -D_GLIBCXX_USE_CXX11_ABI=0"
        elif self.settings.cppstd == "98":
            env_build.cxx_flags = "-std=gnu++98"
        env_build.fpic = True
        tools.mkdir("build")
        # make sure timestamps are correct to avoid invocation of autoconf tools
        tools.touch("%s/aclocal.m4"  % os.path.join(self.source_folder, self.source_subfolder))
        tools.touch("%s/Makefile.in" % os.path.join(self.source_folder, self.source_subfolder))
        tools.touch("%s/configure"   % os.path.join(self.source_folder, self.source_subfolder))
        env_build.libs.remove('systemc')
        with tools.chdir("build"):
            env_build.configure(
                configure_dir=os.path.join(self.source_folder, self.source_subfolder),    
                args=[
                    '--prefix=%s' % os.path.join(self.source_folder, 'install'),
                    '--with-systemc=%s' % self.deps_cpp_info["systemc"].rootpath,
                    '--enable-static=no' if self.options.shared else '--enable-static=yes', 
                    '--enable-shared=yes' if self.options.shared else '--enable-shared=no',
                    '--disable-debug' if self.settings.build_type == "Release" else '--disable-opt'
                    ]
                )
            env_build.make()
            env_build.make(args=["install"])
            #env_build.make(args=["check"])

    def package(self):
        # Headers
        self.copy(pattern="*.h", dst="include", src="install/include", keep_path=True)
        # Libs
        self.copy(pattern="*", dst="lib", src="install/lib-linux", keep_path=False)
        self.copy(pattern="*", dst="lib", src="install/lib-linux64", keep_path=False)
        self.copy(pattern="*", dst="lib", src="install/lib-macosx", keep_path=False)
        self.copy(pattern="*", dst="lib", src="install/lib-macosx64", keep_path=False)
        self.copy(pattern="*", dst="lib", src="install/lib-cygwin", keep_path=False)
        self.copy(pattern="*", dst="lib", src="install/lib-mingw", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["scv"]
