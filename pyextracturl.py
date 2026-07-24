import re
INPUT_FILE = "input.txt"
OUTPUT_FILE = "domains.txt"
# Matches:
# https://domain...
# http://domain...
# or plain domains
pattern = re.compile(
    r'((?:https?://)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})(?:[/?#:][^\s"\'>]*)?',
