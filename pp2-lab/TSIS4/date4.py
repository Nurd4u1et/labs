import datetime
def differens(tom, tod):
    diff = tom - tod
    return diff.total_seconds()
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
res = differens(tomorrow,today)
print(res)