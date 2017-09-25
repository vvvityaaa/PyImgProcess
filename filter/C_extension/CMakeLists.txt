cmake_minimum_required(VERSION 3.8)
project(variancemodule)

set(CMAKE_C_STANDARD 11)

set(SOURCE_FILES extensionModule.c)
add_executable(variancemodule ${SOURCE_FILES})