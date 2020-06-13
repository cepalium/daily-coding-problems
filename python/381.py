# --------------------------
# Author: Tuan Nguyen
# Date created: 20200613
#!381.py
# --------------------------
"""
Implement a function that converts a hex string to base64.

For example, the string:
deadbeef

should produce:
3q2+7w==
"""
def hex_string_to_base64_string(hex_string):
    import base64
    byte = bytes.fromhex(hex_string)
    base64_encoded = base64.b64encode(byte)
    base64_string = base64_encoded.decode("utf-8")
    return base64_string


def test1():
    assert hex_string_to_base64_string("deadbeef") == "3q2+7w=="

if __name__ == "__main__":
    test1()