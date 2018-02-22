from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    archs = ['x86', 'x86_64']
    types = ['Debug','Release']
    cxxstds = ['98', '11','14']
    shared = [True,False]
    configs = [[i,k,s] for i in cxxstds for k in types for s in shared]
    for triple in configs:
        builder.add(settings={"build_type":triple[1]}, options={"stdcxx" : triple[0], "shared" : triple[2]}, env_vars={}, build_requires={})
    builder.run()
