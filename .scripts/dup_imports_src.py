import pathlib, re, collections, sys
p = pathlib.Path('src').resolve()
c = collections.Counter()
for f in p.rglob('*.py'):
    try:
        text = f.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    for line in text.splitlines():
        m = re.match(r"^\s*(from\s+\S+\s+import\s+[\S, ]+|import\s+\S+)", line)
        if m:
            c[m.group(1).strip()] += 1
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    if v > 1:
        print(v, '|', k)
