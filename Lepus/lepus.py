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

"""
    A file for Lepus App-related code to go.
    This will probably change later.
"""

class Game:
    """
    represents the concept of a single "Videogame"
    in the collection
    """

    def __init__(self):
        self.title = ""
        self.exe_path = ""
        
