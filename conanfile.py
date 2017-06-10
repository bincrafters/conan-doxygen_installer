from conans import ConanFile, tools
import os


class CMakeInstallerConan(ConanFile):
    name = "doxygen"
    version = "1.8.13"
    license = "GNU GPL-2.0"
    description = "A documentation system for C++, C, Java, IDL and PHP --- Note: Dot is disabled in this package"
    url = "http://github.com/inexor-game/conan-doxygen"
    settings = {"os": ["Windows", "Linux"], "arch": ["x86", "x86_64"]}
#    options = {"build_from_source": [False, True]} NOT SUPPORTED YET
#    default_options = "build_from_source=False"
    exports = "FindDoxygen.cmake"

    def config(self):
        if self.settings.os == "Linux" and self.settings.arch == "x86":
            # self.options.build_from_source = True
            raise Exception("Not supported x86 for Linux")


    def get_download_filename(self):
        if self.settings.os == "Windows":
            if self.settings.arch == "x86":
                ending = "windows.bin.zip"
            else:
                ending = "windows.x64.bin.zip"
        else:
            ending = "linux.bin.tar.gz"

        return "doxygen-%s.%s" % (self.version, ending)
#       mac would be:
#       http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.13.dmg but I dunno how to install dmg files.

    def build(self):

        url = "http://ftp.stack.nl/pub/users/dimitri/%s" % self.get_download_filename()

#       source location:
#       http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.13.src.tar.gz

        dest_file = "file.tar.gz" if self.settings.os == "Linux" else "file.zip"
        self.output.warn("Downloading: %s" % url)
        tools.download(url, dest_file, verify=False)
        tools.unzip(dest_file)
        os.unlink(dest_file)
        doxyfile = "FindDoxygen.cmake"
        executeable = self.package_folder + "/doxygen"
        executeable = executeable.replace('\\', '/')
        if self.settings.os == "Windows":
            executeable += ".exe"

        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_EXECUTABLE", 'set(DOXYGEN_EXECUTABLE "{}" CACHE INTERNAL "")'.format(executeable))
        tools.replace_in_file(doxyfile, "## MARKER POINT: DOXYGEN_VERSION", 'set(DOXYGEN_VERSION "{}" CACHE INTERNAL "")'.format(self.version))

    def package(self):
        if self.settings.os == "Windows":
            srcdir = ""
        else:
            srcdir = "doxygen-%s/bin" % self.version
        self.copy("*", dst=".", src=srcdir)

    def package_info(self):
        self.env_info.path.append(self.package_folder)
