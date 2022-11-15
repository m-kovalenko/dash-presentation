from datetime import datetime
from random import random

import pandas as pd

rows = []
counter = 0
for d in range(11):
    rows.extend([(counter := counter + random(), datetime(2022, 11, d+6, h)) for h in range(24)])


df = pd.DataFrame(data=rows, columns=['value', 'datetime'])
df.to_csv('beautiful_data.csv', index=False)
