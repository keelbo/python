from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object.strftime("%Y-%m-%d"))
print(dt_object)

# 2018-12-25
# 2018-12-25 09:27:53
