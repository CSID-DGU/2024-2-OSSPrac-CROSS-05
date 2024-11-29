from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

# 기본 홈 경로
@app.route('/')
def home():
    return "Welcome to the CROSS Backend Server!"

# favicon 요청 처리
@app.route('/favicon.ico')
def favicon():
    return '', 204

# 프론트엔드에서 데이터를 받아 처리
@app.route('/process', methods=['POST'])
def process_data():
    # 클라이언트에서 전달받은 데이터 처리
    team_name = request.form.get('team_name')
    names = request.form.getlist('name[]')
    majors = request.form.getlist('major[]')
    roles = request.form.getlist('role[]')
    phones = request.form.getlist('phone[]')
    email_locals = request.form.getlist('emailLocal[]')
    email_domains = request.form.getlist('emailDomain[]')

    # 팀 구성원 정보 정리
    team_members = []
    for i, (name, major, role, phone, email_local, email_domain) in enumerate(
            zip(names, majors, roles, phones, email_locals, email_domains)):
        
        member = {
            'name': name,
            'major': major,
            'role': role,
            'phone': phone,
            'email': f"{email_local}@{email_domain}"
        }
        team_members.append(member)

    # 팀장을 맨 앞으로 정렬
    team_members.sort(key=lambda x: x['role'] != '팀장')

    # JSON 응답 반환
    return jsonify({"team_name": team_name, "team_members": team_members})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
