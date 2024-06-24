#! /usr/bin/env python3

#    Project Lepus: a videogame library manager
#    Copyright (C) 2024  Ethan Blahay
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser

import lepus

def main():
    # parse arguments
    parser = ArgumentParser()

    parser.add_argument(
        "--version",
        version="Project Lepus 0.x.y-alpha",
        action="version"
    )

    args = parser.parse_args()

    # run application
    g = lepus.Game()
    g.title = "Metroid Fusion"
    g.exe_path = "/usr/bin/notify-send"

    print(g.exe_path)


if __name__ == "__main__":
    main()