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
Tests PrerequisiteSearcher.
"""

import sys
from unittest import TestCase
from unittest.mock import patch, call, MagicMock


class TestPrerequisiteSearcher(TestCase):
    PrerequisiteSearcher = None
    config = None

    @classmethod
    def setUpClass(cls):
        sys.modules['aqt'] = MagicMock()
        sys.modules['anki'] = MagicMock()

        from rtkcraft.config import config
        from rtkcraft.prerequisite_searcher import PrerequisiteSearcher

        TestPrerequisiteSearcher.config = config
        TestPrerequisiteSearcher.PrerequisiteSearcher = PrerequisiteSearcher

    def setUp(self):
        self.prerequisite_searcher = TestPrerequisiteSearcher.PrerequisiteSearcher()

    @patch('importlib.util.find_spec')
    def test_no_morphman_plugin_found(self, find_spec):
        mm_plugin_name = TestPrerequisiteSearcher.config['morphman_plugin_name']
        mm_plugin_id = TestPrerequisiteSearcher.config['morphman_plugin_id']
        find_spec.side_effect = [False, False]

        self.assertRaises(RuntimeError, self.prerequisite_searcher.get_morph_man)

        find_spec.assert_has_calls([
            call(mm_plugin_name),
            call(mm_plugin_id)
        ])

    @patch('importlib.util.find_spec')
    @patch('importlib.import_module')
    def test_morphman_plugin_by_name_found(self, import_module, find_spec):
        mm_plugin_name = TestPrerequisiteSearcher.config['morphman_plugin_name']
        find_spec.side_effect = [True]
        import_module.side_effect = ["success return"]

        plugin_return = self.prerequisite_searcher.get_morph_man()

        find_spec.assert_called_once_with(mm_plugin_name)
        import_module.assert_called_once_with(mm_plugin_name)
        self.assertIsNotNone(plugin_return)

    @patch('importlib.util.find_spec')
    @patch('importlib.import_module')
    def test_morphman_plugin_by_id_found_and_caches(self, import_module, find_spec):
        mm_plugin_id = TestPrerequisiteSearcher.config['morphman_plugin_id']
        find_spec.side_effect = [False, True]
        import_module.side_effect = ["success return"]

        plugin_return = self.prerequisite_searcher.get_morph_man()
        plugin_return2 = self.prerequisite_searcher.get_morph_man()

        find_spec.assert_has_calls([
            call(TestPrerequisiteSearcher.config['morphman_plugin_name']),
            call(mm_plugin_id)
        ])
        import_module.assert_called_once_with(mm_plugin_id)
        self.assertIsNotNone(plugin_return)
        self.assertIsNotNone(plugin_return2)
