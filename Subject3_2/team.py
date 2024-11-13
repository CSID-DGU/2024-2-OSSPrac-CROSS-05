from flask import Flask, request, render_template, url_for

# Flask 애플리케이션 생성
app = Flask(__name__)

# '/' 경로로 요청이 들어오면 index.html 렌더링
@app.route('/')
def index():
    return render_template('index.html')

# '/input' 경로로 요청이 들어오면 input.html 렌더링
@app.route('/input')
def input_page():
    return render_template('input.html')

# '/result' 경로로 POST 요청이 들어오면 팀 구성원 정보 처리 후 result.html 렌더링
@app.route('/result', methods=['POST'])
def result():
    # 폼에서 입력된 팀 이름 및 팀 구성원 정보 가져오기
    team_name = request.form.get('team_name')
    names = request.form.getlist('name[]')  # 이름 목록
    majors = request.form.getlist('major[]')  # 전공 목록
    roles = [request.form.get(f'role_{i}') for i in range(len(names))]  # 역할 목록
    phones = request.form.getlist('phone[]')  # 전화번호 목록
    email_locals = request.form.getlist('emailLocal[]')  # 이메일 앞부분 목록
    email_domains = request.form.getlist('emailDomain[]')  # 이메일 도메인 목록

    # 팀 구성원 정보 저장을 위한 리스트 초기화
    team_members = []

    # 각 구성원의 정보 가져와서 딕셔너리 형태로 저장
    for i, (name, major, role, phone, email_local, email_domain) in enumerate(
            zip(names, majors, roles, phones, email_locals, email_domains)):

        # 역할에 따른 기본 프로필 이미지 설정
        if role == '팀장':
            profile_picture_url = url_for('static', filename='leader.png')  # 팀장은 leader.png 사용
        else:
            profile_picture_url = url_for('static', filename='member.png')  # 팀원이면 member.png 사용

        # 구성원 정보 딕셔너리 생성
        member = {
            'name': name,
            'major': major,
            'role': role,
            'phone': phone,
            'email': f"{email_local}@{email_domain}",
            'profilePicture': profile_picture_url
        }
        team_members.append(member)  # 리스트에 구성원 추가

    # 팀 구성원 리스트에서 팀장을 가장 앞에 오도록 정렬
    team_members.sort(key=lambda x: x['role'] != '팀장')

    # result.html을 렌더링하고 팀 이름과 팀 구성원 정보를 전달
    return render_template('result.html', team_name=team_name, teamMembers=team_members)

# '/contact' 경로로 요청이 들어오면 이메일과 전화번호 정보를 가져와 contact.html 렌더링
@app.route('/contact')
def contact():
    # URL에서 이메일과 전화번호 정보 가져오기
    email = request.args.get('email')
    phone = request.args.get('phone')

    # contact.html에 이메일과 전화번호 정보를 전달하여 렌더링
    return render_template('contact.html', email=email, phone=phone)

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
