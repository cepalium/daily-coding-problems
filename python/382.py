# --------------------------
# Author: Tuan Nguyen
# Date created: 20200613
#!382.py
# --------------------------
"""
Write a function to decode a Base64 string back to a hexadecimal string.

For example, the following string:
3q2+7w==

should produce:
deadbeef
"""


def base64_string_to_hex_string(base64_string):
    import base64

    byte = base64.b64decode(base64_string)
    hex_string = byte.hex()
    return hex_string


def test1():
    assert base64_string_to_hex_string("3q2+7w==") == "deadbeef"


if __name__ == "__main__":
    test1()
