from datetime import datetime, timedelta

print((datetime.now() - timedelta(days=5)).strftime('%d.%m.%Y'))