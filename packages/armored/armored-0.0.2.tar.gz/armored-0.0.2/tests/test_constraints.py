import unittest

import armored.constraints as const


class TestPrimaryKey(unittest.TestCase):
    def test_pk_init(self):
        t = const.Pk(of="foo")
        self.assertEqual("foo", t.of)
        self.assertListEqual([], t.cols)

        t = const.Pk(of="foo", cols=["col1"])
        self.assertEqual("foo_col1_pk", t.name)
        self.assertListEqual(["col1"], t.cols)

        t = const.Pk(of="foo", cols=["col1", "col2"])
        self.assertEqual("foo_col1_col2_pk", t.name)
        self.assertListEqual(["col1", "col2"], t.cols)

    def test_pk_model_validate(self):
        t = const.Pk.model_validate(
            {
                "of": "foo",
                "cols": ["col1"],
            }
        )
        self.assertEqual("foo", t.of)
        self.assertListEqual(["col1"], t.cols)
        self.assertEqual("foo_col1_pk", t.name)


class TestReference(unittest.TestCase):
    def test_ref_init(self):
        t = const.Ref(tbl="foo", col="bar")
        self.assertEqual("foo", t.tbl)
        self.assertEqual("bar", t.col)


class TestForeignKey(unittest.TestCase):
    def test_fk_init(self):
        t = const.Fk(
            of="foo",
            to="test",
            ref=const.Ref(tbl="bar", col="baz"),
        )
        self.assertEqual("foo", t.of)
        self.assertEqual("test", t.to)
        self.assertEqual("bar", t.ref.tbl)
        self.assertEqual("baz", t.ref.col)
        self.assertEqual("foo_test_bar_baz_fk", t.name)

    def test_fk_model_validate(self):
        t = const.Fk.model_validate(
            {
                "of": "foo",
                "to": "test",
                "ref": {
                    "tbl": "bar",
                    "col": "baz",
                },
            }
        )
        self.assertEqual("foo", t.of)
        self.assertEqual("test", t.to)
        self.assertEqual("bar", t.ref.tbl)
        self.assertEqual("baz", t.ref.col)
        self.assertEqual("foo_test_bar_baz_fk", t.name)
