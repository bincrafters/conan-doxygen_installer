#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake

class TestPackageConan(ConanFile):
    generators = "cmake_paths"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def test(self):
        self.output.info("Version:")
        self.run("doxygen --version", run_environment=True)
