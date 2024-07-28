import csv
import random
import datetime

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

# Prepare CSV file
csv_filename = 'ad_campaigns.csv'
csv_headers = [
    'date', 'campaign_id', 'platform', 'impressions', 'clicks', 'conversions',
    'spend', 'ctr', 'conversion_rate', 'cost_per_click', 'cost_per_conversion'
]

with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csv_headers)

    # Generate and write 10000 rows of mock data
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

        row = [
            date.isoformat(), campaign_id, platform, impressions, clicks, conversions,
            spend, ctr, conversion_rate, cost_per_click, cost_per_conversion
        ]
        csvwriter.writerow(row)

print(f"CSV file '{csv_filename}' created with 10000 rows of mock data.")