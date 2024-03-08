from flask import Flask, render_template, request
import cohere
from cohere.responses.classify import Example

app = Flask(__name__)
co = cohere.Client('dAxSoAHq2B95WA3eItl7wR3VqchNQV3TXk5LuRpP')  # Replace with your actual API key

examples = [
  Example("Do you offer same day shipping?","Shipping and handling policy"),
  Example("Can you ship to Italy?","Shipping and handling policy"),
  Example("How long does shipping take?","Shipping and handling policy"),
  Example("Can I buy online and pick up in store?","Shipping and handling policy"),
  Example("What are your shipping options?","Shipping and handling policy"),
  Example("My order arrived damaged, can I get a refund?","Start return or exchange"),
  Example("You sent me the wrong item","Start return or exchange"),
  Example("I want to exchange my item for another colour","Start return or exchange"),
  Example("I ordered something and it wasn't what I expected. Can I return it?","Start return or exchange"),
  Example("What's your return policy?","Start return or exchange"),
]
inputs = [
    "Am I still able to return my order?",
    "When can I expect my package?",
    "Do you ship overseas?",
    "can I still return my order?",
    "When can I get my package?",
    "Do you have ship locally?"
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        text = request.form['text']
        response = co.classify(inputs=[text], examples=examples)
        return render_template('result.html', text=text, result=response)


if __name__ == '__main__':
    app.run(debug=True)