
from flask import Flask, redirect, render_template, request, send_from_directory
import open_ai
import unsplash
import tup
from bs4 import BeautifulSoup
import mysql_connection
import uns
import convert
import os.path

app = Flask(__name__, static_url_path='')


@app.route('/templates/<path:path>')
def send_templates(path):
    return send_from_directory('templates', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/favicon/<path:path>')
def send_favicon(path):
    return send_from_directory('favicon', path)


@app.route('/unsplashy/<path:path>')
def send_unsplashy(path):
    return send_from_directory('unsplashy', path)

@app.route('/output/<path:path>')
def send_output(path):
    return send_from_directory('output', path)

@app.route('/', methods=['GET', 'POST'])
def root():
    api_response = ""
    unsplash_result = ""
    result=""
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        #moved code below to main.py to check in terminal but we will still use flask_server for the actual website
        #user_input=input("Describe what you want your website to look like")

        api_response = open_ai.openai_request(user_input)

        unsplash_result = unsplash.search_unsplash(user_input, 3)

        id1 = unsplash_result[0]
        id2 = unsplash_result[1]
        id3 = unsplash_result[2]

        prompt="\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" + "\n</head>" + "\n<body" + "style='background-image:src(" + "'https://unsplash.com/photos/" + id1 + "/download'" + ")>"
        #response=tup.convertTuple(api_response)
        #prompt=tup.convertTuple(prompt)
        
        
        #mysql_connection.save_data(user_input, response)
        #save_path='output'
        #file_name="output.html"
        #completeName = os.path.join(save_path, file_name)
        result=prompt+api_response+ "<img src='https://unsplash.com/photos/" + id1 + "/download'alt='' width='400' height='400'>" +"<img src='https://unsplash.com/photos/" + id2 + "/download'alt='' width='400' height='400'>" + "<img src='https://unsplash.com/photos/" + id3 + "/download'alt='' width='400' height='400'>" + "</body>" + "<style>" + "</style>" + "<script>" + "</script>" 
        soup=BeautifulSoup(result, "html.parser")
        with open("output/output.html", "w+") as file:
            #file = open(completeName, "w")
            file.write(soup.prettify())

    return render_template('index.html', api_response=result, unsplash_results=unsplash_result)
