#!/usr/bin/env python3
from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    types = ['Debug','Release']
    for t in types:
        builder.add(settings={"build_type":t}, options={}, env_vars={}, build_requires={})
    builder.run()
