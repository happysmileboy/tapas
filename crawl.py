import requests
from bs4 import BeautifulSoup as bs
from yeonsonam.models import *

secret_key='a5187dc3fd4c4572a84a6bc3c0888bfc'

detail_url=[]

drama = Drama2.objects.all()

for i in range(len(drama)):
	detail_url.append('http://www.kopis.or.kr/openApi/restful/pblprfr/' +drama[i].perf_id+ '?service=a5187dc3fd4c4572a84a6bc3c0888bfc')
	print(drama[i].id)

for i in range(len(drama)):
	drama2 = Drama2.objects.get(id=i+2)
	drama2.detail_url=detail_url[i]
	drama2.save()
	print(i+2)



for i in range(len(drama)):
	req = requests.get(drama[i].detail_url)
	html = req.text
	soup = bs(html, 'html.parser')
	select = soup.select('mt10id')
	drama2 = Drama2.objects.get(id=i+2)
	drama2.place_id = select[0].text
	drama2.save()
	print('place_id '+str(i+2)+' complete')







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




for i in range(len(t)):
	if '대학로' in  t[i].place:
		b = t[i].id
		a = Drama2.objects.get(id=b)
		a.tag_places = Tag_places.objects.get(id=1)
		a.save()


























