from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    libstd = ['libstdc++11']
    types = ['Debug','Release']
    configs = [[i,k] for i in libstd for k in types]
    for triple in configs:
        builder.add(settings={"build_type":triple[1], "compiler.libcxx":triple[0]}, options={}, env_vars={}, build_requires={})
    builder.run()
