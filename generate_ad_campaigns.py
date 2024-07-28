import csv
import random
import datetime

def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Campaign performance profiles
campaign_profiles = {
    'CAMP_001': {'performance': 'high', 'trend': 'improving'},
    'CAMP_002': {'performance': 'medium', 'trend': 'stable'},
    'CAMP_003': {'performance': 'low', 'trend': 'declining'},
    'CAMP_004': {'performance': 'high', 'trend': 'stable'},
    'CAMP_005': {'performance': 'medium', 'trend': 'improving'},
    'CAMP_006': {'performance': 'low', 'trend': 'improving'},
    'CAMP_007': {'performance': 'high', 'trend': 'declining'},
    'CAMP_008': {'performance': 'medium', 'trend': 'declining'},
    'CAMP_009': {'performance': 'low', 'trend': 'stable'},
    'CAMP_010': {'performance': 'medium', 'trend': 'stable'},
}

# Platform characteristics
platform_profiles = {
    'Google Ads': {'ctr': 'high', 'conversion_rate': 'medium', 'cost': 'high'},
    'Facebook Ads': {'ctr': 'medium', 'conversion_rate': 'high', 'cost': 'medium'},
    'Instagram Ads': {'ctr': 'high', 'conversion_rate': 'low', 'cost': 'low'},
    'LinkedIn Ads': {'ctr': 'low', 'conversion_rate': 'high', 'cost': 'high'},
}

def generate_metrics(date, campaign_id, platform, base_impressions):
    profile = campaign_profiles[campaign_id]
    platform_profile = platform_profiles[platform]
    
    # Adjust base metrics based on campaign performance
    if profile['performance'] == 'high':
        base_impressions *= random.uniform(1.2, 1.5)
    elif profile['performance'] == 'low':
        base_impressions *= random.uniform(0.6, 0.9)
    
    # Adjust metrics based on platform characteristics
    ctr_factor = {'high': 0.05, 'medium': 0.03, 'low': 0.01}[platform_profile['ctr']]
    conv_factor = {'high': 0.15, 'medium': 0.1, 'low': 0.05}[platform_profile['conversion_rate']]
    cost_factor = {'high': 2, 'medium': 1.5, 'low': 1}[platform_profile['cost']]
    
    impressions = int(base_impressions)
    clicks = int(impressions * ctr_factor * random.uniform(0.8, 1.2))
    conversions = int(clicks * conv_factor * random.uniform(0.8, 1.2))
    spend = clicks * cost_factor * random.uniform(0.5, 1.5)
    
    # Adjust based on trend
    trend_factor = 1
    days_since_start = (date - datetime.date(2023, 1, 1)).days
    if profile['trend'] == 'improving':
        trend_factor = 1 + (days_since_start / 365) * 0.5
    elif profile['trend'] == 'declining':
        trend_factor = 1 - (days_since_start / 365) * 0.3
    
    impressions = int(impressions * trend_factor)
    clicks = int(clicks * trend_factor)
    conversions = int(conversions * trend_factor)
    
    ctr = (clicks / impressions) * 100 if impressions > 0 else 0
    conversion_rate = (conversions / clicks) * 100 if clicks > 0 else 0
    cost_per_click = spend / clicks if clicks > 0 else 0
    cost_per_conversion = spend / conversions if conversions > 0 else 0
    
    return impressions, clicks, conversions, spend, ctr, conversion_rate, cost_per_click, cost_per_conversion

# Generate CSV file
csv_filename = 'ad_campaigns.csv'
csv_headers = [
    'date', 'campaign_id', 'platform', 'impressions', 'clicks', 'conversions',
    'spend', 'ctr', 'conversion_rate', 'cost_per_click', 'cost_per_conversion'
]

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(csv_headers)
    
    for _ in range(10000):
        date = random_date(start_date, end_date)
        campaign_id = random.choice(list(campaign_profiles.keys()))
        platform = random.choice(list(platform_profiles.keys()))
        base_impressions = random.randint(1000, 10000)
        
        metrics = generate_metrics(date, campaign_id, platform, base_impressions)
        row = [date.isoformat(), campaign_id, platform] + list(metrics)
        csvwriter.writerow(row)

print(f"CSV file '{csv_filename}' created with 10000 rows of realistic ad campaign data.")