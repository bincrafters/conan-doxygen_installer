cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

project(test_package)

find_package(Doxygen REQUIRED)

set(DOXYGEN_GENERATE_HTML YES)
set(DOXYGEN_GENERATE_MAN NO)

set(DOXYGEN_PROJECT_BRIEF "test package")
set(DOXYGEN_ALIASES
  [[conan="@conanio"]]
)
set(DOXYGEN_VERBATIM_VARS DOXYGEN_ALIASES)

# https://gitlab.kitware.com/cmake/cmake/issues/18738
set(DOXYGEN_LATEX_MAKEINDEX_CMD makeindex)

add_executable(${PROJECT_NAME} test_package.cpp)

doxygen_add_docs(doxygen ${PROJECT_SOURCE_DIR} COMMENT "generate HTML")
