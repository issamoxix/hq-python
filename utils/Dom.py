from requests_html import HTMLSession
class Dom:
    def __init__(self,url):
        self.url = url
        self.s = HTMLSession()
    def GetDom(self):
        try:
            r = self.s.get(self.url)
            r.html.render(timeout=20)
            return r.text
        except:
            self.s.close()
            return print('Erorr in the Dom class')

