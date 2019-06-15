from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    libstd = ['libstdc++11']
    types = ['Debug','Release']
    shared = [True,False]
    configs = [[i,k] for i in shared for k in types]
    for triple in configs:
        builder.add(settings={"build_type":triple[1]}, options={"shared":triple[0]}, env_vars={}, build_requires={})
    builder.run()
