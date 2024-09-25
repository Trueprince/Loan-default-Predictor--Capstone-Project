import flask
import pandas as pd
from joblib import load 

# Load the model
model_path = 'C:\\Users\\202207760\\Desktop\\Capstone Project webpage\\Loan-Default-Predictor-main\\DeploymentModel.joblib'
model = load(model_path)

app = flask.Flask(__name__, template_folder='templates')

# Route for the home page
@app.route('/', methods=['GET'])
def home():
    return flask.render_template('home.html')

# Route for the loan prediction form
@app.route('/predict', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    if flask.request.method == 'POST':
        # Get form input
        Age = flask.request.form['Age']
        Income = flask.request.form['Income']
        LoanAmount = flask.request.form['LoanAmount']
        CreditScore = flask.request.form['CreditScore']
        MonthsEmployed = flask.request.form['MonthsEmployed']
        NumCreditLines = flask.request.form['NumCreditLines']
        InterestRate = flask.request.form['InterestRate']
        LoanTerm = flask.request.form['LoanTerm']
        DTIRatio = flask.request.form['DTIRatio']
        Education = flask.request.form['Education']
        EmploymentType = flask.request.form['EmploymentType']
        MaritalStatus = flask.request.form['MaritalStatus']
        HasMortgage = flask.request.form['HasMortgage']
        HasDependents = flask.request.form['HasDependents']
        LoanPurpose = flask.request.form['LoanPurpose']
        HasCoSigner = flask.request.form['HasCoSigner']

        # Create DataFrame for the model
        incoming_vector = pd.DataFrame(
            [[
                Age, Income, LoanAmount, CreditScore, MonthsEmployed,
                NumCreditLines, InterestRate, LoanTerm, DTIRatio, 
                Education, EmploymentType, MaritalStatus, HasMortgage,
                HasDependents, LoanPurpose, HasCoSigner
            ]],
            columns=[ 
                'Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed',
                'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 
                'Education', 'EmploymentType', 'MaritalStatus', 'HasMortgage',
                'HasDependents', 'LoanPurpose', 'HasCoSigner'
            ],
            index=['input']
        )

        # Check the input format
        print("Input Vector:\n", incoming_vector)

        # Prediction
        prediction = model.predict(incoming_vector)[0]
        print("Prediction:", prediction)  # Debug print

        if prediction == 1:
            return flask.render_template('result_Yes.html')
        else:
            return flask.render_template('result_No.html')

# Route for About Us page
@app.route('/about', methods=['GET'])
def about():
    return flask.render_template('about.html')

# Route for Contact Us page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        subject = flask.request.form['subject']
        message = flask.request.form['message']
        
        return flask.redirect(flask.url_for('contact_success'))
    return flask.render_template('contact.html')

@app.route('/contact-success', methods=['GET'])
def contact_success():
    return flask.render_template('contact_success.html')

# Route for News page
@app.route('/news', methods=['GET'])
def news():
    return flask.render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
