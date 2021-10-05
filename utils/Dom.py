from requests_html import HTMLSession
class Dom:
    def __init__(self,url):
        self.url = url
        self.s = HTMLSession()
    def GetDom(self):
        r = self.s.get(self.url)
        r.html.render(timeout=20)
        return r.text

