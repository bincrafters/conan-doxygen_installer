#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build(target="doxygen")

    def test(self):
        self.output.info("Version:")
        self.run("doxygen --version")
