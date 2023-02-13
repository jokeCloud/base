# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# docs:
# https://dateutil.readthedocs.com.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 09:30:30', fmt)
delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
print(data_fim - delta)
print(data_fim + relativedelta(seconds=60, minutes=10))
