import unittest

import armored.__base as base


class TestBase(unittest.TestCase):
    def setUp(self):
        class Name(base.BaseUpdatableModel):
            name: str
            nickname: str

        self.name = Name

    def test_initialize(self):
        people = self.name(name="foo", nickname="bar")
        self.assertEqual("foo", people.name)
        self.assertEqual("bar", people.nickname)

    def test_update(self):
        people = self.name(name="foo", nickname="bar")
        people.update(data={"name": "new foo", "nickname": "new bar"})
        self.assertEqual("new foo", people.name)
        self.assertEqual("new bar", people.nickname)
