import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ad_campaigns.db')
cursor = conn.cursor()

# Query 1: Count total rows
cursor.execute("SELECT COUNT(*) FROM ad_campaigns")
total_rows = cursor.fetchone()[0]
print(f"Total rows in the database: {total_rows}")

# Query 2: Get average CTR by platform
cursor.execute("""
SELECT platform, AVG(ctr) as avg_ctr 
FROM ad_campaigns 
GROUP BY platform
""")
platform_ctr = cursor.fetchall()
print("\nAverage CTR by platform:")
for platform, avg_ctr in platform_ctr:
    print(f"{platform}: {avg_ctr:.2f}%")

# Query 3: Get top 5 campaigns by spend
cursor.execute("""
SELECT campaign_id, SUM(spend) as total_spend
FROM ad_campaigns
GROUP BY campaign_id
ORDER BY total_spend DESC
LIMIT 5
""")
top_campaigns = cursor.fetchall()
print("\nTop 5 campaigns by spend:")
for campaign, spend in top_campaigns:
    print(f"{campaign}: ${spend:.2f}")

# Close the connection
conn.close()