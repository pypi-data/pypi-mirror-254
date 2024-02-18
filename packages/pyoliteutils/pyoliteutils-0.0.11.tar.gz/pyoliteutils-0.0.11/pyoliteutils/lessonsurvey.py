from urllib.parse import urlencode
import pandas as pd
from js import fetch

class lessonsurvey():
    BASEURL = "https://utc-olp-api-proxy.glitch.me/lessonsurvey/"#answer"
    student = "Change Me"

    def __init__(self, student = None) -> None:
        self.setStudent(student)
        
    def setStudent(self, student):
        self.student = student

    async def send(self, q="Change Me", a="Change Me"):
        ANSWERURL = self.BASEURL + "answer"
        URL2 = ANSWERURL + "?"+urlencode({"question":q,"answer":a, "student":self.student})
        res = await fetch(URL2)
        #res = await fetch(URL  + "?" + urlencode({"q":1, "answer":ans}))
        text = await res.text()
        return text

    async def show(self, question=None):
        ANSWERSSURL = self.BASEURL + "answers"
        res = await fetch(ANSWERSSURL)
        text = await res.text()
        data = pd.read_json(text)
        return data
    