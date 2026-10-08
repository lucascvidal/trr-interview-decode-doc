"""Decode an ASCII-art message hidden in a Google Doc table."""


def decode_message(url: str) -> None:
    """Fetch `url`, parse (x, character, y) rows, print the grid to stdout."""
    # TODO: implement
    raise NotImplementedError("Implement decode_message")


if __name__ == "__main__":
    SAMPLE_URL = (
        "https://docs.google.com/document/d/"
        "15yp-KodWl3xiW4d6bnDk0e-Ci2Q65QXUqcnUpk7ybog/export?format=html"
    )
    decode_message(SAMPLE_URL)
