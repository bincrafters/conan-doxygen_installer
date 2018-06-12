from conans import ConanFile, tools
import os


class DoxygenConan(ConanFile):
    name = "doxygen"
    version = "1.8.13"
    license = "GNU GPL-2.0"
    description = "A documentation system for C++, C, Java, IDL and PHP --- Note: Dot is disabled in this package"
    url = "http://github.com/inexorgame/conan-doxygen"
    settings = {"os": ["Windows", "Linux", "Macos"], "arch": ["x86", "x86_64"]}
#    options = {"build_from_source": [False, True]} NOT SUPPORTED YET
#    default_options = "build_from_source=False"
    exports = "FindDoxygen.cmake"

    def config(self):
        if self.settings.os in ["Linux", "Macos"] and self.settings.arch == "x86":
            # self.options.build_from_source = True
            raise Exception("Not supported x86 for Linux or Macos")


    def get_download_filename(self):
        if self.settings.os == "Windows":
            if self.settings.arch == "x86":
                ending = "windows.bin.zip"
            else:
                ending = "windows.x64.bin.zip"
        elif self.settings.os == "Macos":
            program = "Doxygen"
            ending = "dmg"
        else:
            ending = "linux.bin.tar.gz"


        return "%s-%s.%s" % (program, self.version, ending)


    def build(self):

        url = "http://ftp.stack.nl/pub/users/dimitri/%s" % self.get_download_filename()

#       source location:
#       http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.13.src.tar.gz

        if self.settings.os == "Linux":
            dest_file = "file.tar.gz"
        elif self.settings.os == "Macos":
            dest_file = "file.dmg"
        else:
            dest_file = "file.zip"
        self.output.warn("Downloading: %s" % url)
        tools.download(url, dest_file, verify=False)
        tools.unzip(dest_file)
        os.unlink(dest_file)
        doxyfile = "FindDoxygen.cmake"
        executeable = "doxygen"
        if self.settings.os == "Windows":
            executeable += ".exe"

        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_EXECUTABLE", 'set(DOXYGEN_EXECUTABLE "${CONAN_DOXYGEN_ROOT}/%s" CACHE INTERNAL "")' % executeable)
        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_VERSION", 'set(DOXYGEN_VERSION "%s" CACHE INTERNAL "")' % self.version)

    def package(self):
        if self.settings.os == "Windows":
            srcdir = ""
        else:
            srcdir = "doxygen-%s/bin" % self.version
        self.copy("*", dst=".", src=srcdir)

    def package_info(self):
        self.env_info.path.append(self.package_folder)
