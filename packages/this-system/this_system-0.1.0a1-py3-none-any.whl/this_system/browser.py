# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License  along with this
# program. If not, see <https://www.gnu.org/licenses/>

"""Classes and functons for working with Browser information"""

import re
import subprocess
from pathlib import Path
from platform import system, machine

from xdg.DesktopEntry import DesktopEntry


class Browser:
    """
    A browser class containing information about a browser.
    """

    def __init__(self, name: str, path: str):
        """

        :param name: the name of the browser
        :type name: str
        :param path: the path to th executable of the browser
        :type path: str
        """
        self.__browser_name__ = name
        self.__browser_path__ = path
        self.__browser_version__ = self.get_version_string()
        self.__browser_useragent__ = self.__get_useragent_string__()

    def get_version_string(self) -> str:
        """
        Retrieve the version string return by <executable> --version

        :return: the version
        :rtype: str
        """
        version_pattern = re.compile(r"\b(\S+\.\S+)\b")
        if system() == "Linux":
            try:
                version_string = (
                    subprocess.run(
                        [self.__browser_path__, "--version"],
                        check=True,
                        capture_output=True,
                        shell=False,
                    )
                    .stdout.decode()
                    .rstrip("\n")
                )
            except FileNotFoundError:
                pass
            else:
                match = version_pattern.search(version_string)
                if match:
                    return match[0]
        return None

    def __get_qtwebengine_version__(self) -> str:
        """
        Retrieve the version string of the installed QT webengine

        :return: the version
        :rtype: str
        """
        # Let's try dpkg first (debian based distros)
        try:
            libqt_version = subprocess.run(
                ["dpkg", "-s", "libqt5webengine5"],
                check=True,
                capture_output=True,
                shell=False,
            ).stdout.decode()
        except FileNotFoundError:
            pass
        else:
            for line in libqt_version.split("\n"):
                if line.startswith("Version"):
                    return line.split(" ")[1].split("+")[0]
        return None

    def __get_useragent_string__(self) -> str:
        """
        Construct the useragent string for a given browser

        :return: the useragent string
        :rtype: str
        """
        operating_system = system()
        arch = machine()

        product = "Mozilla"
        product_version = "5.0"
        rws = ""
        comment = ""

        khtml = "(KHTML, like Gecko)"

        if self.__browser_name__ in ["Chromium Web Browser"]:
            if operating_system == "Linux":
                rws = f"X11; {operating_system} {arch}"
            else:
                rws = f"{operating_system} {arch}"
            version_string = f"{self.__browser_version__.split('.')[0]}.0.0.0"
            comment = (
                f"AppleWebKit/537.36 {khtml} Chrome/{version_string} Safari/537.36"
            )
        elif self.__browser_name__ in ["Falkon"]:
            if operating_system == "Linux":
                rws = f"X11; {operating_system} {arch}"
            else:
                rws = f"{operating_system} {arch}"
            apple_webkit = "AppleWebKit/537.36"
            qt_webengine_version = self.__get_qtwebengine_version__()
            qt_webengine_string = f"QtWebEngine/{qt_webengine_version}"
            chrome = "Chrome/87.0.4280.144"
            safari = "Safari/537.36"
            comment = (
                f"{apple_webkit} {khtml} "
                ""
                f"{self.__browser_name__}/{self.__browser_version__} "
                f"{qt_webengine_string} {chrome} {safari}"
            )
        elif self.__browser_name__ in ["Firefox"]:
            if operating_system == "Linux":
                rws = f"X11; {operating_system} {arch}; rv:{self.__browser_version__}"
            else:
                rws = f"{operating_system} {arch}; rv:{self.__browser_version__}"
            comment = (
                f"Gecko/20100101 {self.__browser_name__}/{self.__browser_version__}"
            )
        elif self.__browser_name__ in ["Pale Moon"]:
            if operating_system == "Linux":
                rws = f"X11; {operating_system} {arch}; rv:102.0"
            else:
                rws = f"{operating_system} {arch}; rv:102.0"
            comment = (
                f"Gecko/20100101 Goanna/6.5 Firefox/102.0 "
                f"{self.__browser_name__}/{self.__browser_version__}"
            )
        return f"{product}/{product_version} ({rws}) {comment}"

    @property
    def name(self) -> str:
        """

        :return: the name of the browser
        :rtype: str
        """
        return self.__browser_name__

    @property
    def version(self) -> str:
        """

        :return: the version of the browser
        :rtype: str
        """
        return self.__browser_version__

    @property
    def path(self):
        """

        :return: the path to the executable of the browser
        :rtype: str
        """
        return self.__browser_path__

    @property
    def useragent(self) -> str:
        """

        :return: the useragent for this browser on this machine
        :rtype: str
        """
        return self.__browser_useragent__


def detect_installed_browsers() -> list[Browser]:
    """
    Return a list of installed browsers.

    :return: a list of installed browsers
    :rtype: list[Browser]
    """
    results = []
    if system() == "Linux":
        xdg_data_locations = (
            "~/.local/share/applications",
            "/usr/share/applications",
            "/var/lib/snapd/desktop/applications",
        )
        for data_location in xdg_data_locations:
            for desktop_file in Path(data_location).glob("*.desktop"):
                this_desktop_entry = DesktopEntry(desktop_file)
                if (
                    "WebBrowser" in this_desktop_entry.getCategories()
                    and this_desktop_entry.getGenericName() == "Web Browser"
                ):
                    browser_name = this_desktop_entry.getName()
                    browser_executable = this_desktop_entry.getExec().split()[0]
                    results.append(
                        Browser(
                            name=browser_name,
                            path=browser_executable,
                        )
                    )
    return results
