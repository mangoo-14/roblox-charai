
#things
#from bardapi import Bard
#from characterai import PyCAI
from flask import Flask, render_template, request
import openai
openai.api_key = 'pk-EhBaJKLdShkJhtydCtnkDTUicIgehXBFWTBNSBnuZOmTBwTH'
openai.api_base = 'https://api.pawan.krd/v1'
#import os
#bard:
#msg = Bard().get_answer(str(received_data))["content"]
#os.environ["_BARD_API_KEY"] = "XQjNkfUfAbguKsg5pkajFWa5q08kE4w3wSeqwC0z029pQFXCahnfJdYAhqiiGjk58HksUg."


# flask


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST', 'GET', "POST / HTTP/1.1"])
def test():
    if request.method == 'GET':
        msg = "This is a response to the Roblox instance, sent from Python"
        print("SENT >>", msg)
        return msg

    if request.method == 'POST':
        received_data = request.get_data().decode('utf-8')
        
        if received_data == "/newchat":
            print("RECEIVED >> ", received_data)	
            msg = "new chat!"
            print("SENT >> ", msg)
            return str(msg)
        else:
            response = openai.Completion.create(
        model="text-davinci-003",
        prompt=(received_data, "\nAI:"),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Human: ", "AI: "]
)

        print("RECEIVED >> ", received_data)	
        msg = response.choices[0].text
        print("SENT >> ", msg)
        return str(msg)


app.run(host='0.0.0.0',port='1111',debug=False)






