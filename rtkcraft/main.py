# -*- coding: utf-8 -*-

# RTKCraft generates kanji cards based on known morphs from MorphMan.
# Copyright (C) 2020  David Lõssenko  <lysenkodavid@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Initializes plugin.
"""

import sys

from rtkcraft.prerequisite_searcher import PrerequisiteSearcher


def main():
    ps = PrerequisiteSearcher()
    ps.get_morph_man()


if 'unittest' not in sys.modules:
    main()
