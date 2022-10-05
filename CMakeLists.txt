#
# Copyright (c) 2016, 2020 CNRS Authors: Joseph Mirabel, Guilhem Saurel
#

cmake_minimum_required(VERSION 3.1)

set(PROJECT_NAME hpp-baxter)
set(PROJECT_DESCRIPTION "Wrappers for Baxter robot in HPP.")

set(PROJECT_USE_CMAKE_EXPORT TRUE)

include(cmake/hpp.cmake)
include(cmake/python.cmake)

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
