from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    archs = ['x86', 'x86_64']
    types = ['Debug','Release']
    cxxstds = ['98','11','14']
    configs = [[i,k] for i in cxxstds for k in types]
    for triple in configs:
        builder.add(settings={"build_type":triple[1]}, options={"stdcxx" : triple[0]}, env_vars={}, build_requires={})
    builder.run()
