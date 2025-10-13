import json, os, urllib.request

URL = "https://api.exchange.coinbase.com/products"
OUT = os.path.join(os.getcwd(), "public", "pairs.json")

print("Fetching Coinbase products...")
with urllib.request.urlopen(URL) as r:
    data = json.loads(r.read().decode())

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"✅ Wrote {len(data)} total pairs to {OUT}")
