from datetime import datetime, timedelta

print(f"Yesterday: {(datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y')}")
print(f"Today: {datetime.now().strftime('%d.%m.%Y')}")
print(f"Tomorrow: {(datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')}")