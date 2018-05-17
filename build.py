from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(gcc_versions=["7"])
    builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler.libcxx": "libstdc++11"},
                options={"Poco:shared": True}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "Debug", "compiler.libcxx": "libstdc++11"},
                options={"Poco:shared": True}, env_vars={}, build_requires={})    
    builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler.libcxx": "libstdc++11"},
                options={}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "Debug", "compiler.libcxx": "libstdc++11"},
                options={}, env_vars={}, build_requires={})    
    #builder.add_common_builds(shared_option_name="Poco:shared", pure_c=False)
    builder.run()
