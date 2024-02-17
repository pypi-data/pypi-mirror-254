# nailplot.py
import requests

def get_data(qn, line=None):
    content = requests.get(
        "https://raw.githubusercontent.com/vinodhugat/qqqqq/main/"+qn)
    
    if line is not None:
        modcontent = content.text.split("\n")
        return modcontent[line]
    else:
        return content.text
