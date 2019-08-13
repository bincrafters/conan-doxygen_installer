cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

project(test_package)

find_package(Doxygen REQUIRED doxygen)

add_executable(${PROJECT_NAME} test_package.cpp)

doxygen_add_docs(docs ALL COMMENT "generate HTML")
