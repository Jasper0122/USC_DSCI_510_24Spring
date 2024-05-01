import requests
import re

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',

}
sess=requests.session()
a=sess.get(url='https://www.neighborhoodatlas.medicine.wisc.edu/login',headers=headers)
pp=re.findall('value="(.*?)"',a.text)
cref=pp[0]
data = {
  '_csrf': cref,
  'email': 'zongrong@usc.edu',
  'password': 'Lz13988966266'
}
#
response = sess.post('https://www.neighborhoodatlas.medicine.wisc.edu/login', headers=headers, data=data)
print(response.status_code)
url1='https://www.neighborhoodatlas.medicine.wisc.edu/download'
response1=sess.get(url=url1,headers=headers)
pp1=re.findall('value="(.*?)"',response1.text)

data = {
  'state-type': 'blockgroup',
  '_csrf': pp1[0],
  'scale-group': 'state', # state - Single State; national - All States
  'state-name': 'CA', # CA - California
  'version-group': '20' # 20 - 2020
}

response2 = sess.post('https://www.neighborhoodatlas.medicine.wisc.edu/adi-download', headers=headers, data=data)
# if success
if response2.status_code == 200:
    # writing response to zip file
    with open('adi-download.zip', 'wb') as zip_file:
        zip_file.write(response2.content)
    print("Successfully save File as adi-download.zip")
else:
    print("Reponse Error, Status Code:", response2.status_code)