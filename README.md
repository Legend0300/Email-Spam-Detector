# Email Spam Detection Web App

This repository contains a simple Flask web application for detecting whether an email is spam or not. The application uses a pre-trained machine learning model to make predictions on the provided email content.

## Installation and Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/email-spam-detection.git
   cd email-spam-detection
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask scikit-learn
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and visit [http://localhost:5000](http://localhost:5000) to access the web app.

## How It Works

1. Upon visiting the web app, you will see a form where you can enter your email content.

2. Type your email content in the provided text area.

3. Click the "Check for Spam" button to submit the form.

4. The web app will send the entered email content to the server for prediction.

5. The server will use a pre-trained spam classifier (loaded from `spam_classifier.pkl`) to make a prediction.

6. The prediction result ("Spam" or "Not Spam") will be displayed below the form.

## Web App Structure

- `app.py`: The main Flask application script that handles requests and prediction logic.

- `spam_classifier.pkl`: A pre-trained machine learning model (pickle file) used for email spam classification.

- `templates/index.html`: The HTML template for the web app interface.

- `static`: A directory containing static files (e.g., CSS, JavaScript) for styling and interactive behavior.

## Styling and Typography

The web app interface is designed using Bootstrap for responsive design and custom CSS for styling. It features a simple and clean layout for ease of use. The main headings and typography have been structured as follows:

### Main Heading (h1)

Email Spam Detection Web App

### Subheading (h2)

Installation and Setup

How It Works

Web App Structure

### Code and File Names

File names and code snippets are formatted using inline code backticks:

`app.py`

`spam_classifier.pkl`

### Code Blocks

```python
@app.route('/predict', methods=['POST'])
def predict():
    # Get the email data from the form
    data = request.form["emailInput"]

    # Load the pre-trained classifier
    pickel_in = open('spam_classifier.pkl', 'rb')
    classifier = pickle.load(pickel_in)

    # Make a prediction on the email data   
    prediction = classifier.predict([data])

    # Print the response in the backend
    print("Received email:", data)
    print("Prediction:", prediction)

    # ...
    # Rest of the code
    # ...
```

### Links

Links to external resources are styled with a blue color and an underline:

[Bootstrap CSS](https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css)

### Buttons

Buttons have a blue primary color and a darker shade on hover:

<button type="submit" class="btn btn-primary">Check for Spam</button>

## Acknowledgments

This web app is for educational and demonstration purposes only. The spam classifier model used in this example may not be optimized for production use. It is recommended to use larger and more diverse datasets for building robust spam detection models in real-world applications.

Please ensure that you comply with ethical guidelines and data privacy regulations when handling user data or training machine learning models for email spam detection.

---
