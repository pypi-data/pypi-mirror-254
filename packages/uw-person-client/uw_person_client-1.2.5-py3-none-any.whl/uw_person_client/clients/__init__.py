# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


class AbstractUWPersonClient():

    def get_person_by_uwnetid(self, uwnetid):
        raise NotImplementedError()

    def get_person_by_uwregid(self, uwregid):
        raise NotImplementedError()

    def get_person_by_student_number(self, student_number):
        raise NotImplementedError()

    def get_persons(self, page=None, page_size=None):
        raise NotImplementedError()

    def get_registered_students(self):
        raise NotImplementedError()

    def get_active_students(self, page=None, page_size=None):
        raise NotImplementedError()

    def get_active_employees(self, page=None, page_size=None):
        raise NotImplementedError()

    def get_advisers(self, advising_program=None):
        raise NotImplementedError()

    def get_persons_by_adviser_netid(self, uwnetid):
        raise NotImplementedError()

    def get_persons_by_adviser_regid(self, uwregid):
        raise NotImplementedError()

    def _zfill_or_none(self, value, length):
        value = str(value).zfill(length) if (
            value and len(str(value)) > 0) else None
        if value == "0" * length:
            return None
        return value

    def format_system_key(self, value):
        return self._zfill_or_none(value, 9)

    def format_student_number(self, value):
        return self._zfill_or_none(value, 7)
