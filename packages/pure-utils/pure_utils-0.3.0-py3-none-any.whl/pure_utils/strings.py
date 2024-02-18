"""Utilities for working with strings."""

from random import choices
from string import ascii_lowercase, ascii_uppercase
from zlib import compress, decompress

__all__ = ["genstr", "gzip", "gunzip"]


def genstr(length: int = 10, /, *, is_uppercase: bool = False) -> str:
    """Generate ASCII-string with random letters.

    Args:
        length: The length of generated string.
        is_uppercase: If enable, generate string in uppercase.

    Returns:
        Generated ASCII-string with random letters.

    Usage:

    .. code-block:: python

        from pure_utils import genstr

        dummy = genstr(20)
        print(dummy)  # otvqydcprjtpcuboumbs

        dummy = genstr(20, is_uppercase=True)
        print(dummy)  # POXDVZCMDWXBPVVRXWHN
    """
    string_generator = ascii_uppercase if is_uppercase else ascii_lowercase
    return "".join(choices(string_generator, k=length))


def gzip(string: str | bytes, /, *, level: int = 9) -> bytes:
    """Compress string (or bytes string) with gzip compression level.

    Args:
        string: Source (uncompressed) string.
        level: Compression level (numbers from 1 to 9) (default: 9).
               1 - fastest compression but big result size;
               9 - slowest compression but small result size (max compression).

    Returns:
        Compressed string in bytes.

    Usage:

    .. code-block:: python

        from pure_utils import gzip

        big_string = "abc" * 100500
        print(len(big_string))  # 301500

        compressed_string = gzip(big_string)
        print(len(compressed_string))  # 319
    """
    return compress(string if isinstance(string, bytes) else string.encode(), level=level)


def gunzip(compressed_string: bytes, /) -> str:
    """Decompress bytes (earlier compressed with gzip) to string.

    Args:
        compressed_string: Bytes for decompression to string.

    Returns:
        Decompressed string from bytes.

    Usage:

    .. code-block:: python

        from pure_utils import gzip, gunzip

        compressed_string = gzip("sample string")

        print(gunzip(compressed_string))  # sample string
    """
    return decompress(compressed_string).decode()
