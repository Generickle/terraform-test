from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Set up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def chat():
    response_text = ''
    if request.method == 'POST':
        user_message = request.form['message']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use a different model as needed
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        response_text = response.choices[0].message['content'].strip()
    
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
