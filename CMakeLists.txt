cmake_minimum_required(VERSION 3.0.2)
project(jetauto_gazebo)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
