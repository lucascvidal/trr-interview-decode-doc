"""Decode an ASCII-art message hidden in a Google Doc table."""


def decode_message(url: str) -> None:
    """Fetch `url`, parse (x, character, y) rows, print the grid to stdout."""
    # TODO: implement
    raise NotImplementedError("Implement decode_message")


if __name__ == "__main__":
    SAMPLE_URL = (
        "https://docs.google.com/document/d/e/2PACX-1vQq0c4tDdEaPjQ8gvokUkfqEVKLlWql5qwrGyuTeYNKIK_90pWznAm1bWSCQ7IHhnDwt8LbdxPHb4IR/pub"
    )
    decode_message(SAMPLE_URL)
