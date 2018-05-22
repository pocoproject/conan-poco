from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={"arch": "x86_64", "build_type": "Release"},
                options={"*:shared": True}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
                options={"*:shared": True}, env_vars={}, build_requires={})    
    builder.add(settings={"arch": "x86_64", "build_type": "Release"},
                options={}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
                options={}, env_vars={}, build_requires={})    
    #builder.add_common_builds(shared_option_name="Poco:shared", pure_c=False)
    builder.run()
