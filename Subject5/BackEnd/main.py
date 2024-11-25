from flask import Flask, request

app = Flask(__name__)

# 기본 홈 경로
@app.route('/')
def home():
    return "Welcome to the Backend Server!"

# favicon 요청 처리
@app.route('/favicon.ico')
def favicon():
    return '', 204

# 프론트엔드에서 데이터를 받아 처리
@app.route('/process', methods=['POST'])
def process_data():
    # 프론트엔드에서 전달받은 데이터
    name = request.form.get('Name', 'Unknown')
    student_number = request.form.get('StudentNumber', 'Unknown')
    gender = request.form.get('Gender', 'Unknown')
    major = request.form.get('Major', 'Unknown')
    programming_languages = request.form.getlist('PL_list')

    # 결과 데이터를 플레인 텍스트 형식으로 반환
    result_data = f"{name}|{student_number}|{gender}|{major}|{','.join(programming_languages)}"
    return result_data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)  # BackEnd는 5001번 포트에서 실행