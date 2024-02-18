if(TARGET autosdk)
  return()
endif()

get_filename_component(_IMPORT_PREFIX "${CMAKE_CURRENT_LIST_DIR}/../../" ABSOLUTE)

set(autosdk_INCLUDE_DIR "${_IMPORT_PREFIX}/RelWithDebInfo/include")

add_library(autosdk SHARED IMPORTED)
set_target_properties(autosdk PROPERTIES
  IMPORTED_CONFIGURATIONS "DEBUG;RELEASE;RELWITHDEBINFO;MINSIZEREL"
  INTERFACE_INCLUDE_DIRECTORIES "${autosdk_INCLUDE_DIR}"
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/Debug/autosdk.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/Debug/autosdk.dll"
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.dll"
  IMPORTED_IMPLIB_RELWITHDEBINFO "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.lib"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.dll"
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/RelWithDebInfo/autosdk.dll"
)

set(Autosdk_FOUND TRUE)
set(Autosdk_PROTO_FILES "${_IMPORT_PREFIX}/RelWithDebInfo/include/ADASISv3.proto")

string(TOUPPER "${CMAKE_BUILD_TYPE}" UPPER_BUILD_TYPE)
get_target_property(autosdk_LIBRARIES autosdk IMPORTED_LOCATION_${UPPER_BUILD_TYPE})

unset(_IMPORT_PREFIX)
