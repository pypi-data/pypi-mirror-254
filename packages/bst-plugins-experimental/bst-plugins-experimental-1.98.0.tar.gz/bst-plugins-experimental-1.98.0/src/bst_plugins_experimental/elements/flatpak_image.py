# Copyright (c) 2017 freedesktop-sdk
# Copyright (c) 2018 Codethink Limited
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Authors:
#        Valentin David <valentin.david@gmail.com>
#        Thomas Coldrick <thomas.coldrick@codethink.co.uk>


"""Flatpak Image Element

.. _flatpak_image:

A buildstream plugin used to stage its build-dependencies, and metadata
provided by the 'metadata' field in a format useful to generate flatpaks.
"""
import configparser
import os

from buildstream import Element


class FlatpakImageElement(Element):

    BST_MIN_VERSION = "2.0"
    BST_STRICT_REBUILD = True
    BST_FORBID_RDEPENDS = True
    BST_FORBID_SOURCES = True

    def configure(self, node):
        node.validate_keys(["directory", "include", "exclude", "metadata"])
        self.directory = self.node_subst_vars(node.get_scalar("directory"))
        self.include = node.get_str_list("include")
        self.exclude = node.get_str_list("exclude")
        self.metadata = configparser.ConfigParser()
        self.metadata.optionxform = str
        self.metadata_dict = {}
        metadata_node = node.get_mapping("metadata")
        for section, pairs in metadata_node.items():
            section_dict = {}
            for key, value in pairs.items():
                section_dict[key] = self.node_subst_vars(value)
            self.metadata_dict[section] = section_dict

        self.metadata.read_dict(self.metadata_dict)

    def preflight(self):
        pass

    def get_unique_key(self):
        key = {}
        key["directory"] = self.directory
        key["include"] = sorted(self.include)
        key["exclude"] = sorted(self.exclude)
        key["metadata"] = self.metadata_dict
        key["version"] = 2  # Used to force rebuilds after editing the plugin
        return key

    def configure_sandbox(self, sandbox):
        pass

    def stage(self, sandbox):
        stagedir = os.path.join(os.sep, "buildstream", "allfiles")
        with self.timed_activity("Staging dependencies", silent_nested=True):
            self.stage_dependency_artifacts(
                sandbox,
                path=stagedir,
                include=self.include,
                exclude=self.exclude,
            )

    def assemble(self, sandbox):
        self.stage_sources(sandbox, "input")

        basedir = sandbox.get_virtual_directory()
        allfiles = basedir.open_directory("buildstream/allfiles", create=True)
        reldirectory = os.path.relpath(self.directory, "/")
        installdir = basedir.open_directory("buildstream/install", create=True)
        filesdir = installdir.open_directory("files", create=True)

        if self.metadata.has_section("Application"):
            installdir.open_directory("export", create=True)

        for section in self.metadata.sections():
            if section.startswith("Extension "):
                extensiondir = self.metadata.get(section, "directory")
                installdir.open_directory(
                    os.path.join("files", extensiondir),
                    create=True,
                )

        if allfiles.exists(reldirectory):
            subdir = allfiles.open_directory(reldirectory)
            filesdir.import_files(subdir)
        if allfiles.exists("etc"):
            etcdir = allfiles.open_directory("etc")
            filesetcdir = filesdir.open_directory("etc", create=True)
            filesetcdir.import_files(etcdir)

        with installdir.open_file("metadata", mode="w") as m:
            self.metadata.write(m)
        return os.path.join(os.sep, "buildstream", "install")


def setup():
    return FlatpakImageElement
