from collections import namedtuple
import datetime

now = datetime.datetime.now()
yesterday1 = now - datetime.timedelta(days=1)
twodaysago = yesterday1 - datetime.timedelta(days=1)
onehourago = datetime.datetime.now() - datetime.timedelta(hours=1)

print(now)
print(onehourago)