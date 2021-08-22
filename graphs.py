from datetime import  datetime, timedelta
import urllib.request
import os

now = datetime.now()
hour = datetime.time(now).hour
minute = datetime.time(now).minute

today_date = datetime.strftime(now, '%d-%m-%y')
if hour <20 or minute <=30:
    today_date = datetime.strftime(now -timedelta(1), '%d-%m-%y' )

url = 'https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-'+ today_date + '-COVID-19.pdf'

if not os.path.exists(os.path.abspath(os.getcwd()) + f'\{today_date}.pdf'):
    urllib.request.urlretrieve(url, filename=f'{today_date}.pdf')
else:
    print('No new file has been uploaded')

