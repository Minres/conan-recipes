# conan-recipes

A bunch of conan recipes to package C++ libraries. The packages of those recipes can be found at https://bintray.com/minres/conan-repo


# How to build the packages on your own

Install https://github.com/conan-io/conan-package-tools to build all needed combinations

## Seasocks

to build all variations run

```
cd Seasocks
CONAN_USERNAME=<username> CONAN_CHANNEL=<channel name> python build.py
```

to build a specific variant run the following commands:

```
conan create . Seasocks/1.3.2@<username>/<channel name>  -s build_type=<build type> -s compiler.libcxx=<libstdc++ variant>
```

## SystemC

download the SystemC distribution from http://www.accellera.org/downloads/standards/systemc and unpack into the SystemC directory

```
cd SystemC
CONAN_USERNAME=<username> CONAN_CHANNEL=<channel name> python build.py
```

to build a specific variant run the following command

```
conan create . SystemC/2.3.2@minres/<channel name>  -o stdcxx=<c++ std variant> -s build_type=<build type>
```

where <c++ std variant> is one of 98, 11, or 14

## SystemC Verification library

download the SystemC distribution from http://www.accellera.org/downloads/standards/systemc and unpack into the SystemCVerification directory and apply the patch scv4systemc-2.3.2.patch

```
cd SystemCVerification
CONAN_USERNAME=<username> CONAN_CHANNEL=<channel name> python build.py
```

to build a specific variant run the following command

```
conan create . SystemCVerification/2.0.1a@minres/<channel name>  -o stdcxx=<c++ std variant> -s build_type=<build type>
```

where <c++ std variant> is one of 98, 11, or 14

## uploading

Uploading can be done using
```
conan upload  <package name>/<package version>@<user name>/<channel> --all -r=<remote name>
```
