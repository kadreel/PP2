from datetime import datetime

print(f"Microsecondless: {datetime.now().replace(microsecond=0)}")