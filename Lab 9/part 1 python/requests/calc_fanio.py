import json
from collections import defaultdict

with open('requests/deps.json') as f:
    deps = json.load(f)

fan_in  = defaultdict(int)
fan_out = defaultdict(int)

for module, info in deps.items():
    # out‑degree = number of imports
    fan_out[module] = len(info.get('imports', []))
    # in‑degree: count each 'imported_by'
    for importer in info.get('imported_by', []):
        fan_in[module] += 1

print(f"{'Module':40s} {'Fan‑In':>6s} {'Fan‑Out':>7s}")
print("-"*55)
for m in sorted(deps):
    print(f"{m:40s} {fan_in[m]:6d} {fan_out[m]:7d}")
