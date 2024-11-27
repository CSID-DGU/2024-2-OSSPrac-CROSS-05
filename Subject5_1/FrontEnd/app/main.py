from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 입력 페이지 렌더링 
@app.route('/') 
def main():
    return render_template('input_info.html')

# 결과 페이지 렌더링
@app.route('/result', methods=['POST'])
def result():
    # 사용자 입력 데이터를 수집
    form_data = {
        "Name": request.form.get('Name'),
        "StudentNumber": request.form.get('StudentNumber'),
        "Gender": request.form.get('Gender'),
        "Major": request.form.get('Major'),
        "PL_list": request.form.getlist('PL_list')
    }

    # 백엔드로 데이터 전달 및 결과 수신
    response = requests.post('http://backapp:5001/process', data=form_data)
    result_data = response.text.split('|')  # 플레인 텍스트 파싱

    # 결과 페이지 렌더링
    return render_template(
        'result.html',
        Name=result_data[0],
        StudentNumber=result_data[1],
        Gender=result_data[2],
        Major=result_data[3],
        Languages=result_data[4]
    )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # FrontEnd는 5000번 포트에서 실행
