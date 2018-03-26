Conan Packages for POCO C++ Libraries
=====================================

[Conan.io](https://conan.io) package for [POCO](http://pocoproject.org/) library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/Poco/1.9.0/pocoproject/stable).

## Build Status

- Travis: [![Travis Build Status](https://travis-ci.org/pocoproject/conan-poco.svg?branch=master)](https://travis-ci.org/pocoproject/conan-poco)
- AppVeyor: [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/swn6l4rxpsgn8arg?svg=true)](https://ci.appveyor.com/project/obiltschnig/conan-poco)


## Build Packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload Packages to Server

    $ conan upload Poco/1.9.0@pocoproject/stable --all

## Reuse the Packages

### Basic Setup

    $ conan install Poco/1.9.0@pocoproject/stable

### Project Setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Poco/1.9.0@pocoproject/stable

    [options]
    Poco:shared=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all his dependencies) and generates
the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths
and variables that you need to link with your dependencies.

