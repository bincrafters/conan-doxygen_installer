[![Download](https://api.bintray.com/packages/bincrafters/public-conan/doxygen_installer%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/doxygen_installer%3Abincrafters/_latestVersion)
[![Build Status Travis](https://travis-ci.com/bincrafters/conan-doxygen_installer.svg?branch=stable%2F1.8.15)](https://travis-ci.com/bincrafters/conan-doxygen_installer)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-doxygen_installer?branch=stable%2F1.8.15&svg=true)](https://ci.appveyor.com/project/bincrafters/conan-doxygen_installer)

## Conan package recipe for [*doxygen_installer*](https://github.com/doxygen/doxygen)

A documentation system for C++, C, Java, IDL and PHP --- Note: Dot is disabled in this package

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/bincrafters/public-conan/doxygen_installer%3Abincrafters).


## Issues

If you wish to report an issue or make a request for a Bincrafters package, please do so here:

[Bincrafters Community Issues](https://github.com/bincrafters/community/issues)


## For Users

### Basic setup

    $ conan install doxygen_installer/1.8.15@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    doxygen_installer/1.8.15@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . bincrafters/stable




## Add Remote

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package doxygen_installer.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/bincrafters/conan-doxygen_installer/blob/stable/1.8.15/LICENSE.md)
