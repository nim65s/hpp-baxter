#!/usr/bin/env python
# Copyright (c) 2016 CNRS
# Author: Joseph Mirabel
#

from hpp.corbaserver.robot import Robot as Parent


#
#  Control of robot Baxter in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp-corbaserver. It derive from class hpp.corbaserver.robot.Robot.
#
#  At creation of an instance, the urdf and srdf files are loaded using
#  idl interface hpp::corbaserver::Robot::loadRobotModel.
class Robot(Parent):
    #
    #  Information to retrieve urdf and srdf files.
    packageName = "hpp-baxter"
    meshPackageName = "baxter_description"
    rootJointType = "anchor"
    #
    #  Information to retrieve urdf and srdf files.
    urdfName = "baxter"
    urdfSuffix = "_colman"
    srdfSuffix = ""

    def __init__(self, robotName, load=True, **kwargs):
        Parent.__init__(self, robotName, self.rootJointType, load, **kwargs)
        self.tf_root = "base_footprint"
