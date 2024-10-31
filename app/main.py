from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['Name']
    student_number = request.form['StudentNumber']
    gender = request.form['Gender']
    major = request.form['Major']
    programming_languages = request.form.getlist('PL_list')

    return render_template('result.html', Name=name, StudentNumber=student_number, Gender=gender, Major=major, Languages=', '.join(programming_languages))

if __name__ == '__main__':
    app.run(debug=True)
