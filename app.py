from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the email data from the form
    data = request.form["emailInput"]

    pickel_in = open('spam_classifier.pkl','rb')
    classifier = pickle.load(pickel_in)

    # Make a prediction on the email data   
    prediction = classifier.predict([data])

    # Print the response in the backend
    print("Received email:", data)
    print("Prediction:", prediction)

    if prediction[0] == 1:
        prediction = "Spam"
    else:
        prediction = "Not Spam"


    # For this example, we'll just return the email data as JSON response
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
