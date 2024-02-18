cmake_minimum_required(VERSION 3.26)
project(asio VERSION 1.29.0)

set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/asio/include)

# target
add_library(${PROJECT_NAME} INTERFACE)
target_include_directories(${PROJECT_NAME} INTERFACE
  $<BUILD_INTERFACE:${INCLUDE_DIR}>
  $<INSTALL_INTERFACE:include>
)
target_compile_definitions(${PROJECT_NAME} INTERFACE ASIO_STANDALONE)

# install
include(GNUInstallDirs)
install(DIRECTORY ${INCLUDE_DIR}/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Targets INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(EXPORT ${PROJECT_NAME}Targets FILE ${PROJECT_NAME}Targets.cmake DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME})

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Version.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME}
)

install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Version.cmake"
    DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME}
)