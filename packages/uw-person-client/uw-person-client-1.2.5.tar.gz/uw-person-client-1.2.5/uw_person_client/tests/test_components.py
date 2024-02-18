# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from unittest import TestCase
from uw_person_client.components import AbstractBase, Term


class AbstractBaseTest(TestCase):

    def test_attributes(self):
        ab = AbstractBase()
        ab.property1 = "value1"
        ab.property2 = "value2"
        self.assertEqual(ab.property1, "value1")
        self.assertEqual(ab.property2, "value2")

        with self.assertRaises(AttributeError):
            ab.foobar


class TermTest(TestCase):
    def test_quarter_name(self):
        term = Term()

        with self.assertRaises(AttributeError):
            term.quarter_name
        term.quarter = 0
        self.assertEqual(term.quarter_name, None)
        term.quarter = 1
        self.assertEqual(term.quarter_name, "Winter")
        term.quarter = 4
        self.assertEqual(term.quarter_name, "Autumn")
