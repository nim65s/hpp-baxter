#!/usr/bin/env python
# Copyright (c) 2016 CNRS
# Author: Joseph Mirabel
#

from hpp.corbaserver.manipulation.robot import Robot as Parent

##
#  Control of robot Baxter in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp-manipulation-corba. It derive from class hpp.corbaserver.manipulation.robot.Robot.
#
#  At creation of an instance, the urdf and srdf files are loaded using
#  idl interface hpp::corbaserver::Robot::loadRobotModel.
class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    urdfFilename = "package://hpp-baxter/urdf/baxter.urdf"
    srdfFilename = "package://hpp-baxter/srdf/baxter_manipulation.srdf"

    ## Constructor
    # \param compositeName name of the composite robot that will be built later,
    # \param robotName name of the first robot that is loaded now,
    # \param load whether to actually load urdf files. Set to no if you only
    #        want to initialize a corba client to an already initialized
    #        problem.
    # \param rootJointType type of root joint among ("freeflyer", "planar",
    #        "anchor"),
    def __init__ (self, compositeName, robotName, load = True,
                  rootJointType = "anchor", **kwargs):
        Parent.__init__ (self, compositeName, robotName, rootJointType, load, **kwargs)
        self.tf_root = "base_footprint"
