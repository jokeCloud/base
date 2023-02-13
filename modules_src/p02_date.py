# criando datas com módulo datetime
# datetime(ano, mês, ano)
# datetime(ano, mês, ano, horas, minutos, segundos)
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

from pytz import timezone

time_zone_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(time_zone_tokyo)

unix_count = datetime.now()
print(unix_count.timestamp())

data = datetime(2023, 2, 13)
print(data)

data_str = '2023-02-13 11:44:22'
data_str_br = '13/02/2023'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data_str_fmt_br = '%d/%m/%Y'

hora = datetime(2023, 2, 13, 11, 42, 23)
print(hora)


data = datetime.strptime(data_str, data_str_fmt)
print(data)

dia = datetime.strptime(data_str_br, data_str_fmt_br)
print(dia)


horario = datetime.now()
print(f'horario: {horario.timestamp()}')
print(f'{datetime.fromtimestamp(horario.timestamp())}')
