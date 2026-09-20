from pathlib import Path
import re,sys
BAD=[re.compile(r'Bearer\s+[A-Za-z0-9._-]{16,}',re.I),re.compile(r'-----BEGIN .*PRIVATE KEY-----'),re.compile(r'\b[^\s@]+@[^\s@]+\.[^\s@]+\b')]
root=Path(sys.argv[1] if len(sys.argv)>1 else '.'); bad=[]
for p in root.rglob('*.log'):
    txt=p.read_text(encoding='utf-8',errors='ignore')
    if any(x.search(txt) for x in BAD): bad.append(str(p))
print('PASS' if not bad else 'FAIL'); [print(' -',x) for x in bad]
raise SystemExit(bool(bad))
