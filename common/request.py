import requests,os,logging
from common.oppymysql import Open_mysql
from websocket import create_connection
import os
import json

class web_Interface(object):
    def __init__(self,url_root):
        self.url_root= url_root
        self.websocket_status = False

    def __del__(self):
        if self.websocket_status==True:
            self.ws.close()

    def default_headers(self):
        self.headers = {'Referer':self.url_root}
        return self.headers

    def web_api(self,method,url,data_OR_param,headers=None,response_content=0,files=None):
        '''
        
        :param method: 传入str类型的'post','get'和'ws'（websocket）
        :param url: 路由
        :param data_OR_param: 参数，可以传入str或dict
        :param headers: 没有特殊要求，可以传入，dict类型
        :param dictText: True 或 False，  True则返回一个内容为requests.text的dict，False返回一个requests对象，
                自己处理，如requests.XXX
        :return: 
        '''
        lowermethod=method.lower()

        if headers==None:
            headers=self.default_headers()

        if lowermethod == 'post':
            if files==None:
                d=self.http_post(url=url,data=data_OR_param,headers=headers)
                response = self.response_content(d=d, response_content=response_content)
                return response
            else:
                d=self.http_post_upload(url=url,data=data_OR_param,headers=headers,files=files)
                response = self.response_content(d=d, response_content=response_content)
                return response

        elif lowermethod == 'get':
            d=self.http_get(url=url,param=data_OR_param,headers=headers)
            response=self.response_content(d=d,response_content=response_content)
            return response

        elif lowermethod == 'ws':
            self.websocket_status = True
            url_root=self.url_root
            d=self.websocket_send(url_root=url_root,param=data_OR_param)

        else:
            print("无对应接口类型："+ method)



    # def httpResponse_message(self,status_code,text,cookies,headers):
    #     d={}
    #     d["status_code"]=status_code
    #     d["cookies"]=cookies
    #     d["headers"]=headers
    #     d["text"] = text
    #     return d

    def response_content(self,d,response_content):
        if response_content == 1:
            dict = json.loads(d.text)
            return dict
        elif response_content == 0:
            return d
        else:
            dict = json.loads(d.text)
            dictValue = dict[response_content]
            return dictValue

    def websocket_send(self,url_root,param):
        self.ws = create_connection(url_root)
        self.ws.send(param)
        res = self.ws.recv()
        return res

    def http_post(self,url,data,headers):
        interface_url=self.url_root + url
        a=requests.session().post(url=interface_url,data=data,headers=headers)
        return a

    def http_post_upload(self,url,data,headers,files):
        interface_url=self.url_root + url
        a=requests.session().post(url=interface_url,data=data,headers=headers,files=files)
        return a

    def http_get(self,url,param,headers):
        interface_url= self.url_root + url
        a=requests.get(url=interface_url,params=param,headers=headers)
        return a


if __name__ == '__main__':
    r = web_Interface("http://192.168.1.104")
    urlsession = '/abs/psshop/open/chk/login'
    param = 'usercode=18229922307&pwd=e10adc3949ba59abbe56e057f20f883e&sessionid='
    session = r.web_api(method='get', url=urlsession, data_OR_param=param,response_content='data')
    print(session)
    print(type(session))



    # adb='start cmd/k  ipconfig'
    # os.system(adb)
