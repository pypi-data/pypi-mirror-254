#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "correctionlib" for configuration "Release"
set_property(TARGET correctionlib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(correctionlib PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/correctionlib/lib/correctionlib.dll"
  )

list(APPEND _cmake_import_check_targets correctionlib )
list(APPEND _cmake_import_check_files_for_correctionlib "${_IMPORT_PREFIX}/correctionlib/lib/correctionlib.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
