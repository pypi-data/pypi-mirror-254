import datetime
import unittest
from unittest import mock
from zoneinfo import ZoneInfo

import armored.lineages as lineages
import armored.settings as st


class TestTS(unittest.TestCase):
    @mock.patch("armored.lineages.datetime", wraps=datetime.datetime)
    def test_ts_init(self, mock_datetime):
        mock_datetime.utcnow.return_value = datetime.datetime(
            2023, 1, 1, 0, 0, 0
        )
        t = lineages.TS()
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "ts": datetime.datetime(2023, 1, 1, 0, 0, 0).astimezone(
                    tz=ZoneInfo(st.TSSetting.tz)
                ),
                "tz": "Asia/Bangkok",
            },
        )


class TestTag(unittest.TestCase):
    @mock.patch("armored.lineages.date", wraps=datetime.date)
    @mock.patch("armored.lineages.datetime", wraps=datetime.datetime)
    def test_tag_init(self, mock_datetime, mock_date):
        mock_date.return_value = datetime.date(2023, 1, 1)
        mock_datetime.utcnow.return_value = datetime.datetime(
            2023, 1, 1, 0, 0, 0
        )
        t = lineages.Tag()
        self.assertDictEqual(
            t.model_dump(by_alias=False),
            {
                "author": "undefined",
                "desc": None,
                "labels": [],
                "ts": datetime.datetime(2023, 1, 1, 0, 0, 0).astimezone(
                    tz=ZoneInfo(st.TSSetting.tz)
                ),
                "vs": datetime.date(2023, 1, 1),
                "tz": "Asia/Bangkok",
            },
        )
