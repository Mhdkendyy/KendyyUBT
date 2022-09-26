from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL0NpbGlrUHJvamVjdC9CaW9uLVB5cm9Cb3Q=").decode("utf-8"),
)
