from datetime import datetime

date1 = datetime(2025, 2, 21, 12, 0, 0)
date2 = datetime(2025, 2, 20, 10, 30, 0)

difference = (date1 - date2).total_seconds()

print(f"Difference in seconds: {difference}")
