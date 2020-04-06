#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="minres")
    types = ['Debug','Release']
    for t in types:
        builder.add(settings={"build_type":t}, options={}, env_vars={}, build_requires={})
    builder.run()
