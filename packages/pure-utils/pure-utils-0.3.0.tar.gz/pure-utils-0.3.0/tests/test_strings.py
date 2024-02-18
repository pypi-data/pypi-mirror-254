import pytest
from strings import genstr, gunzip, gzip


class TestGenstr:
    def test_with_default_params(self):
        random_string = genstr()

        assert random_string
        assert len(random_string) == 10
        # String generated in lowercase, by default.
        assert random_string == random_string.lower()

    def test_with_custom_length(self):
        random_string = genstr(5)
        assert len(random_string) == 5

    def test_with_is_uppercase(self):
        random_string = genstr(is_uppercase=True)
        assert random_string == random_string.upper()


class TestGzip:
    @pytest.fixture(scope="function")
    def string(self):
        return "test string"

    @pytest.fixture(scope="function")
    def string_in_bytes(self, string):
        return string.encode()

    @pytest.fixture(scope="function")
    def compressed_string(self):
        return b"x\xda+I-.Q(.)\xca\xccK\x07\x00\x1a\xc0\x04x"

    def test_on_string(self, mocker, string, string_in_bytes, compressed_string):
        compress_mock = mocker.patch("strings.compress", return_value=compressed_string)

        result = gzip(string)

        assert result
        assert isinstance(result, bytes)
        compress_mock.assert_called_once_with(string_in_bytes, level=9)

    def test_on_bytes(self, mocker, string_in_bytes, compressed_string):
        compress_mock = mocker.patch("strings.compress", return_value=compressed_string)

        result = gzip(string_in_bytes)

        assert result
        assert isinstance(result, bytes)
        compress_mock.assert_called_once_with(string_in_bytes, level=9)

    def test_on_string_with_custom_compress_level(
        self, mocker, string, string_in_bytes, compressed_string
    ):
        compress_mock = mocker.patch("strings.compress", return_value=compressed_string)

        result = gzip(string, level=5)

        assert result
        assert isinstance(result, bytes)
        compress_mock.assert_called_once_with(string_in_bytes, level=5)


class TestGunzip:
    @pytest.fixture(scope="function")
    def string(self):
        return "test string"

    @pytest.fixture(scope="function")
    def string_in_bytes(self, string):
        return string.encode()

    @pytest.fixture(scope="function")
    def compressed_string(self):
        return b"x\xda+I-.Q(.)\xca\xccK\x07\x00\x1a\xc0\x04x"

    def test_on_compressed_string(self, mocker, string, string_in_bytes, compressed_string):
        decompress_mock = mocker.patch("strings.decompress", return_value=string_in_bytes)

        result = gunzip(compressed_string)

        assert result
        assert isinstance(result, str)
        decompress_mock.assert_called_once_with(compressed_string)
