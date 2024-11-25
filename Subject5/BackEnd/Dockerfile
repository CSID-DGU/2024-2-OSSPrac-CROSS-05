# 베이스 이미지 설정
FROM python:3

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# requirements.txt 복사
COPY requirements.txt ./

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY . .

# 애플리케이션 실행 명령
CMD ["python3", "main.py"]
