import sqlite3
import random
import datetime

# Create a connection to the SQLite database
conn = sqlite3.connect('ad_campaigns.db')
cursor = conn.cursor()

# Create the ad_campaigns table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ad_campaigns (
    id INTEGER PRIMARY KEY,
    date TEXT,
    campaign_id TEXT,
    platform TEXT,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER,
    spend REAL,
    ctr REAL,
    conversion_rate REAL,
    cost_per_click REAL,
    cost_per_conversion REAL
)
''')

# Function to generate a random date
def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Generate mock data
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
campaign_ids = [f'CAMP_{i:03d}' for i in range(1, 11)]
platforms = ['Google Ads', 'Facebook Ads', 'Instagram Ads', 'LinkedIn Ads']

# Insert 10,000 rows of mock data
for _ in range(10000):
    date = random_date(start_date, end_date)
    campaign_id = random.choice(campaign_ids)
    platform = random.choice(platforms)
    impressions = random.randint(1000, 100000)
    clicks = random.randint(10, 1000)
    conversions = random.randint(0, 50)
    spend = round(random.uniform(50, 1000), 2)
    
    ctr = round((clicks / impressions) * 100, 2)
    conversion_rate = round((conversions / clicks) * 100, 2) if clicks > 0 else 0
    cost_per_click = round(spend / clicks, 2) if clicks > 0 else 0
    cost_per_conversion = round(spend / conversions, 2) if conversions > 0 else None

    cursor.execute('''
    INSERT INTO ad_campaigns (date, campaign_id, platform, impressions, clicks, conversions, spend, ctr, conversion_rate, cost_per_click, cost_per_conversion)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (date.isoformat(), campaign_id, platform, impressions, clicks, conversions, spend, ctr, conversion_rate, cost_per_click, cost_per_conversion))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'ad_campaigns.db' created with 10,000 rows of mock data.")