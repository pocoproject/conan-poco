cmake_minimum_required(VERSION 3.1.2)
project(MyHello CXX)
set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(echo EchoServer.cpp)
conan_target_link_libraries(echo)

add_executable(socket socket.cpp)
conan_target_link_libraries(socket)

add_executable(md5 md5.cpp)
conan_target_link_libraries(md5)

add_executable(sample SampleApp.cpp)
conan_target_link_libraries(sample)

