# -*- coding: utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup.py module for the workflow's worker utilities.

All the workflow related code is gathered in a package that will be built as a
source distribution, staged in the staging area for the workflow being run and
then installed in the workers when they start running.  This behavior is
triggered by specifying the --setup_file command line option when running the
workflow for remote execution.
"""

import logging
import subprocess
from distutils.command.build import build as _build

import setuptools

logger = logging.getLogger(__name__)


class Build(_build):
    """A build command class that will be invoked during package install.

    The package built using the current setup.py will be staged and later
    installed in the worker using `pip install package'. This class will be
    instantiated during install for this specific scenario and will trigger
    running the custom commands specified.
    """

    sub_commands = _build.sub_commands + [("CustomCommands", None)]


# Some custom command to run during setup. The command is not essential for
# this workflow. It is used here as an example. Each command will spawn a child
# process. Typically, these commands will include steps to install non-Python
# packages. For instance, to install a C++-based library libjpeg62 the
# following two commands will have to be added:
#
#     ['apt-get', 'update'],
#     ['apt-get', '--assume-yes', install', 'libjpeg62'],
#
# First, note that there is no need to use the sudo command because the setup
# script runs with appropriate access.
# Second, if apt-get tool is used then the first command needs to be 'apt-get
# update' so the tool refreshes itself and initializes links to download
# repositories.  Without this initial step the other apt-get install commands
# will fail with package not found errors. Note also --assume-yes option which
# shortcuts the interactive confirmation.
#
# The output of custom commands (including failures) will be logged in the
# worker-startup log.
CUSTOM_COMMANDS = []


class CustomCommands(setuptools.Command):
    """A setuptools Command class able to run arbitrary commands."""

    def initialize_options(self):
        """Set default values for all options that this command supports."""
        pass

    def finalize_options(self):
        """Set final values for all the options that this command supports."""
        pass

    def RunCustomCommand(self, command_list):
        """Run custom commands via a subprocess."""
        print("Running command: {}".format(command_list))
        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        stdout_data, _ = p.communicate()
        print("Command output: {}".format(stdout_data))
        if p.returncode != 0:
            raise RuntimeError(
                "Command {} failed: exit code: {}".format(
                    command_list, p.returncode
                )
            )

    def run(self):
        """Run custom commands defined by CUSTOM_COMMANDS."""
        for command in CUSTOM_COMMANDS:
            self.RunCustomCommand(command)


with open("requirements-worker.txt") as f:
    worker_requirements = f.read().splitlines()

setuptools.setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.project_short_description}}",
    author="{{cookiecutter.maintainer_name}}",
    author_email="{{cookiecutter.email}}",
    install_requires=worker_requirements,
    packages=setuptools.find_packages(),
    cmdclass={"build": Build, "CustomCommands": CustomCommands},
)
