import diaspora
from diaspora import Diaspora,pyrustic_data
class ProtoPy(Diaspora):
    def __init__(self):
        super().__init__()
    def add(self,post):
        self.pub(self,event=self.pub,data=post)


proto = ProtoPy()
proto.pub(data=22e)