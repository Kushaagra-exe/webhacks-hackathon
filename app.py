from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyDl9IMiuDS254NMT3l02pYOuOw0UUz0IFk")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompts = "I'm looking for a {} trip to {} that fits within my {}. My travel interests include {} and I prefer a {} experience. I'm planning to travel during {} and my current location is {}"



app = Flask(__name__)


@app.route('/')
def home():
    return "working"


@app.route('/home', methods=['GET','POST'])
def homepage():
    if request.method == "GET":
        return render_template("Homepage.html")
    elif request.method == "POST":
        data = request.form
        duration = data['duration']
        dest_type = data['dest_type']
        Budget = data['Budget']
        interests = data['interests']
        style = data['style']
        when = data['when']
        curr_location = data['curr_location']

        final_prompt = prompts.format(duration,dest_type,Budget, interests, style, when, curr_location)
        jsonresp = ["input:{}".format(final_prompt),
                    "output: ",
        ]
        return jsonresp


if __name__ == '__main__':
    app.run(debug=True)

