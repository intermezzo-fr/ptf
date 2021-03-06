#!/usr/bin/env python
#####################################
# Installation module for smbexec
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (purehate)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update "

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/leebaird/discover.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="discover"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION},./setup.sh,exit""
