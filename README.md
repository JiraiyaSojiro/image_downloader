# Image Downloader
This project is a Python script that utilizes the pandas and requests libraries to download images from URLs specified in an Excel file and save them locally with designated filenames. The environment is managed through Docker and Docker Compose for ease of use and deployment.

## System Requirements
- Docker
- Docker Compose

## Installation
1. **Clone this project:**

   ```bash
   git clone https://github.com/JiraiyaSojiro/image_downloader.git
   cd image_downloader
   
2. **Prepare the Excel file:**

Place an Excel file containing the columns "URL_File" and "Name_File" into the input folder, naming the file image_links.xlsx

3. **Run the project with Docker Compose:**

   ```bash
   docker-compose up --build
  
This command will build the Docker image and run the container as specified in docker-compose.yml

## Usage
After running Docker Compose, the images will be downloaded and saved in the data/images folder.

## Support
If you encounter any issues or have questions, feel free to open an issue in this repository.


**Author**
Jiraiya

------------------------------------------------------------------------------

# โปรแกรมดาวน์โหลดรูปภาพ

โปรเจกต์นี้เป็นสคริปต์ Python ที่ใช้ไลบรารี `pandas` และ `requests` สำหรับดาวน์โหลดรูปภาพจาก URL ที่ระบุในไฟล์ Excel และบันทึกลงในเครื่องด้วยชื่อไฟล์ที่กำหนด โดยมีการจัดการสภาพแวดล้อมผ่าน Docker และ Docker Compose เพื่อความสะดวกในการใช้งานและการปรับใช้

## ความต้องการระบบ

- Docker
- Docker Compose

## การติดตั้ง

1. **โคลนโปรเจกต์นี้:**

   ```bash
   git clone https://github.com/JiraiyaSojiro/image_downloader.git
   cd image_downloader
   
2. **เตรียมไฟล์ Excel:**

วางไฟล์ Excel ที่มีคอลัมน์ "URL_File" และ "Name_File" ลงในโฟลเดอร์ input โดยตั้งชื่อไฟล์ว่า image_links.xlsx

3. **รันโปรเจกต์ด้วย Docker Compose:**

   ```bash
   docker-compose up --build
  
คำสั่งนี้จะสร้าง Docker image และรันคอนเทนเนอร์ตามที่กำหนดใน docker-compose.yml

## การใช้งาน
หลังจากรัน Docker Compose รูปภาพจะถูกดาวน์โหลดและบันทึกลงในโฟลเดอร์ data/images

## การสนับสนุน**
หากคุณพบปัญหาหรือมีคำถาม สามารถเปิด Issue ใน repository นี้ได้

**ผู้เขียน**
Jiraiya
