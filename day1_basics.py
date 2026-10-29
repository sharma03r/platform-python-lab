clusters = {
    "prod-noida-1": "4.18",
    "prod-noida-2": "4.20",
    "dev-1": "4.18",
}

for c,k in clusters.items():
  print(f"{c}: {k}")