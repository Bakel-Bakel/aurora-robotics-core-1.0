cmake_minimum_required(VERSION 3.0.2)

project(fanuc_m710ic_description 0.5.1)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY meshes urdf
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
