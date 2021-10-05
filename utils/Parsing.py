from bs4 import BeautifulSoup as Bs


class Parsing:
    def __init__(self,dom):
        self.soup = Bs(dom,"html.parser")
    def GetHeaderData(self):
        features = self.soup.select('div.c-bh-strip__label')
        return features

      
