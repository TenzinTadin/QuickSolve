cmake_minimum_required(VERSION 3.12)
project(MyPythonProject VERSION 1.0.0)

# Configure setup.py file
configure_file(
  ${CMAKE_CURRENT_SOURCE_DIR}/CMake/setup.py.in
  ${CMAKE_CURRENT_BINARY_DIR}/setup.py
)

# Define custom target
add_custom_target(
  python_package
  COMMAND python ${CMAKE_CURRENT_BINARY_DIR}/setup.py sdist bdist_wheel
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  COMMENT "Creating Python package..."
)