import unittest

import armored.catalogs as catalogs
import armored.dtypes as dtypes


class TestBaseColumn(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_base_column_init(self):
        t = catalogs.BaseCol(name="foo", dtype={"type": "base"})
        self.assertEqual("foo", t.name)
        self.assertEqual("base", t.dtype.type)

        t = catalogs.BaseCol(name="foo", dtype="varchar( 100 )")
        self.assertEqual("foo", t.name)
        self.assertEqual("varchar", t.dtype.type)
        self.assertEqual(100, t.dtype.max_length)

        t = catalogs.BaseCol(
            name="foo", dtype={"type": "varchar", "max_length": 100}
        )
        self.assertEqual("foo", t.name)
        self.assertEqual("varchar", t.dtype.type)
        self.assertEqual(100, t.dtype.max_length)

    def test_base_column_model_validate(self):
        t = catalogs.BaseCol.model_validate(
            {
                "name": "foo",
                "dtype": {
                    "type": "varchar",
                    "max_length": 1000,
                },
            }
        )
        self.assertEqual("foo", t.name)
        self.assertEqual("varchar", t.dtype.type)
        self.assertEqual(1000, t.dtype.max_length)

        t = catalogs.BaseCol.model_validate(
            {
                "name": "foo",
                "dtype": {"type": "int"},
            }
        )
        self.assertEqual("foo", t.name)
        self.assertEqual("integer", t.dtype.type)


class TestColumn(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_column_init(self):
        t = catalogs.Col(name="foo", dtype=dtypes.BaseType())
        self.assertDictEqual(
            {
                "name": "foo",
                "dtype": {"type": "base"},
                "nullable": True,
                "unique": False,
                "default": None,
                "check": None,
                "pk": False,
                "fk": {},
            },
            t.model_dump(by_alias=False),
        )

        t = catalogs.Col(name="foo", dtype={"type": "base"})
        self.assertDictEqual(
            {
                "name": "foo",
                "dtype": {"type": "base"},
                "nullable": True,
                "unique": False,
                "default": None,
                "check": None,
                "pk": False,
                "fk": {},
            },
            t.model_dump(by_alias=False),
        )

        t = catalogs.Col(name="foo", dtype="base")
        self.assertDictEqual(
            {
                "name": "foo",
                "dtype": {"type": "base"},
                "nullable": True,
                "unique": False,
                "default": None,
                "check": None,
                "pk": False,
                "fk": {},
            },
            t.model_dump(by_alias=False),
        )

        t = catalogs.Col(
            name="foo",
            dtype="varchar( 20 )",
            fk={"table": "bar", "column": "baz"},
        )
        self.assertDictEqual(
            {
                "name": "foo",
                "dtype": {"max_length": 20, "type": "varchar"},
                "nullable": True,
                "unique": False,
                "default": None,
                "check": None,
                "pk": False,
                "fk": {"table": "bar", "column": "baz"},
            },
            t.model_dump(by_alias=False),
        )

    def test_column_extract_column_from_dtype(self):
        t = catalogs.Col.extract_column_from_dtype("numeric( 10, 2 )")
        self.assertEqual(
            t,
            {
                "unique": False,
                "pk": False,
                "nullable": True,
                "dtype": "numeric( 10, 2 )",
            },
        )

        t = catalogs.Col.extract_column_from_dtype(
            "varchar( 100 ) not null default 'Empty' check( <name> <> 'test' )"
        )
        self.assertDictEqual(
            t,
            {
                "unique": False,
                "pk": False,
                "nullable": False,
                "check": "check( <name> <> 'test' )",
                "dtype": "varchar( 100 )",
                "default": "'Empty'",
            },
        )

        t = catalogs.Col.extract_column_from_dtype("serial primary key")
        self.assertDictEqual(
            t,
            {
                "unique": False,
                "pk": True,
                "nullable": False,
                "dtype": "integer",
                "default": "nextval('tablename_colname_seq')",
            },
        )

        t = catalogs.Col.extract_column_from_dtype("integer null default 1")
        self.assertDictEqual(
            t,
            {
                "unique": False,
                "pk": False,
                "nullable": True,
                "dtype": "integer",
                "default": "1",
            },
        )
