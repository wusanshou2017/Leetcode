# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\CLion 2019.1.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\CLion 2019.1.3\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = E:\lc\dfs_tree

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = E:\lc\dfs_tree\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/dfs_tree.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/dfs_tree.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/dfs_tree.dir/flags.make

CMakeFiles/dfs_tree.dir/main.cpp.obj: CMakeFiles/dfs_tree.dir/flags.make
CMakeFiles/dfs_tree.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=E:\lc\dfs_tree\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/dfs_tree.dir/main.cpp.obj"
	D:\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\dfs_tree.dir\main.cpp.obj -c E:\lc\dfs_tree\main.cpp

CMakeFiles/dfs_tree.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/dfs_tree.dir/main.cpp.i"
	D:\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E E:\lc\dfs_tree\main.cpp > CMakeFiles\dfs_tree.dir\main.cpp.i

CMakeFiles/dfs_tree.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/dfs_tree.dir/main.cpp.s"
	D:\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S E:\lc\dfs_tree\main.cpp -o CMakeFiles\dfs_tree.dir\main.cpp.s

# Object files for target dfs_tree
dfs_tree_OBJECTS = \
"CMakeFiles/dfs_tree.dir/main.cpp.obj"

# External object files for target dfs_tree
dfs_tree_EXTERNAL_OBJECTS =

dfs_tree.exe: CMakeFiles/dfs_tree.dir/main.cpp.obj
dfs_tree.exe: CMakeFiles/dfs_tree.dir/build.make
dfs_tree.exe: CMakeFiles/dfs_tree.dir/linklibs.rsp
dfs_tree.exe: CMakeFiles/dfs_tree.dir/objects1.rsp
dfs_tree.exe: CMakeFiles/dfs_tree.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=E:\lc\dfs_tree\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable dfs_tree.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\dfs_tree.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/dfs_tree.dir/build: dfs_tree.exe

.PHONY : CMakeFiles/dfs_tree.dir/build

CMakeFiles/dfs_tree.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\dfs_tree.dir\cmake_clean.cmake
.PHONY : CMakeFiles/dfs_tree.dir/clean

CMakeFiles/dfs_tree.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" E:\lc\dfs_tree E:\lc\dfs_tree E:\lc\dfs_tree\cmake-build-debug E:\lc\dfs_tree\cmake-build-debug E:\lc\dfs_tree\cmake-build-debug\CMakeFiles\dfs_tree.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/dfs_tree.dir/depend

