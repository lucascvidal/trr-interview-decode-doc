# Interview prompt — decode a hidden message (25 minutes)

You are given a **Google Doc** URL. The document contains a table of ASCII characters and their `(x, y)` coordinates. Your job is to fetch that document, place each character on a 2D grid, and **print the grid to stdout** so the ASCII-art message `TheRealReal` appears.

## Time box

**25 minutes.** Aim for a correct happy-path solution and clear reasoning. You do not need production-grade error handling, tests, or support for multiple URL formats.

## Language & libraries

- **Python preferred.** If you want another language, ask the interviewer first.
- You may use the Python standard library plus **`requests`** and **`BeautifulSoup`** (already listed in `requirements.txt` / Codespaces).

## Data shape

The Google Doc’s exported HTML includes a table. After the header row, each data row has three cells, in this order:

| x-coordinate | Character | y-coordinate |
|-------------:|:---------:|-------------:|
| 0            | #         | 0            |
| 1            | #         | 0            |
| …            | …         | …            |

- `x` and `y` are non-negative integers.
- `Character` is typically `#`, or a space.
- Positions not listed in the table should be treated as **spaces**.
- Print **one row per line**, joining characters left-to-right. Use `y` as the row index and `x` as the column index (`grid[y][x]`). Print rows from `y = 0` through `y = max_y`.

## Sample Google Doc (live exercise)

```
https://docs.google.com/document/d/15yp-KodWl3xiW4d6bnDk0e-Ci2Q65QXUqcnUpk7ybog/export?format=html
```

This is the HTML export of a Google Doc containing the table above. Fetch it with `requests` and parse the table.

## What to implement

Complete `decode_message(url: str) -> None` in `decode.py` so that running:

```bash
python3 decode.py
```

fetches the sample URL, builds the grid, and prints the message to stdout.

## Success criteria

1. Correct printed message for the sample document (happy path).
2. You can explain your fetch → parse → grid → print approach.

## Out of scope for 25 minutes

- Auth, databases, web UI, Docker
- Supporting both the shared document URL and export URL forms
- Exhaustive error handling or a full test suite

If time remains, the interviewer may ask about edge cases (malformed rows, empty document, network failure).
