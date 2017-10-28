from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    cxxstds = ['98','11','14']
    archs = ['x86', 'x86_64']
    types = ['Debug','Release']
    #configs = [[i,j,k] for i in cxxstds for j in archs for k in types]
    #for triple in configs:
    #    builder.add(settings={"arch": triple[1], "build_type":triple[2]}, options={"SystemC:stdcxx" : triple[0]}, env_vars={}, build_requires={})
    configs = [[i,k] for i in cxxstds for k in types]
    for triple in configs:
        builder.add(settings={"build_type":triple[1]}, options={"SystemC:stdcxx" : triple[0]}, env_vars={}, build_requires={})
    builder.run()
