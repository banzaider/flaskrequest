import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    url = request.form.get('message')
    print(f"Received from PHP: {url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # ส่งข้อมูล HTML ที่ได้กลับไปยัง PHP
        return soup.prettify()
    else:
        return f"ไม่สามารถเข้าถึงเว็บไซต์ได้: {response.status_code}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
