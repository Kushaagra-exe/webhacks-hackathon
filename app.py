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

prompts = " Suggest 5 exciting travel destinations that perfectly match my preferences. I'm looking for a {} days trip to a {} that fits within my budget of {}. My travel interests include {} and I prefer a {} experience. I'm planning to travel during {} and my current location is {}. Answer is the following format **suggestion 1** - description about that place and so on for 5 suggestions "



app = Flask(__name__)


@app.route('/')
def home():
    return "working"

@app.route('/home', methods=['GET','POST'])
def homepage():
    return render_template("Homepage.html")


@app.route('/suggestor', methods=['GET','POST'])
def suggestor():
    if request.method == "GET":
        return render_template("Suggestor.html")
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

        response = model.generate_content(jsonresp)
        newresp = response.text.replace("** * **", "<strong>")
        newresp = newresp.replace(":**", "</strong>")
        newresp = newresp.replace(". **", "<br>")
        newresp = newresp.replace("**", "")
        newresp = newresp.replace("*", "<br>")
        newresp = newresp.replace("Suggestion", "<br><br>Suggestion")



        return newresp, 200

        # return jsonresp


if __name__ == '__main__':
    app.run(debug=True)

