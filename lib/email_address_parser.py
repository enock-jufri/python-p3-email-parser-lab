# your code goes here!
import re

class EmailAddressParser:
    def __init__(self,text):
        self.text=text
    
    def parse(self):
        emails= re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',self.text)
        return sorted(set(emails))
    
parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
print(parser.parse())