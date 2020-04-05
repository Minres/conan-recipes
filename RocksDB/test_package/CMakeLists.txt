project(PackageTest CXX)
cmake_minimum_required(VERSION 3.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(rocks_sample rocksdb.cpp)
target_link_libraries(rocks_sample CONAN_PKG::rocksdb)
target_link_libraries(rocks_sample CONAN_PKG::gflags)
