#.rst:
# FindDoxygen
# -----------
#
# This module looks for Doxygen and the path to Graphviz's dot
#
# Doxygen is a documentation generation tool.  Please see
# http://www.doxygen.org
#
# This module accepts the following optional variables:
#
# ::
#
#    DOXYGEN_SKIP_DOT       = If true this module will skip trying to find Dot
#                             (an optional component often used by Doxygen)
#
#
#
# This modules defines the following variables:
#
# ::
#
#    DOXYGEN_EXECUTABLE     = The path to the doxygen command.
#    DOXYGEN_FOUND          = Was Doxygen found or not?
#    DOXYGEN_VERSION        = The version reported by doxygen --version
#
#
#
# ::
#
#    DOXYGEN_DOT_EXECUTABLE = The path to the dot program used by doxygen.
#    DOXYGEN_DOT_FOUND      = Was Dot found or not?
#
# For compatibility with older versions of CMake, the now-deprecated
# variable ``DOXYGEN_DOT_PATH`` is set to the path to the directory
# containing ``dot`` as reported in ``DOXYGEN_DOT_EXECUTABLE``.
# The path may have forward slashes even on Windows and is not
# suitable for direct substitution into a ``Doxyfile.in`` template.
# If you need this value, use :command:`get_filename_component`
# to compute it from ``DOXYGEN_DOT_EXECUTABLE`` directly, and
# perhaps the :command:`file(TO_NATIVE_PATH)` command to prepare
# the path for a Doxygen configuration file.

#=============================================================================
# Copyright 2001-2009 Kitware, Inc.
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
#  License text for the above reference.)

# For backwards compatibility support
if(Doxygen_FIND_QUIETLY)
  set(DOXYGEN_FIND_QUIETLY TRUE)
endif()


#
# Find Doxygen...
#

#find_program(DOXYGEN_EXECUTABLE
#  NAMES doxygen
#  PATHS
#    "[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\doxygen_is1;Inno Setup: App Path]/bin"
#    /Applications/Doxygen.app/Contents/Resources
#    /Applications/Doxygen.app/Contents/MacOS
#  DOC "Doxygen documentation generation tool (http://www.doxygen.org)"
#)

## MARKER POINT: DOXYGEN_EXECUTABLE
## MARKER POINT: DOXYGEN_VERSION

set(DOXYGEN_SKIP_DOT ON)
set(DOXYGEN_FOUND ON)

#
# Backwards compatibility...
#

if(APPLE)
  # Restore the old app-bundle setting setting
  set(CMAKE_FIND_APPBUNDLE ${TEMP_DOXYGEN_SAVE_CMAKE_FIND_APPBUNDLE})
endif()

# Maintain the _FOUND variables as "YES" or "NO" for backwards compatibility
# (allows people to stuff them directly into Doxyfile with configure_file())
if(DOXYGEN_FOUND)
  set(DOXYGEN_FOUND "YES")
else()
  set(DOXYGEN_FOUND "NO")
endif()
if(DOXYGEN_DOT_FOUND)
  set(DOXYGEN_DOT_FOUND "YES")
else()
  set(DOXYGEN_DOT_FOUND "NO")
endif()

# For backwards compatibility support
set (DOXYGEN ${DOXYGEN_EXECUTABLE} )
set (DOT ${DOXYGEN_DOT_EXECUTABLE} )

mark_as_advanced(
  DOXYGEN_EXECUTABLE
  DOXYGEN_DOT_EXECUTABLE
  )
