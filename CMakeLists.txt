#
# Copyright (c) 2016, 2020 CNRS Authors: Joseph Mirabel, Guilhem Saurel
#

cmake_minimum_required(VERSION 3.10)

set(PROJECT_NAME hpp-baxter)
set(PROJECT_DESCRIPTION "Wrappers for Baxter robot in HPP.")

set(PROJECT_USE_CMAKE_EXPORT TRUE)

# Check if the submodule cmake have been initialized
set(JRL_CMAKE_MODULES "${CMAKE_CURRENT_LIST_DIR}/cmake")
if(EXISTS "${JRL_CMAKE_MODULES}/base.cmake")
  message(STATUS "JRL cmakemodules found in 'cmake/' git submodule")
else()
  find_package(jrl-cmakemodules QUIET CONFIG)
  if(jrl-cmakemodules_FOUND)
    get_property(
      JRL_CMAKE_MODULES
      TARGET jrl-cmakemodules::jrl-cmakemodules
      PROPERTY INTERFACE_INCLUDE_DIRECTORIES)
    message(STATUS "JRL cmakemodules found on system at ${JRL_CMAKE_MODULES}")
  elseif(${CMAKE_VERSION} VERSION_LESS "3.14.0")
    message(
      FATAL_ERROR
        "\nCan't find jrl-cmakemodules. Please either:\n"
        "  - use git submodule: 'git submodule update --init'\n"
        "  - or install https://github.com/jrl-umi3218/jrl-cmakemodules\n"
        "  - or upgrade your CMake version to >= 3.14 to allow automatic fetching\n"
    )
  else()
    message(STATUS "JRL cmakemodules not found. Let's fetch it.")
    include(FetchContent)
    FetchContent_Declare(
      "jrl-cmakemodules"
      GIT_REPOSITORY "https://github.com/jrl-umi3218/jrl-cmakemodules.git")
    FetchContent_MakeAvailable("jrl-cmakemodules")
    FetchContent_GetProperties("jrl-cmakemodules" SOURCE_DIR JRL_CMAKE_MODULES)
  endif()
endif()

include("${JRL_CMAKE_MODULES}/hpp.cmake")
include("${JRL_CMAKE_MODULES}/python.cmake")

compute_project_args(PROJECT_ARGS LANGUAGES CXX C)
project(${PROJECT_NAME} ${PROJECT_ARGS})

add_project_dependency(example-robot-data 3.9.1 REQUIRED)

findpython()

set(CATKIN_PACKAGE_SHARE_DESTINATION
    ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})

install(FILES package.xml DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(FILES urdf/box.urdf urdf/baxter.urdf urdf/baxter_colman.urdf
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf)
install(FILES srdf/box.srdf srdf/baxter.srdf srdf/baxter_manipulation.srdf
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/srdf)
install(FILES src/hpp/corbaserver/baxter/robot.py
              src/hpp/corbaserver/baxter/__init__.py
        DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/baxter)
install(FILES src/hpp/corbaserver/manipulation/baxter/robot.py
              src/hpp/corbaserver/manipulation/baxter/__init__.py
        DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/manipulation/baxter)

add_library(${PROJECT_NAME} INTERFACE)
install(
  TARGETS ${PROJECT_NAME}
  EXPORT ${TARGETS_EXPORT_NAME}
  DESTINATION lib)
install(FILES package.xml DESTINATION share/${PROJECT_NAME})
