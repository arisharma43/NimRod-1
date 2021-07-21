from bs4 import BeautifulSoup
import open_ai
import mysql_connection
import tup
import flask_server
import unsplash
from flask import request
import uns
import convert
import convert
import os.path

user_input = input("Simply describe what you want to see in HTML:\n")
#user_input = flask_server.root()
id1 = uns.uns(0)
id1=convert.listToString(id1)
#prompt="\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" + "<script src='script.js'></script>\n" + "<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>" + "<style>\n" + "<!--style only-->\n" + "body{\n"
#prompt= "\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" 
#response = open_ai.openai_request(user_input)
# python3 main.py

#user_input=input("Describe what you want your website to look like:\n")

request = open_ai.openai_request(user_input)

unsplash_result = unsplash.search_unsplash(user_input, 3)

id1 = unsplash_result[0]
id2 = unsplash_result[1]
id3 = unsplash_result[2]

prompt="\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" 
response=tup.convertTuple(request)
prompt=tup.convertTuple(prompt)
soup=BeautifulSoup(response, "html.parser")
        
        #mysql_connection.save_data(user_input, response)
#save_path='/output'
#file_name="/output.html"
#completeName = os.path.join(save_path, file_name)
result=prompt+soup.prettify()+ "background-image:<img src='https://unsplash.com/photos/" + id1 + "/download'alt='' width='400' height='400'>" +"<img src='https://unsplash.com/photos/" + id2 + "/download'alt='' width='400' height='400'>" + "<img src='https://unsplash.com/photos/" + id3 + "/download'alt='' width='400' height='400'>" + "<style>" + "</style>" + "<script>" + "</script>" 
#with open(completeName, "w+") as file:
    # file = open(completeName, "w")
    #file.write(result)
print(result)

#print(soup.prettify())
