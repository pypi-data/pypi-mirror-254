# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from functools import reduce
from itertools import starmap
import io
import os
import re

from six import string_types


class Version:
    """
    The software component version numbering is mostly inspired from
    Apache version numbering or similar other version numbering such as
    Semantic Versioning.  Version numbers are denoted using a standard
    tuple of integers: ``major.minor.patch``.

    A ``major`` version identifies the product stage of the project.  The
    basic intent is that ``major`` versions are incompatible, large-scale
    upgrades of the software component.  This enables a check of a client
    application against the latest version of the software component to
    ensure compatibility.  If there is a discrepancy between the two, the
    client application MUST be updated accordingly.

    A ``minor`` version is incremented when substantial new functionality
    or improvement are introduced; the ``major`` version number doesn't
    change.  A ``minor`` version retains backward compatibility with older
    minor versions.  It is NOT forward compatible as a previous ``minor``
    version doesn't include new functionality or improvement that has been
    introduced in this newer ``minor`` version.

    A ``patch`` version is incremented when bugs were fixed or
    implementation details were refactored.  The ``major`` and ``minor``
    version don't change.  A ``patch`` version is backward and forward
    compatible with older and newer patches of the same major and minor
    version.

    References:

    * Apache Portable Runtime (APR)'s Version Numbering
      (http://apr.apache.org/versioning.html)
    * Semantic Versioning (http://semver.org/)
    * PEP 386 - Changing the version comparison module in Distutils
      (http://www.python.org/dev/peps/pep-0386/)
    """
    # Name of the file in which the version of an application is commonly
    # written.
    DEFAULT_VERSION_FILE_NAME = 'VERSION'

    # Regular expression that matches the string representation of a version
    # denoted using a standard tuple of integers ``major.minor.patch``.
    # REGEX_VERSION = re.compile(r'^(\d+)(.(\d+)(.(\d+)){0,1}){0,1}$')
    REGEX_PATTERN_SEMANTIC_VERSION = r'^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'

    def __eq__(self, other: Version) -> int:
        result = self.compare_versions(
            (self.__major, self.__minor, self.__patch),
            (other.major, other.minor, other.patch)
        )
        return result == 0

    def __ge__(self, other) -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __gt__(self, other) -> bool:
        result = self.compare_versions(
            (self.__major, self.__minor, self.__patch),
            (other.major, other.minor, other.patch)
        )
        return result > 0

    def __init__(self, value, *args):
        """
        Build a ``Version`` instance providing the version of a software
        component as either:

        - A string representation of a semantic versioning 3-component number
          (at least 1);

        - From 1 to 3 integers representing, in that particular order, ``major``,
          ``minor``, and ``patch``;

        - A tuple of 3 integers ``(major, minor, patch)``.

        For example:

        ```python
        >>> Version("1")
        >>> Version("1.2")
        >>> Version("1.2.8")
        >>> Version(1)
        >>> Version(1, 2)
        >>> Version(1, 2, 8)
        >>> Version((1,))
        >>> Version((1, 2)
        >>> Version((1, 2, 8))
        ```


        :param value: Either a string representation of a software component
            of the following format: ``major.minor.patch``, or a tuple of 3
            integers `(major, minor, patch)`, or an integer representing the
            `major` component number.

        :param args: 1 or 2 integers for respectively the `minor`, and `patch`
            component numbers of the version, when the argument `value` passed
            to this function is an integer (the `major` component number).
        """
        if isinstance(value, string_types):
            self.__major, self.__minor, self.__patch, self.__prerelease, self.__build_metadata = self.__convert_string_to_version_component_numbers(value)
        elif isinstance(value, tuple):
            self.__major, self.__minor, self.__patch = value + (0,) * (3 - len(value))
            self.__prerelease = self.__build_metadata = None
        elif isinstance(value, int):
            minor_patch = args or ()
            minor_patch += (0,) * (2 - len(minor_patch))
            self.__major, self.__minor, self.__patch = (value,) + minor_patch
            self.__prerelease = self.__build_metadata = None
        else:
            raise ValueError(f"Invalid value '{value}'")

    def __le__(self, other: Version) -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __lt__(self, other: Version) -> bool:
        result = self.compare_versions(
            (self.__major, self.__minor, self.__patch),
            (other.major, other.minor, other.patch)
        )
        return result < 0

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}({self.__major}, { self.__minor}, {self.__patch})'

    def __str__(self) -> str:
        return f'{self.__major}.{self.__minor}.{self.__patch}'

    @property
    def build_metadata(self) -> str or None:
        """
        Return the build metadata when defined.

        Build metadata is intended to track build maturity when preparing an
        application for a public release of any kind, including pre-releases.

        It can sometimes be helpful to include information such as:

        - The exact git hash of the commit used to produce the current build.

        - The release channel of the build.  For example, is this build a very
          experimental and potentially broken "nightly" release, a semi-stable
          "beta" release containing a few new experimental features, or a
          robust and well-tested "stable" release?

        - Whether the project as a whole is alpha-level quality (the entire
          project is pretty new and experimental).


        :return: The build metadata or ``None``.
        """
        return self.__build_metadata

    @staticmethod
    def compare_versions(
            this: (int, int, int),
            other: (int, int, int)
    ) -> int:
        """
        Compare a version to another.


        :param this: A tuple ``(major, minor, patch)``.

        :param other: One other tuple ``(major, minor, patch)``.


        :return: A negative integer if the first version passed to this
            function is below the second version passed, ``0`` if these two
            versions are equivalent, or a positive integer if the first
            version is above the second version.
        """
        return reduce(
            lambda a, b: 1 if a == 1 else -1 if a == -1 else b,
            # Use the function `starmap` instead ot the built-in function `map` as
            # Python 3 doesn't allow tuple parameter unpacking as `map(lambda (a, b): ...`.
            starmap(
                lambda a, b: 1 if a > b else -1 if a < b else 0,
                zip(this, other)
            )
        )

    @classmethod
    def __convert_string_to_version_component_numbers(
            cls,
            s: str,
            strict: bool = True
    ) -> (int, int, int, str, str):
        """
        Convert the string representation of a semantic versioning 3-component
        number into a tuple of integers `(major, minor, patch)`.

        If only 1-component number is given, the function returns `minor` and
        `patch` equal to `0`.


        :param s: A string representation of a semantic version 1- or
            3-component number.

        :param strict: Indicate whether the string ``s`` needs to strictly
            comply with Semantic Version.


        :return: A tuple of integers `(major. minor, patch, prerelease, build_metadata)`.


        :raise ValueError: If the string ``s`` doesn't comply with Semantic
            Versioning while the argument ``strict`` is ``true``.
        """
        if not isinstance(s, string_types):
            raise ValueError(f"The argument 's' is of the wrong type '{type(s)}'")

        if s is None and strict:
            raise ValueError(f"The argument 's' MUST NOT be null")

        match = re.match(cls.REGEX_PATTERN_SEMANTIC_VERSION, s.strip())
        if match:
            major = match.group('major')
            minor = match.group('minor')
            patch = match.group('patch')
            prerelease = match.group('prerelease')
            build_metadata = match.group('buildmetadata')

            return int(major), int(minor or 0), int(patch or 0), prerelease, build_metadata
        elif strict:
            raise ValueError(f"The argument 's' doesn't comply with Semantic Versioning")

    @classmethod
    def from_file(cls, path: str, file_name: str = None) -> Version:
        """
        Return a version written in a file.


        :param path: The absolute path of the version file.

        :param file_name: The name of the file where the version is written in.
            It defaults to {@link Version.DEFAULT_VERSION_FILE_NAME}.


        :return: An object {@link Version}.
        """
        version_file_path_name = os.path.join(path, file_name or cls.DEFAULT_VERSION_FILE_NAME)
        with io.open(version_file_path_name, mode='rt', encoding='utf-8') as fd:
            version = Version(fd.read())

        return version

    @staticmethod
    def from_string(s: str) -> Version or None:
        """
        Return the version corresponding to the specified string.


        :param s: A string representing a version.


        :return: The version corresponding to the string, or ``None`` if the
            argument ``s`` is null.
        """
        return s and Version(s)

    @property
    def major(self) -> int:
        return self.__major

    @property
    def minor(self) -> int:
        return self.__minor

    @property
    def patch(self) -> int:
        return self.__patch

    @property
    def prerelease(self) -> str or None:
        """
        Return the pre-release version when defined.

        A pre-release version indicates that the version is unstable and might
        not satisfy the intended compatibility requirements as denoted by its
        associated normal version.


        :return: The pre-release version or ``None``.
        """
        return self.__prerelease