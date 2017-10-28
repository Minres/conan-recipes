from conans import ConanFile, tools, AutoToolsBuildEnvironment


class SystemcverificationConan(ConanFile):
    name = "SystemCVerification"
    version = "2.0.0a"
    folder = "scv-2.0.0a-20161019"
    license = "Apache 2.0 License"
    url = "https://github.com/Minres/conan-recipes/blob/master/SystemCVerification"
    description = "The SystemC Verification (SCV) library provides a common set of APIs that are used as a basis to verification activities with SystemC"
    settings = "os", "compiler", "build_type", "arch"
    options = {"stdcxx":[98,11,14]}
    default_options = "stdcxx=98"
    generators = "txt"
    exports_sources = "scv-2.0.0a-20161019/*"
    requires = "SystemC/2.3.2@minres/stable"

    def configure(self):
        self.options["SystemC"].stdcxx = self.options.stdcxx
                
        # Maybe in windows we know that OpenSSL works better as shared (false)
        #if self.settings.os == "Windows":
        #    self.options["OpenSSL"].shared = True
                              
        # Or adjust any other available option
        #    self.options["Poco"].other_option = "foo"
                                                 
    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        if self.options.stdcxx == "14":
            env_build.cxx_flags = "-std=c++14"
        elif self.options.stdcxx == "11":
            env_build.cxx_flags = "-std=c++11"
        elif self.options.stdcxx == "98":
            env_build.cxx_flags = "-std=c++98"
        #env_build.libs.append("pthread")
        #env_build.defines.append("NEW_DEFINE=23")

        self.output.info(env_build.vars)
        with tools.environment_append(env_build.vars):
            self.run("cd %s &&  mkdir _build" % self.folder)
            configure_command = 'cd %s/_build && env && ../configure --prefix=%s/_install --with-systemc=%s --disable-debug --disable-opt' 
            self.output.info(configure_command % (self.folder, self.build_folder, self.deps_cpp_info["SystemC"].rootpath))
            self.run(configure_command % (self.folder, self.build_folder, self.deps_cpp_info["SystemC"].rootpath))
            self.run("cd %s/_build && make -j && make install" % self.folder)

    def package(self):
        # Headers
        self.copy(pattern="*.h", dst="include", src="_install/include", keep_path=True)
        # Libs
        self.copy(pattern="*", dst="lib", src="_install/lib-linux", keep_path=False)
        self.copy(pattern="*", dst="lib", src="_install/lib-linux64", keep_path=False)
        self.copy(pattern="*", dst="lib", src="_install/lib-macosx", keep_path=False)
        self.copy(pattern="*", dst="lib", src="_install/lib-macosx64", keep_path=False)
        self.copy(pattern="*", dst="lib", src="_install/lib-cygwin", keep_path=False)
        self.copy(pattern="*", dst="lib", src="_install/lib-mingw", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["scv"]
