
# Name: Makefile
# Author: Lucas Haug
# 05/2021

# Program options
EXECUTABLE ?= loader
WORKING_DIR ?= P1/Loader

###############################################################################
## Output configuration
###############################################################################

VERBOSE ?= 0

# Verbosity
ifeq ($(VERBOSE),0)
AT := @
else
AT :=
endif

###############################################################################
## Input files
###############################################################################

# Build directory
BUILD_DIR := build/$(WORKING_DIR)

# Source files and headers
SOURCES = $(shell find $(WORKING_DIR)/src -name "*.cpp")
HEADERS = $(shell find $(WORKING_DIR)/inc -name "*.h")

# Object files
OBJECTS:= $(addprefix $(BUILD_DIR)/,$(notdir $(SOURCES:.cpp=.o)))

vpath %.cpp $(sort $(dir $(SOURCES)))

###############################################################################
## Compiler settings
###############################################################################

FLAGS := -g -Wall -Wextra -std=c++11
COMPILER := g++

# Include paths
C_INCLUDES  := $(addprefix -I,                            \
	$(sort $(dir $(HEADERS)))                             \
)

FLAGS += $(C_INCLUDES)

###############################################################################
## Build Targets
###############################################################################

all: $(BUILD_DIR)/$(EXECUTABLE)

$(BUILD_DIR)/$(EXECUTABLE): $(OBJECTS)
	$(AT)$(COMPILER) $(FLAGS) -o $@ $(OBJECTS)

$(BUILD_DIR)/%.o: %.cpp | $(BUILD_DIR)
	$(AT)$(COMPILER) $(FLAGS) -o $@ -c $^

$(BUILD_DIR):
	$(AT)echo "Creating build directory"
	$(AT)mkdir -p $@

###############################################################################
## Auxiliary Targets
###############################################################################

clean:
	$(AT)rm -rf $(BUILD_DIR)

run: all
ifeq ($(OS), Windows_NT)
	$(AT)start powershell -NoExit ./$(BUILD_DIR)/$(EXECUTABLE)
else
	$(AT)./$(BUILD_DIR)/$(EXECUTABLE)
endif

# Format source code using uncrustify
format:
	$(AT)uncrustify -c uncrustify.cfg --replace --no-backup $(SOURCES) $(HEADERS)

###############################################################################

.PHONY: all clean run format