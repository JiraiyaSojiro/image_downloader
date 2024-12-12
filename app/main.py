import os
import pandas as pd
import requests

# กำหนดเส้นทางไปยังไฟล์ Excel
excel_path = '/input/image_links.xlsx'

# กำหนดโฟลเดอร์ที่ต้องการบันทึกรูปภาพ
save_folder = '/data/images'

# สร้างโฟลเดอร์หากยังไม่มี
os.makedirs(save_folder, exist_ok=True)

# อ่านข้อมูลจากไฟล์ Excel
df = pd.read_excel(excel_path)

# วนลูปผ่านแต่ละแถวใน DataFrame
for index, row in df.iterrows():
    img_url = row['URL_File']
    img_name = row['Name_File']
    img_extension = os.path.splitext(img_url)[-1]  # ดึงนามสกุลไฟล์จาก URL
    save_path = os.path.join(save_folder, f"{img_name}{img_extension}")

    try:
        # ดึงข้อมูลรูปภาพจาก URL
        response = requests.get(img_url)
        response.raise_for_status()  # ตรวจสอบว่าการร้องขอสำเร็จ

        # บันทึกรูปภาพลงในโฟลเดอร์ที่กำหนด
        with open(save_path, 'wb') as f:
            f.write(response.content)

        print(f"บันทึกรูปภาพ: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {img_url}: {e}")
