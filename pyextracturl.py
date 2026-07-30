import re
INPUT_FILE = "input.txt"
OUTPUT_FILE = "domains.txt"
# Matches:
# https://domain...
# http://domain...
# or plain domains
pattern = re.compile(
    r'((?:https?://)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})(?:[/?#:][^\s"\'>]*)?',
    re.IGNORECASE
)
seen = set()
with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as fin, \
     open(OUTPUT_FILE, "w", encoding="utf-8") as fout:

    for line in fin:
        for match in pattern.finditer(line):
