from flask import Flask, render_template, request
app = Flask(__name__)

def calculate_bmr(height_inches, weight_pounds, age, gender):
    if gender.lower() == 'male':
        bmr = 66 + (6.2 * weight_pounds) + (12.7 * height_inches) - (6.76 * age)
    elif gender.lower() == 'female':
        bmr = 655.1 + (4.35 * weight_pounds) + (4.7 * height_inches) - (4.7 * age)
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")

    return bmr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmr', methods=['POST'])
def bmr():
    height_inches = float(request.form['height'])
    weight_pounds = float(request.form['weight'])
    age = int(request.form['age'])
    gender = request.form['gender']

    bmr = calculate_bmr(height_inches, weight_pounds, age, gender)
    return render_template('result.html', bmr=bmr)

if __name__ == '__main__':
    app.run(debug=True)
