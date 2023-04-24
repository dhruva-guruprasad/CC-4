from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods = ['POST', 'GET'])
def index():
    num_1 = request.form.get("first")
    num_2 = request.form.get('second')
    op = request.form.get('operation')
    result = ''
    input_check = 0

    if num_1 == '' or num_2 == '':
        input_check = 1
    	
        flash('Please enter both the numbers')
    elif op == 'add':
        result = requests.get("http://add:5051/add/" + str(num_1) + "/" + str(num_2)).text
    elif op == 'minus':
        result =  requests.get("http://subtract:5052/subtract/" + str(num_1) + "/" + str(num_2)).text
    elif op == 'multiply':
        result = requests.get("http://multiply:5053/multiply/" + str(num_1) + "/" + str(num_2)).text
    elif op == 'divide':
    	
        result = requests.get("http://divide:5054/divide/" + str(num_1) + "/" + str(num_2)).text
    
    elif op == 'mod':
    	
        result = requests.get("http://mod:5055/mod/" + str(num_1) + "/" + str(num_2)).text
    elif op == 'lt':
    	
        result = requests.get("http://lt:5056/lt/" + str(num_1) + "/" + str(num_2)).text
    elif op == 'gt':
    	
        result = requests.get("http://gt:5057/gt/" + str(num_1) + "/" + str(num_2)).text
	
    if input_check == 0:
    	
        flash(f'The result of operation {op} on {num_1} and {num_2} is {result}')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )