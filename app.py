from flask import Flask, render_template, request, redirect, url_for, make_response
import json
app = Flask(__name__)

app.secret_key = 'secret key'

@app.route('/',methods = ['GET'])
def index():
    return redirect('/home')

@app.route('/home', methods =['GET'])
def home():
    # data= read from file
    with open('db.json', 'r') as openfile:
        json_object = json.load(openfile)
    
    print(json_object)
    return render_template('index.html', data=json_object)

@app.route('/statusForm', methods =['GET', 'POST'])
def statusForm():
    if request.method== 'POST':
        # write to file
        json_object = json.dumps(request.form, indent = 4)
 
        with open("db.json", "w") as outfile:
            outfile.write(json_object)
        return redirect('/home')
    else:
        return render_template('form.html')

if __name__ == '__main__':
   app.run(debug=True)