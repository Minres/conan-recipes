# conan-recipes

A bunch of conan recipes to package C++ libraries. The packages of those recipes can be found at https://bintray.com/minres/conan-repo


# How to build the packages on your own

Install https://github.com/conan-io/conan-package-tools to build all needed combinations

## SystemC Verification library

download the SystemC distribution from http://www.accellera.org/downloads/standards/systemc and unpack into the SystemCVerification directory and apply the patch scv4systemc-2.3.2.patch

```
cd systemc-cci
python3 build.py
```

to build a specific variant run the following command

```
conan create . -s build_type=<build type>
```

where <c++ std variant> is one of 98, 11, or 14

## uploading

Uploading can be done using
```
conan upload  <package name>/<package version>@<user name>/<channel> --all -r=<remote name>
```

# Problems

If you are going to build the packages under Linux using gcc you might run into linker issues. You can try to fix this by setting a the C++11 libstdc++. This can be done by adding `-s compiler.libcxx=libstdc++11` to the package build calls.
