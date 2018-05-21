cmake_minimum_required(VERSION 3.1.2)
projecT(conanpoco CXX)
include(${CMAKE_CURRENT_SOURCE_DIR}/../conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


macro(use_cxx11)
  if(CMAKE_VERSION VERSION_LESS "3.1")
    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
      set (CMAKE_CXX_FLAGS "--std=gnu++11 ${CMAKE_CXX_FLAGS}")
    endif()
  else()
    set(CMAKE_CXX_STANDARD 11)
  endif()
endmacro()

if(CXX_14)
    message("Activating CXX_STANDARD 14")
    set(CMAKE_CXX_STANDARD 14)
else()
    message("Not activating CXX_STANDARD 14")
    message("Activating CXX_STANDARD 11")
    use_cxx11()
endif()


include("CMakeListsOriginal.cmake")
