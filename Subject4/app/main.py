# Description: 사용자로부터 입력받은 값을 result 페이지에 출력하는 스크립트

from flask import Flask, render_template, request

# flask 애플리케이션 생성
app = Flask(__name__)

# main 페이지 route 설정
@app.route('/')
def main():
    return render_template('input_info.html')

# result 페이지 route 설정
@app.route('/result', methods=['POST'])
def result():
    # form 데이터에서 입력 값 가져오기
    name = request.form['Name']
    student_number = request.form['StudentNumber']
    gender = request.form['Gender']
    major = request.form['Major']
    programming_languages = request.form.getlist('PL_list')

    # result 페이지 렌더링
    return render_template('result.html', Name=name, StudentNumber=student_number, Gender=gender, Major=major, Languages=', '.join(programming_languages))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # 애플리케이션 IP 설정 후 실행
