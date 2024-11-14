# 베이스 이미지 설정
FROM ubuntu:latest

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 애플리케이션 파일 추가
COPY . /app

# 애플리케이션 실행 명령
CMD ["python3", "app.py"]
