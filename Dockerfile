# ใช้ Python base image
FROM python:3.8-slim

# กำหนด working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง dependencies
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกสคริปต์และโฟลเดอร์ที่จำเป็น
COPY app/ /app/
COPY input/ /input/
COPY data/ /data/

# รันสคริปต์ Python
CMD ["python", "main.py"]
