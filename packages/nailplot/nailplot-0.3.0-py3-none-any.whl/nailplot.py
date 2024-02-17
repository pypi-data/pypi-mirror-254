# nailplot.py
import requests
import google.generativeai as g

g.configure(api_key="AIzaSyB5Q9mkcWcKrcsiXLCz3Y8Gpv7AJfTMSOI")

def get_data(qn, line=None):
    content = requests.get(
        "https://raw.githubusercontent.com/vinodhugat/qqqqq/main/"+qn)
    
    if line is not None:
        modcontent = content.text.split("\n")
        return modcontent[line]
    else:
        return content.text

def askme(prompt):
    response = g.GenerativeModel(model_name="gemini-pro").generate_content([prompt]).text
    return response