#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ros2_control_demo_example_6::ros2_control_demo_example_6" for configuration ""
set_property(TARGET ros2_control_demo_example_6::ros2_control_demo_example_6 APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ros2_control_demo_example_6::ros2_control_demo_example_6 PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libros2_control_demo_example_6.so"
  IMPORTED_SONAME_NOCONFIG "libros2_control_demo_example_6.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS ros2_control_demo_example_6::ros2_control_demo_example_6 )
list(APPEND _IMPORT_CHECK_FILES_FOR_ros2_control_demo_example_6::ros2_control_demo_example_6 "${_IMPORT_PREFIX}/lib/libros2_control_demo_example_6.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
