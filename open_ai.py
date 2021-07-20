import constant
import json
import logit_bias_3
import logit_bias_2
import logit_bias_1
import openai
from bs4 import BeautifulSoup
import tup
import mysql_connection
import unsplash
import uns



def openai_request(user_input):
    with open('keys.json') as f:
        keys = json.load(f)
    openai.api_key = keys['openapi']
    id1 = uns.uns(0)
    #id2 = uns.uns(1)
    #id3 = uns.uns(2)
    #start_request = "\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" +  "<script src='script.js'></script>\n"  + "<style>\n" + "<!--style only-->\n" + "body{\n" + "background-image:<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>"

    response = openai.Completion.create(
        prompt="\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" +  "<script src='script.js'></script>\n"  + "<style>\n" + "<!--style only-->\n" + "body{\n",
        #prompt= "Website Generator, turn text into HTML, \n\n <html> <head> <title> </title> </head> <script src='script.js'></script> <img src='' photos alt='' width='500' height='600'> <style> <!--style only--> </style> <!--html only--> <body> </body> </html> " ,
        #prompt= "\n<html>" + "\n<head>" +  "\n<title>" + user_input + "</title>\n" +  "<script src='script.js'></script>\n"  + "<style>\n" + "<!--style only-->\n" + "body{\n" + "background-image:<img src='https://unsplash.com/photos/" + id1 + "'alt='' width='' height=''>",
        engine=constant.ENGINE,
        max_tokens=constant.MAX_TOKENS,
        frequency_penalty=constant.FREQUENCY_PENALTY,
        logit_bias=logit_bias_3.logit_bias_3,
        # logit_bias=logit_bias_1.logit_bias_1,
        presence_penalty=constant.PRESENCE_PENALTY,
        temperature=constant.TEMPERATURE,
        top_p=constant.TOP_P,

    )
    
    return response.choices[0].text
    """
    response.choices[0].text
    css_code = start_request + \
        response.choices[0].text + "\n</style>" + "\n<body>\n"
    
        html_code = start_request+response.choices[0].text
        print(html_code)
        return response.choices[0].text
    

    #start_request = css_code
    response2 = openai.Completion.create(
        prompt=css_code,
        engine=constant.ENGINE,
        max_tokens=constant.MAX_TOKENS,
        frequency_penalty=constant.FREQUENCY_PENALTY,
        logit_bias=logit_bias_2.logit_bias_2,
        presence_penalty=constant.PRESENCE_PENALTY,
        temperature=constant.TEMPERATURE,
        top_p=constant.TOP_P,

    )
    
    response2.choices[0].text
    html_code = css_code + "\n\n<!--This is where the html starts...-->\n\n" + \
        response2.choices[0].text + "\n </html>"
    html_code = html_code.lower()
    print(html_code)
    
    return response.choices[0].text + response2.choices[0].text
    
"""