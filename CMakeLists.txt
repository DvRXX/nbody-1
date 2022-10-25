cmake_minimum_required(VERSION 3.16)
project(nbody)

set(CMAKE_CXX_STANDARD 20)

add_executable(nbody
        nbody.cpp)
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libstdc++ -static-libgcc -static")
