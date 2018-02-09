import requests
from bs4 import BeautifulSoup as bs
from yeonsonam.models import *

secret_key='a5187dc3fd4c4572a84a6bc3c0888bfc'

detail_url=[]

drama = Drama2.objects.all()

for i in range(len(drama)):
	detail_url.append('http://www.kopis.or.kr/openApi/restful/pblprfr/' +drama[i].key+ '?service=a5187dc3fd4c4572a84a6bc3c0888bfc')
	print(drama[i].id)

for i in range(len(drama)):
	drama2 = Drama2.objects.get(id=i+2)
	drama2.detail_url=detail_url[i]
	drama2.save()
	print(i+2)



for i in range(len(drama)):
	req = requests.get(drama[i].detail_url)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	select = soup.select('mt10id')
	drama2 = Drama2.objects.get(id=i+2)
	drama2.place_id = select[0].text
	drama2.save()
	print('place_id '+str(i+2)+' complete')
	select = soup.select('prfcast')
	drama2.cast = select[0].text
	drama2.save()
	print('cast '+str(i+2)+' complete')
	select = soup.select('prfcrew')
	drama2.crew = select[0].text
	drama2.save()
	print('crew '+str(i+2)+' complete')
	select = soup.select('prfruntime')
	drama2.runtime = select[0].text
	drama2.save()
	print('runtime '+str(i+2)+' complete')
	select = soup.select('prfage')
	drama2.age = select[0].text
	drama2.save()
	print('age '+str(i+2)+' complete')
	select = soup.select('entrpsnm')
	drama2.enterprise = select[0].text
	drama2.save()
	print('enterprise '+str(i+2)+' complete')
	select = soup.select('pcseguidance')
	drama2.price = select[0].text
	drama2.save()
	print('price '+str(i+2)+' complete')







for i in range(len(drama)):
	req = requests.get(drama[i].detail_url)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	select = soup.select('sty')
	drama2 = Drama2.objects.get(id=i+2)
	drama2.summary = select[0].text
	drama2.save()
	select = soup.select('styurl')
	b=[]
	for s in select:
		b.append(s.text)
	drama2.styurl= b
	print(b)
	drama2.save()
	select = soup.select('dtguidance')
	drama2.time = select[0].text
	drama2.save()































