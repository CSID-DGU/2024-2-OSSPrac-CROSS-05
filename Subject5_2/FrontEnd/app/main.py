from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# '/' 경로로 요청이 들어오면 index.html 렌더링
@app.route('/')
def index():
    return render_template('index.html')

# '/input' 경로로 요청이 들어오면 input.html 렌더링
@app.route('/input')
def input_page():
    return render_template('input.html')

# '/result' 경로로 POST 요청이 들어오면 백엔드와 통신 후 결과 렌더링
@app.route('/result', methods=['POST'])
def result():
    # 입력 데이터 수집
    form_data = {
        "team_name": request.form.get('team_name'),
        "name[]": request.form.getlist('name[]'),
        "major[]": request.form.getlist('major[]'),
        "role[]": [request.form.get(f'role_{i}') for i in range(len(request.form.getlist('name[]')))],
        "phone[]": request.form.getlist('phone[]'),
        "emailLocal[]": request.form.getlist('emailLocal[]'),
        "emailDomain[]": request.form.getlist('emailDomain[]')
    }

    # 백엔드로 데이터 전송 및 처리 결과 수신
    response = requests.post('http://backapp:5001/process', data=form_data)
    result_data = response.json()

    # 결과 페이지 렌더링
    return render_template(
        'result.html',
        team_name=result_data['team_name'],
        teamMembers=result_data['team_members']
    )

# '/contact' 경로로 요청이 들어오면 contact.html 렌더링
@app.route('/contact')
def contact():
    email = request.args.get('email')
    phone = request.args.get('phone')
    return render_template('contact.html', email=email, phone=phone)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
