import datetime
""" importing date and time """
def getDate():
    now= datetime.datetime.now().replace(microsecond=0)
    return str(now.date())

def getTime():
    now= datetime.datetime.now().replace(microsecond=0)
    return str(now.time())
