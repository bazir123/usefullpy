import os
input_file = "input.txt"
lines_per_file = 500
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
total_lines = len(lines)
file_count = (total_lines + lines_per_file - 1) // lines_per_file
