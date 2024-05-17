from flask import Flask, render_template, request
from resumen import Resumentexto
import os
from dotenv import load_dotenv

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()
gpt_resumen = Resumentexto(api_key = os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():        
        return render_template('index.html')

@app.route('/resume', methods = ['POST'])
def prueba():
    load_dotenv()
    text = request.form['myTextArea']
    language = request.form['language']
    return render_template ('index.html', resumen = gpt_resumen.resumeTranslate(text, language))
    

if __name__ == '__main__':
    app.run()
