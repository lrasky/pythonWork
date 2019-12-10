import re
import requests

class Handle_lagou:
    def __init__(self):
        self.session = requests.session()
        self.header = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.97Safari / 537.36'
        }
        self.city_list = ''
    def handle_city(self):
        city_search = re.compile(r'zhaioub/"(.*?)</a>')
        city_url = 'https://www.lagou.com/jobs/allCity.html'
        city_result = self.handle_request(url= city_url, method= 'GET')
        self.city_list = city_search.findall(city_result)

    def handle_request(self,method,url,data= None, info= None):
        if method == 'GET':
            requests.packages.urllib3.disable_warnings()
            response = self.session.get(url= url, headers= self.header,verify=False)
            return response.text

if __name__ == '__main__':
    lagou = Handle_lagou()
    lagou.handle_city()
    print(lagou.city_list)
    ' '.replace