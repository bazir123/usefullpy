with open("a.txt", "r", encoding="utf-8") as f:
    a_lines = f.readlines()
with open("b.txt", "r", encoding="utf-8") as f:
    b_lines = {line.strip().lower() for line in f}
missing_lines = [
    line for line in a_lines
    if line.strip().lower() not in b_lines
with open("c.txt", "w", encoding="utf-8") as f:
