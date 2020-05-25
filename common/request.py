import requests,os,logging
from common.oppymysql import Open_mysql
from websocket import create_connection
import os

class test_Interface(object):
    def __init__(self,url_root):
        self.url_root= url_root
        self.websocket_status = False

    def __del__(self):
        if self.websocket_status==True:
            self.ws.close()

    def default_headers(self):
        self.headers = {'Referer':self.url_root}
        return self.headers

    def web_api(self,method,url,data_OR_param,headers=None):

        lowermethod=method.lower()

        if headers==None:
            headers=self.default_headers()

        if lowermethod == 'post':
            d=self.http_post(url=url,data=data_OR_param,headers=headers)

        elif lowermethod == 'get':
            d=self.http_get(url=url,param=data_OR_param,headers=headers)

        elif lowermethod == 'ws':
            self.websocket_status = True
            url_root=self.url_root
            d=self.websocket_send(url_root=url_root,param=data_OR_param)

        else:
            print("无对应接口类型："+ method)
        return  d

    def httpResponse_message(self,status_code,text,cookies,headers):
        d={}
        d["status_code"]=status_code
        d["cookies"]=cookies
        a["headers"]=headers
        d["text"] = text
        return d

    def websocket_send(self,url_root,param):
        self.ws = create_connection(url_root)
        self.ws.send(param)
        res = self.ws.recv()
        return res

    def http_post(self,url,data,headers):
        interface_url=self.url_root + url
        a=requests.session().post(url=interface_url,data=data,headers=headers)
        d=self.httpResponse_message(a.status_code,a.text,a.cookies,a.headers)
        return d

    def http_get(self,url,param,headers):
        interface_url= self.url_root + url
        a=requests.get(url=interface_url,data=param,headers=headers)
        d = self.httpResponse_message(a.status_code, a.text, a.cookies, a.headers)
        return d


if __name__ == '__main__':
    a={'username':'liang',
        'password':'liang',
       }
    r=test_Interface('http://127.0.0.1:12356')
    c=r.web_api('post','/login',a)
    print(c)



    # adb='start cmd/k  ipconfig'
    # os.system(adb)
