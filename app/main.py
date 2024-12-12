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

# ฟังก์ชันเพื่อดึงนามสกุลไฟล์จาก Content-Type
def get_extension_from_content_type(content_type):
    if content_type == 'image/jpeg':
        return '.jpg'
    elif content_type == 'image/png':
        return '.png'
    elif content_type == 'image/gif':
        return '.gif'
    # เพิ่มเติมตามต้องการ
    else:
        return ''

# วนลูปผ่านแต่ละแถวใน DataFrame
for index, row in df.iterrows():
    img_url = row['URL_File']
    img_name = row['Name_File']
    save_path = os.path.join(save_folder, img_name)  # กำหนดชื่อไฟล์เบื้องต้น

    try:
        # ส่งคำขอแบบ HEAD เพื่อดึง Content-Type
        head_response = requests.head(img_url)
        head_response.raise_for_status()  # ตรวจสอบว่าคำขอสำเร็จ

        # ดึง Content-Type จากส่วนหัว
        content_type = head_response.headers.get('Content-Type')
        if content_type:
            # กำหนดนามสกุลไฟล์จาก Content-Type
            extension = get_extension_from_content_type(content_type)
            save_path += extension
        else:
            print(f"ไม่สามารถดึง Content-Type จาก {img_url}")
            continue

        # ดึงข้อมูลรูปภาพจาก URL
        response = requests.get(img_url)
        response.raise_for_status()  # ตรวจสอบว่าคำขอสำเร็จ

        # บันทึกรูปภาพลงในโฟลเดอร์ที่กำหนด
        with open(save_path, 'wb') as f:
            f.write(response.content)

        print(f"บันทึกรูปภาพ: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {img_url}: {e}")
