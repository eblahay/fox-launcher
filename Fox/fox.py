#    Project Fox: a videogame library manager
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
    A file for Fox App-related code to go.
    This will probably change later.
"""

import sqlite3

import os
import subprocess

class Fox:
    """
        a representation of a single instance of the Fox Application
    """
    def __init__(self):
        userdata_dir = os.path.join(os.environ['HOME'], '.local', 'share', 'fox-launcher')
        games_db_path = os.path.join(userdata_dir, 'games.db')

        # check whether userdata dir exists
        if not os.path.isdir(userdata_dir):
            os.mkdir(userdata_dir)

        # check whether db file exists & set flag accordingly
        f_new_db = not os.path.exists(games_db_path)

        # create initial database objects
        try:
            self.db = sqlite3.connect(
                games_db_path
            )
        except sqlite3.OperationalError as e:
            print("ERROR: Unable to open database")
            os.sys.exit(1)

        self.cur = self.db.cursor()
        cur = self.cur

        if f_new_db:
            self.createDB()

    def __del__(self):
        # close database
        self.db.close()

    def createDB(self):
        # create database
        self.cur.execute("CREATE TABLE games(id INTEGER PRIMARY KEY, title, platform, exe)")

        # commit; mk chgs permanent
        self.db.commit()

    def addGame(self, id, platform, exe, title):
        self.cur.execute(f"""
            INSERT INTO games VALUES
                ({id}, '{title}', '{platform}', '{exe}')
        """)

        # commit; mk chgs permanent
        self.db.commit()

    def ls(self):
        # returns list of all contents of 'game' table

        self.cur.execute("""
            SELECT
                id,
                title,
                platform,
                exe
            FROM
                games;
        """)
        return self.cur.fetchall()

    def run(self, gameid):
        # runs game corresponding to the given ID

        platform = self.cur.execute("SELECT platform FROM games WHERE id = ?", (str(gameid))).fetchone()[0]
        exe = self.cur.execute("SELECT exe FROM games WHERE id = ?", (str(gameid))).fetchone()[0]

        match platform:
            case 'linux':
                subprocess.Popen([exe], start_new_session=True)
            case 'windows':
                WINE = "/usr/bin/wine"
                subprocess.Popen([WINE, exe], start_new_session=True)

