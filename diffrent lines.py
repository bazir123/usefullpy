with open("a.txt", "r", encoding="utf-8") as f:
    a_lines = f.readlines()
with open("b.txt", "r", encoding="utf-8") as f:
    b_lines = {line.strip().lower() for line in f}
missing_lines = [
