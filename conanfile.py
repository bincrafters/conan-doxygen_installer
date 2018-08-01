from conans import ConanFile, CMake, tools
import os


class DoxygenConan(ConanFile):
    name = "doxygen"
    version = "1.8.14"
    license = "GPL-2.0"
    description = "A documentation system for C++, C, Java, IDL and PHP --- Note: Dot is disabled in this package"
    url = "https://github.com/inexorgame/conan-doxygen"
    requires = "flex/2.6.4@bincrafters/stable"
    settings = "arch", "build_type", "compiler", "os"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "use_libclang": [True, False]
    }
    default_options = "shared=False", "fPIC=True", "use_libclang=False"
    exports = ["LICENSE", "FindDoxygen.cmake"]
    exports_sources = ["CMakeLists.txt", "FindDoxygen.cmake"]
    generators = "cmake"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        archive_name = "Release_{!s}".format(self.version.replace('.', '_'))
        archive_url = "https://github.com/doxygen/doxygen/archive/{!s}.zip".format(archive_name)
        tools.get(archive_url, sha256="552355c4accf9a0027814460c475f9472658ba923b91e387e8110090a6c5248c")
        os.rename("doxygen-{!s}".format(archive_name), self.source_subfolder)

        doxyfile = "FindDoxygen.cmake"
        cmakefile = "{!s}/CMakeLists.txt".format(self.source_subfolder)
        executeable = "doxygen"
        if self.settings.os == "Windows":
            executeable += ".exe"

        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_EXECUTABLE", 'set(DOXYGEN_EXECUTABLE "${CONAN_DOXYGEN_ROOT}/%s" CACHE INTERNAL "")' % executeable)
        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_VERSION", 'set(DOXYGEN_VERSION "%s" CACHE INTERNAL "")' % self.version)

        tools.replace_in_file(cmakefile, "include(version)", "include('${CMAKE_CURRENT_SOURCE_DIR}/cmake/version.cmake')")


    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["win_static"] = "ON" if self.settings.os == 'Windows' and self.options.shared == False else "OFF"
        cmake.definitions["use_libclang"] = "ON" if self.options.use_libclang else "OFF"

        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)

        if self.settings.os == "Linux":
            srcdir = "doxygen-%s/bin" % self.version
            self.copy("*", dst=".", src=srcdir)

        self.copy("doxygen", dst=".")
        self.copy("doxyindexer", dst=".")
        self.copy("doxysearch.cgi", dst=".")
        self.copy("*.exe", dst=".")
        self.copy("*.dylib", dst=".")
        self.copy("*.dll", dst=".")
        self.copy("*.cmake", dst=".")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # self.env_info.path.append(self.package_folder)
