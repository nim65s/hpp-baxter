#
# Copyright (c) 2016 CNRS
# Authors: Joseph Mirabel
#
#

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(CXX_DISABLE_WERROR TRUE)
INCLUDE(cmake/base.cmake)
INCLUDE(cmake/hpp.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME hpp-baxter)
SET(PROJECT_DESCRIPTION "Wrappers for Baxter robot in HPP.")

FINDPYTHON()

SETUP_HPP_PROJECT()

ADD_REQUIRED_DEPENDENCY("hpp-corbaserver >= 3")

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
install (FILES
  src/hpp/corbaserver/baxter/robot.py
  src/hpp/corbaserver/baxter/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/baxter)
install (FILES
  src/hpp/corbaserver/manipulation/baxter/robot.py
  src/hpp/corbaserver/manipulation/baxter/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/manipulation/baxter)

SETUP_HPP_PROJECT_FINALIZE()
