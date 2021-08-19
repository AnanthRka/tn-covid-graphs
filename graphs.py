from datetime import  datetime,date, timedelta

now = datetime.now()
hour = datetime.time(now).hour
minute = datetime.time(now).minute

today_date = datetime.strftime(now, '%d-%m-%y')
if hour <20 and minute >=30:
    today_date = datetime.strftime(now -timedelta(1), '%d-%m-%y' )
print (today_date)
url = 'https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-'+ today_date + '-COVID-19.pdf'
