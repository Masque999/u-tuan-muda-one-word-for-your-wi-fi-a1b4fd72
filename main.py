# One word for my Wi-Fi: it vanishes mid-call, mid-download, mid-sentence —
# present one moment, gone the next, never with an explanation.
LINE = "Ghosting"

# The entry must be a single word.
assert len(LINE) >= 1, "word must not be empty"
assert LINE == LINE.strip(), "word must not have leading or trailing whitespace"
assert " " not in LINE and "\n" not in LINE and "\t" not in LINE, "entry must be a single word"
assert LINE.isalpha(), "entry must be a single alphabetic word"

import os

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not ship an empty file.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content does not match LINE"
