from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_API_KEY'

def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    prompt = "Generate some dynamic content for my website."
    content = generate_content(prompt)
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
