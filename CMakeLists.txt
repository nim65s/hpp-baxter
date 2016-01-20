#
# Copyright (c) 2016 CNRS
# Authors: Joseph Mirabel
#
#
# This file is part of hpp-baxter
# hpp-baxter is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp-baxter is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp-baxter  If not, see
# <http://www.gnu.org/licenses/>.

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(CXX_DISABLE_WERROR TRUE)
INCLUDE(cmake/base.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME hpp-baxter)
SET(PROJECT_DESCRIPTION "Wrappers for Baxter robot in HPP.")
SET(PROJECT_URL "https://github.com/jmirabel/hpp-baxter")

FINDPYTHON()

SETUP_PROJECT()

# Activate hpp-util logging if requested
SET (HPP_DEBUG FALSE CACHE BOOL "trigger hpp-util debug output")
IF (HPP_DEBUG)
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DHPP_DEBUG")
ENDIF()

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

SETUP_PROJECT_FINALIZE()
