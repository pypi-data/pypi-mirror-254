from datetime import datetime
from sys import version_info

import pytest
from dt import apply_tz, iso2dmy, iso2format, iso2ymd, round_by


class TestApplyTz:
    @pytest.fixture(scope="function")
    def now(self):
        return datetime.now()

    def test_with_defaults(self, now):
        result = apply_tz(now)
        assert result
        assert isinstance(result, datetime)
        assert str(result.tzinfo) == "UTC"

    def test_with_custom_timezone(self, now):
        result = apply_tz(now, "Europe/Moscow")
        assert result
        assert isinstance(result, datetime)
        assert str(result.tzinfo) == "Europe/Moscow"


class TestIso2Dmy:
    @pytest.mark.skipif(version_info < (3, 11), reason="requires python3.11 or higher")
    @pytest.mark.parametrize(
        "iso_datetime, expected",
        [
            ("20050809", "09.08.2005"),
            ("20060809T183142", "09.08.2006"),
            ("2007-08-09T18:31:42", "09.08.2007"),
            ("20080809T183142+03", "09.08.2008"),
            ("2009-08-09T18:31:42+03", "09.08.2009"),
            ("20100809T183142-0330", "09.08.2010"),
            ("2011-08-09T18:31:42-03:30", "09.08.2011"),
        ],
    )
    def test_with_iso_datetime_string(self, iso_datetime, expected):
        formatted_dt = iso2dmy(iso_datetime)
        assert formatted_dt
        assert isinstance(formatted_dt, str)
        assert formatted_dt == expected


class TestIso2Ymd:
    @pytest.mark.skipif(version_info < (3, 11), reason="requires python3.11 or higher")
    @pytest.mark.parametrize(
        "iso_datetime, expected",
        [
            ("20050809", "2005-08-09"),
            ("20060809T183142", "2006-08-09"),
            ("2007-08-09T18:31:42", "2007-08-09"),
            ("20080809T183142+03", "2008-08-09"),
            ("2009-08-09T18:31:42+03", "2009-08-09"),
            ("20100809T183142-0330", "2010-08-09"),
            ("2011-08-09T18:31:42-03:30", "2011-08-09"),
        ],
    )
    def test_with_iso_datetime_string(self, iso_datetime, expected):
        formatted_dt = iso2ymd(iso_datetime)
        assert formatted_dt
        assert isinstance(formatted_dt, str)
        assert formatted_dt == expected


class TestIso2Format:
    @pytest.mark.skipif(version_info < (3, 11), reason="requires python3.11 or higher")
    @pytest.mark.parametrize(
        "iso_datetime, fmt, expected",
        [
            ("20050809", "%Y-%m-%d", "2005-08-09"),
            ("20060809T183142", "%Y-%m-%d %H:%M:%S", "2006-08-09 18:31:42"),
            ("2009-08-09T18:31:42+03", "%d.%m.%Y %H:%M:%S", "09.08.2009 18:31:42"),
        ],
    )
    def test_with_iso_datetime_string(self, iso_datetime, fmt, expected):
        formatted_dt = iso2format(iso_datetime, fmt)
        assert formatted_dt
        assert isinstance(formatted_dt, str)
        assert formatted_dt == expected


class TestRoundBy:
    @pytest.fixture(scope="function")
    def dt(self):
        return datetime.fromisoformat("2024-01-01 10:11:12.472482")

    def test_round_by_day(self, dt):
        rounded_datetime = round_by(dt, boundary="day")
        assert rounded_datetime
        assert isinstance(rounded_datetime, datetime)
        assert str(rounded_datetime) == "2024-01-01 00:00:00"

    def test_round_by_hour(self, dt):
        rounded_datetime = round_by(dt, boundary="hour")
        assert rounded_datetime
        assert isinstance(rounded_datetime, datetime)
        assert str(rounded_datetime) == "2024-01-01 10:00:00"

    def test_round_by_minute(self, dt):
        rounded_datetime = round_by(dt, boundary="minute")
        assert rounded_datetime
        assert isinstance(rounded_datetime, datetime)
        assert str(rounded_datetime) == "2024-01-01 10:11:00"

    def test_round_by_second(self, dt):
        rounded_datetime = round_by(dt, boundary="second")
        assert rounded_datetime
        assert isinstance(rounded_datetime, datetime)
        assert str(rounded_datetime) == "2024-01-01 10:11:12"

    def test_raise_value_error(self, dt):
        with pytest.raises(ValueError) as excinfo:
            round_by(dt, boundary="microsecond")
            assert excinfo.value.message == (
                "Invalid boundary value (microsecond). "
                "Available only: [day, hour, minute, second]."
            )
