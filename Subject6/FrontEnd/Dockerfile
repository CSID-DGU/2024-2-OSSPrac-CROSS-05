# 베이스 이미지 설정
FROM ubuntu:latest

# 작업 디렉토리 설정
WORKDIR /app

# Python 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# 가상 환경 생성
RUN python3 -m venv venv

# 가상 환경 경로 설정
ENV PATH="/app/venv/bin:$PATH"

# requirements.txt 복사
COPY requirements.txt /app/requirements.txt

# requirements에 명시된 패키지(flask) 설치
RUN pip install -r /app/requirements.txt

# 애플리케이션 파일 복사
COPY . /app

# 애플리케이션 실행 명령
CMD ["python3", "app/main.py"]
