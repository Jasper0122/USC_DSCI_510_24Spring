# import module
import requests

# set cookies and headers
cookies = {
    '_ga': 'GA1.1.1236962577.1714036482',
    'uw_madison_cookieconsent_timestamp': '1714036490',
    'uw_madison_cookieconsent_url': 'https://www.neighborhoodatlas.medicine.wisc.edu/login',
    'sess': 's%3AooA5poYz7XtyeroOYROCaAhga9In6xct.mJbAsDH%2Fksm87wiDTgvvPILEZ1cJhafDP7zHBLZ65Z0',
    '_ga_XHQBYHWBMP': 'GS1.1.1714036481.1.1.1714036631.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.neighborhoodatlas.medicine.wisc.edu',
    'Referer': 'https://www.neighborhoodatlas.medicine.wisc.edu/download',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# set requests params
data = {
  'state-type': 'blockgroup',
  '_csrf': 'oFfaGwS0-JItOW6huirExQS8mxSw_nBeESJg',
  'scale-group': 'state', # state - Single State; national - All States
  'state-name': 'CA', # CA - California
  'version-group': '20' # 20 - 2020
}

response = requests.post('https://www.neighborhoodatlas.medicine.wisc.edu/adi-download', headers=headers, cookies=cookies, data=data)
# if success
if response.status_code == 200:
    # writing response to zip file
    with open('adi-download.zip', 'wb') as zip_file:
        zip_file.write(response.content)
    print("Successfully save File as adi-download.zip")
else:
    print("Reponse Error, Status Code:", response.status_code)