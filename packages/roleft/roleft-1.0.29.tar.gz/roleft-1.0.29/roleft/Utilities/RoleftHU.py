import requests




class HU:
    @classmethod
    def GetHtmlContent(cls, url: str = 'http://www.baidu.com') -> str:
        resp = requests.get(url)
        return resp.text