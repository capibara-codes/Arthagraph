import pandas as pd
import os

# Create a data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Ancient IKS Trade Nodes (The History)
# These represent ancient ports and market towns in Maharashtra
ancient_sites = [
    {"site_id": "A1", "name": "Sopara", "type": "Port", "commodity": "Gold, Glass", "lat": 19.41, "lon": 72.81, "period": "Satavahana"},
    {"site_id": "A2", "name": "Kalyan", "type": "Port", "commodity": "Textiles", "lat": 19.24, "lon": 73.13, "period": "Satavahana"},
    {"site_id": "A3", "name": "Paithan", "type": "Capital", "commodity": "Paithani Silk", "lat": 19.47, "lon": 75.38, "period": "Satavahana"},
    {"site_id": "A4", "name": "Junnar", "type": "Trade Hub", "commodity": "Agricultural", "lat": 19.21, "lon": 73.87, "period": "Satavahana"},
    {"site_id": "A5", "name": "Ter", "type": "Market Town", "commodity": "Ivory", "lat": 18.31, "lon": 76.14, "period": "Satavahana"}
]

# 2. Modern FinTech Nodes (The Present)
# These represent modern financial districts or tech hubs
modern_hubs = [
    {"hub_id": "M1", "name": "BKC Mumbai", "specialty": "Investment Banking", "lat": 19.06, "lon": 72.86},
    {"hub_id": "M2", "name": "Hinjewadi Pune", "specialty": "Digital Payments", "lat": 18.59, "lon": 73.73},
    {"hub_id": "M3", "name": "Magarpatta City", "specialty": "FinTech SaaS", "lat": 18.51, "lon": 73.93},
    {"hub_id": "M4", "name": "GIFT City", "specialty": "International Exchange", "lat": 23.16, "lon": 72.68}
]

# Convert to DataFrames
df_ancient = pd.DataFrame(ancient_sites)
df_modern = pd.DataFrame(modern_hubs)

# Save to CSV
df_ancient.to_csv('data/ancient_sites.csv', index=False)
df_modern.to_csv('data/modern_hubs.csv', index=False)

print("✅ Success! Created data/ancient_sites.csv and data/modern_hubs.csv")
print("🚀 You are ready for the next commit.")