from flask import Flask, request, jsonify

app = Flask(__name__)

# '/process' 경로로 POST 요청 처리
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    print("Received data from frontend:", data)  # 디버깅용 출력

    team_name = data.get('team_name', [''])[0]
    names = data.get('name[]', [])
    majors = data.get('major[]', [])
    roles = data.get('role[]', [])
    phones = data.get('phone[]', [])
    email_locals = data.get('emailLocal[]', [])
    email_domains = data.get('emailDomain[]', [])

    team_members = []
    for name, major, role, phone, email_local, email_domain in zip(
            names, majors, roles, phones, email_locals, email_domains):
        member = {
            'name': name,
            'major': major,
            'role': role,
            'phone': phone,
            'email': f"{email_local}@{email_domain}",
            'profilePicture': 'static/leader.png' if role == '팀장' else 'static/member.png'
        }
        team_members.append(member)
        print("Processed member:", member)  # 디버깅용 출력

    team_members.sort(key=lambda x: x['role'] != '팀장')

    response = {
        'team_name': team_name,
        'team_members': team_members
    }
    print("Response to frontend:", response)  # 디버깅용 출력
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
