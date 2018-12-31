#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        self.output.info("Version:")
        self.run("doxygen --version")
