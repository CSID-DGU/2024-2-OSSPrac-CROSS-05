from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# '/' 경로로 index.html 렌더링
@app.route('/')
def index():
    return render_template('index.html')

# '/input' 경로로 input.html 렌더링
@app.route('/input')
def input_page():
    return render_template('input.html')

# '/result' 경로로 POST 요청 처리
@app.route('/result', methods=['POST'])
def process_data():
    # 사용자가 입력한 데이터를 수집
    team_data = request.form.to_dict(flat=False)
    print("Data sent to backend:", team_data)  # 디버깅용 출력

    # Backend로 데이터 전송
    backend_url = "http://backapp:5001/process"
    try:
        response = requests.post(backend_url, json=team_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error communicating with backend: {e}", 500

    # Backend에서 반환된 데이터 확인
    if response.status_code == 200:
        processed_data = response.json()
        print("Data received from backend:", processed_data)  # 디버깅용 출력
        return render_template('result.html', team_name=processed_data['team_name'], teamMembers=processed_data['team_members'])
    else:
        return f"Error from backend: {response.status_code} {response.text}", 500


# '/contact' 경로로 연락처 정보 렌더링
@app.route('/contact')
def contact():
    # URL에서 전달받은 데이터
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    return render_template('contact.html', name=name, email=email, phone=phone)

if __name__ == '__main__':
    # Flask 앱 실행
    app.run(debug=True, host='0.0.0.0', port=5000)
