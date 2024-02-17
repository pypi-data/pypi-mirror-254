import unittest

import armored.catalogs as catalogs


class TestBaseTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_base_table_init(self):
        t = catalogs.BaseTbl(
            name="foo",
            schemas=[catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )


class TestTable(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_table_init(self):
        t = catalogs.Tbl(
            name="foo",
            schemas=[catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertListEqual(
            t.schemas,
            [catalogs.Col(name="foo", dtype="varchar( 10 )")],
        )
        self.assertEqual(t.pk, catalogs.Pk(of="foo"))
        self.assertListEqual(t.fk, [])

        t = catalogs.Tbl(
            name="foo", schemas=[{"name": "foo", "dtype": "varchar( 100 )"}]
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"max_length": 100, "type": "varchar"},
                        "fk": {},
                        "name": "foo",
                        "nullable": True,
                        "pk": False,
                        "unique": False,
                    }
                ],
                "pk": {"cols": [], "of": "foo"},
                "fk": [],
            },
        )

        t = catalogs.Tbl(
            name="foo",
            schemas=[{"name": "foo", "dtype": "varchar( 100 ) primary key"}],
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"max_length": 100, "type": "varchar"},
                        "fk": {},
                        "name": "foo",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    }
                ],
                "pk": {"cols": ["foo"], "of": "foo"},
                "fk": [],
            },
        )

    def test_table_init_with_pk(self):
        t = catalogs.Tbl(
            name="foo",
            schemas=[{"name": "id", "dtype": "integer", "pk": True}],
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "integer"},
                        "fk": {},
                        "name": "id",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    }
                ],
                "pk": {"cols": ["id"], "of": "foo"},
                "fk": [],
            },
        )

    def test_table_model_validate(self):
        t = catalogs.Tbl.model_validate(
            {
                "name": "foo",
                "schemas": [
                    {"name": "id", "dtype": "integer", "pk": True},
                    {
                        "name": "name",
                        "dtype": "varchar( 256 )",
                        "nullable": False,
                    },
                ],
            },
        )
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "name": "foo",
                "schemas": [
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "integer"},
                        "fk": {},
                        "name": "id",
                        "nullable": False,
                        "pk": True,
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "dtype": {"type": "varchar", "max_length": 256},
                        "fk": {},
                        "name": "name",
                        "nullable": False,
                        "pk": False,
                        "unique": False,
                    },
                ],
                "pk": {"cols": ["id"], "of": "foo"},
                "fk": [],
            },
        )
