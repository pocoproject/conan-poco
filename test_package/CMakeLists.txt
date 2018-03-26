cmake_minimum_required(VERSION 3.1.2)
project(MyHello CXX)
set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(echo EchoServer.cpp)
target_link_libraries(echo ${CONAN_LIBS})

add_executable(socket socket.cpp)
target_link_libraries(socket ${CONAN_LIBS})

add_executable(md5 md5.cpp)
target_link_libraries(md5 ${CONAN_LIBS})

add_executable(sample SampleApp.cpp)
target_link_libraries(sample ${CONAN_LIBS})

