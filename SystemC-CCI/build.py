from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    archs = ['x86', 'x86_64']
    types = ['Debug','Release']
    cxxstds = ['98','11','14']
    libstdcxx = ['libstdc++', 'libstdc++11']
    #-s compiler.libcxx=libstdc++
    configs = [[i,k,l] for i in cxxstds for k in types for l in libstdcxx]
    for triple in configs:
        builder.add(settings={"build_type":triple[1], "compiler.libcxx":triple[2]}, options={"stdcxx" : triple[0]}, env_vars={}, build_requires={})
    builder.run()
