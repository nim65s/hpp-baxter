#
# Copyright (c) 2016, 2020 CNRS
# Authors: Joseph Mirabel, Guilhem Saurel
#
#

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

SET(PROJECT_NAME hpp-baxter)
SET(PROJECT_DESCRIPTION "Wrappers for Baxter robot in HPP.")

SET(PROJECT_USE_CMAKE_EXPORT TRUE)

INCLUDE(cmake/hpp.cmake)
INCLUDE(cmake/python.cmake)

COMPUTE_PROJECT_ARGS(PROJECT_ARGS LANGUAGES CXX C)
PROJECT(${PROJECT_NAME} ${PROJECT_ARGS})

ADD_PROJECT_DEPENDENCY(example-robot-data 3.9.1 REQUIRED)

FINDPYTHON()

SET(CATKIN_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})

install(FILES
  package.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )
install(FILES
  urdf/box.urdf
  urdf/baxter.urdf
  urdf/baxter_colman.urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
  )
install(FILES
  srdf/box.srdf
  srdf/baxter.srdf
  srdf/baxter_manipulation.srdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/srdf
  )
install(DIRECTORY meshes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install (FILES
  src/hpp/corbaserver/baxter/robot.py
  src/hpp/corbaserver/baxter/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/baxter)
install (FILES
  src/hpp/corbaserver/manipulation/baxter/robot.py
  src/hpp/corbaserver/manipulation/baxter/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/manipulation/baxter)

ADD_LIBRARY(${PROJECT_NAME} INTERFACE)
INSTALL(TARGETS ${PROJECT_NAME} EXPORT ${TARGETS_EXPORT_NAME} DESTINATION lib)
INSTALL(FILES package.xml DESTINATION share/${PROJECT_NAME})
