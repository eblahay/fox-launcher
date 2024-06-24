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

import os
from argparse import ArgumentParser

f_verbose = False

def log(msg):
	"""
	prints a statement to the CLI
	if run in 'verbose mode'
	"""

	if f_verbose:
		print(msg)

def main():
	# parse arguments
	parser = ArgumentParser()

	parser.add_argument(
	"-v", "--verbose",
		action="store_true"
	)

	args = parser.parse_args()

	# handle parsed args
	f_verbose = args.verbose

	print(f_verbose)

	# body
	os.environ['HOME'] = os.path.join(os.path.dirname(__file__), "data")
	log("env[HOME] = " + os.environ['HOME'])

if __name__ == "__main__":
	main()
