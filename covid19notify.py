import COVID19Py as cp
import win10toast
from pynotifier import Notification

covid19 = cp.COVID19(data_source = 'jhu')
latest = covid19.getLatest()

Notification(
            title = 'Today COVID19 cases News Updates ',
            description = str(latest),
            duration = 30
            ).send()
