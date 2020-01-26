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
Implements PrerequisiteSearcher.
"""

import importlib
from rtkcraft.config import config


class PrerequisiteSearcher:
    """Used for loading and checking the plugin prerequisites for RTKCraft.

    Attributes:
        _morph_man (module): The loaded MorphMan module.
    """
    def __init__(self):
        self._morph_man = None

    def get_morph_man(self):
        """Gets the morphman plugin.

        Returns:
            module: The MorphMan module if found.

        Raises:
            RuntimeException: When the MorphMan module wasn't found.
        """
        if self._morph_man is None:
            mm_plugin_name = config['morphman_plugin_name']
            mm_plugin_id = config['morphman_plugin_id']

            if importlib.util.find_spec(mm_plugin_name):
                self._morph_man = importlib.import_module(mm_plugin_name)

            if self._morph_man is None and importlib.util.find_spec(mm_plugin_id):
                self._morph_man = importlib.import_module(mm_plugin_id)

            if self._morph_man is None:
                raise RuntimeError('MorphMan plugin is a prerequisite for {} to work.'.format(config['plugin_name']))

        return self._morph_man
