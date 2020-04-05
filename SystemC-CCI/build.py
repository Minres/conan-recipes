#!/usr/bin/env python3
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="minres")
    types = ['Debug','Release']
    cxxstds = ['98', '11','14']
    libstdcxx = ['libstdc++', 'libstdc++11']
    shared = [True, False]
    for triple in [[i,k,l,s] for i in cxxstds for k in types for l in libstdcxx for s in shared]:
        if triple[0] != '98' or triple[2] != 'libstdc++11':
            builder.add(
                settings={"build_type":triple[1],"compiler.libcxx":triple[2]},
                options={"stdcxx" : triple[0], "shared" : triple[3]},
                env_vars={},
                build_requires={})
    builder.run()
