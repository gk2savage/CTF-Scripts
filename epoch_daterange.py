import time
import pandas as pd
from datetime import datetime
from_date = 1656672238000
to_date = 1659350638000

from_date_converted = time.strftime("%d %b %Y", time.localtime(from_date / 1000))
to_date_converted = time.strftime("%d %b %Y", time.localtime(to_date / 1000))
fullDateRange = pd.date_range(start=from_date_converted, end=to_date_converted).strftime('%d %b %Y').tolist()
print("fullDateRange", fullDateRange)
