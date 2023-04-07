from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/get_answer', methods=['POST'])
def get_answer():
    city = request.json.get('city')
    work = request.json.get('work')
    years_of_experience = request.json.get('years_of_experience')

    prompt = f"How much does an hour of my work cost if I live in {city} I have worked {work} for {years_of_experience} years, say answer in USA Dollar"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=["."],
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()

    return jsonify({'answer': answer})
