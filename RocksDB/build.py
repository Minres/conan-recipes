#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="minres")
    cxxstds = ['11','14']
    libstdcxx = ['libstdc++', 'libstdc++11']
    shared = [True, False]
    for triple in [[c,l] for c in cxxstds for l in libstdcxx]:
        builder.add(
            settings={"compiler.libcxx":triple[1]},
            options={"stdcxx" : triple[0], "fPIC":True},
            env_vars={},
            build_requires={})
    builder.run()
