cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

project(test_package)

find_package(Doxygen REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)

set(DOXYGEN_GENERATE_HTML NO)
set(DOXYGEN_GENERATE_MAN YES)
set(DOXYGEN_PROJECT_BRIEF "test package")
set(DOXYGEN_ALIASES
  [[conan="@conanio"]]
)
set(DOXYGEN_VERBATIM_VARS DOXYGEN_ALIASES)

doxygen_add_docs(docs test_package.cpp ALL COMMENT "generate HTML")
