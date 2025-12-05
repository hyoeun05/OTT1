from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 임시 데이터 (나중에 DB에서 가져오는 구조로 변경 가능)
MOCK_DATA = [
    {
        "id": 1,
        "title": "2",
        "date": "2025-12-26",
        "ott": "Netflix",
        "poster": "",
        "desc": ".",
        "link": "https://www.netflix.com"
    },
    {
        "id": 2,
        "title": "",
        "date": "2026-01-15",
        "ott": "Disney+",
        "poster": "https://via.placeholder.com/300x450.png?text=Moving+2",
        "desc": "즈.",
        "link": "https://www.disneyplus.com"
    },
    {
        "id": 3,
        "title": "환승연애 4",
        "date": "2025-10-01 ~ 2026-01 매주 수요일 6시",
        "ott": "TVING",
        "poster": "love_transit4.jpg",
        "desc": "다양한 이유로 이별한 커플들이 한 집에 모여 지나간 연애를 되짚고 새로운 인연을 마주하며 자신만의 사랑을 찾아가는 연애 리얼리티.",
        "link": "https://www.tving.com/contents/E004438927"
    },
]

@app.route('/')
def home():
    # 날짜 순으로 데이터 정렬 (가장 가까운 날짜가 먼저 오도록)
    sorted_data = sorted(MOCK_DATA, key=lambda x: x['date'])
    return render_template('index.html', movies=sorted_data)

if __name__ == '__main__':
    app.run(debug=True)