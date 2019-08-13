from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os
import shutil


class DoxygenInstallerConan(ConanFile):
    name = "doxygen_installer"
    version = "1.8.16"
    description = "A documentation system for C++, C, Java, IDL and PHP --- Note: Dot is disabled in this package"
    topics = ("conan", "doxygen", "installer", "devtool", "documentation")
    url = "https://github.com/bincrafters/conan-doxygen_installer"
    homepage = "https://github.com/doxygen/doxygen"
    author = "Inexor <info@inexor.org>"
    license = "GPL-2.0-only"
    exports = ["LICENSE", "FindDoxygen.cmake"]
    exports_sources = ["FindDoxygen.cmake"]

    settings = {"os_build": ["Windows", "Linux", "Macos"], "arch_build": ["x86", "x86_64"]}
#   options = {"build_from_source": [False, True]} NOT SUPPORTED YET
#   default_options = "build_from_source=False"

    def config(self):
        if self.settings.os_build in ["Linux", "Macos"] and self.settings.arch_build == "x86":
            raise ConanInvalidConfiguration("x86 is not supported on Linux or Macos")


    def get_download_filename(self):
        program = "doxygen"

        if self.settings.os_build == "Windows":
            if self.settings.arch_build == "x86":
                ending = "windows.bin.zip"
            else:
                ending = "windows.x64.bin.zip"
        elif self.settings.os_build == "Macos":
            program = "Doxygen"
            ending = "dmg"
        else:
            ending = "linux.bin.tar.gz"


        return "%s-%s.%s" % (program, self.version, ending)

    def unpack_dmg(self, dest_file):
        mount_point = os.path.join(self.build_folder, "mnt")
        tools.mkdir(mount_point)
        self.run("hdiutil attach -mountpoint %s %s" % (mount_point, dest_file))
        try:
            for program in ["doxygen", "doxyindexer", "doxysearch.cgi"]:
                shutil.copy(os.path.join(mount_point, "Doxygen.app", "Contents",
                                         "Resources", program), self.build_folder)
            shutil.copy(os.path.join(mount_point, "Doxygen.app", "Contents",
                                    "Frameworks", "libclang.dylib"), self.build_folder)
        finally:
            self.run("diskutil eject %s" % (mount_point))
            tools.rmdir(mount_point)

    def build(self):
        # source location:
        # https://downloads.sourceforge.net/project/doxygen/rel-1.8.16/doxygen-1.8.16.linux.bin.tar.gz

        url = "http://downloads.sourceforge.net/project/doxygen/rel-{}/{}".format(self.version, self.get_download_filename())

        if self.settings.os_build == "Linux":
            dest_file = "file.tar.gz"
        elif self.settings.os_build == "Macos":
            dest_file = "file.dmg"
        else:
            dest_file = "file.zip"

        self.output.warn("Downloading: {}".format(url))
        tools.download(url, dest_file, verify=False)
        if self.settings.os_build == "Macos":
            self.unpack_dmg(dest_file)
            # Redirect the path of libclang.dylib to be adjacent to the doxygen executable, instead of in Frameworks
            self.run('install_name_tool -change "@executable_path/../Frameworks/libclang.dylib" "@executable_path/libclang.dylib" doxygen')
        else:
            tools.unzip(dest_file)
        os.unlink(dest_file)

        doxyfile = "FindDoxygen.cmake"
        executeable = "doxygen"
        if self.settings.os_build == "Windows":
            executeable += ".exe"

    def package(self):
        if self.settings.os_build == "Linux":
            srcdir = "doxygen-{}/bin".format(self.version)
            self.copy("*", dst=".", src=srcdir)

        self.copy("doxygen", dst="bin")
        self.copy("doxyindexer", dst="bin")
        self.copy("doxysearch.cgi", dst="bin")
        self.copy("*.exe", dst="bin")
        self.copy("*.dylib", dst="bin")
        self.copy("*.dll", dst="bin")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder,"bin"))
