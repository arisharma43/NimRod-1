from bs4 import BeautifulSoup
import open_ai
import mysql_connection
import tup
import flask_server
import unsplash
from flask import request
import uns
import convert

user_input = input("Simply describe what you want to see in HTML:\n")
#user_input = flask_server.root()
id1 = uns.uns(0)
id1=convert.listToString(id1)
#prompt="\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" + "<script src='script.js'></script>\n" + "<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>" + "<style>\n" + "<!--style only-->\n" + "body{\n"
prompt= "\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" +  "<script src='script.js'></script>\n"  + "<style>\n" + "<!--style only-->\n" + "body{\n" ,
response = open_ai.openai_request(user_input)
# python3 main.py



#print(soup.prettify())
