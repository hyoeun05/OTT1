from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 임시 데이터 (나중에 DB에서 가져오는 구조로 변경 가능)
MOCK_DATA = [

    {
        "id": 4,
        "title": "이게 맞아?! 시즌 2",
        "date": "2025-12-03 ~ 2025-12-24 수",
        "ott": "Disney+",
        "poster": "areyousure.jpg",
        "cast": "지민, 정국",
        "desc": "만나기만 하면 시끌벅적한 방탄소년단의 지민, 정국. 이들은 2023년 여름, 군 입대 전 잊지 못할 추억을 남기기 위해 둘만의 여행을 떠난다! 예측 불가 <이게 맞아?!>. 과연, 지민과 정국은 무사히 여행을 마무리 지을 수 있을까?",
        "link": "https://www.disneyplus.com/ko-kr/browse/entity-a18bfb8e-0435-4795-b321-09a42c2e9e91"
    },
    {
        "id": 1,
        "title": "환승연애 4",
        "date": "2025-10-01 ~ 2026-01 수",
        "ott": "TVING",
        "poster": "love_transit4.jpg",
        "desc": "다양한 이유로 이별한 커플들이 한 집에 모여 지나간 연애를 되짚고 새로운 인연을 마주하며 자신만의 사랑을 찾아가는 연애 리얼리티.",
        "link": "https://www.tving.com/contents/E004438927"
    },
 {
        "id": 2,
        "title": "자백의 대가",
        "date": "2025-12-05",
        "ott": "Netflix",
        "poster": "priceofconfession.jpg",
        "cast": "전도연, 김고은, 박해수",
        "desc": "남편을 죽였다는 혐의로 궁지에 몰린 여자. 그녀에게 의문의 여인이 다가와 거래를 제안한다. 그 사건을 대신 자백해 주겠다는 약속. 하지만 그 대가로 누군가의 목숨을 가져와야만 한다.",
        "link": "https://www.netflix.com/kr/title/81757813?fromWatch=true" 
    },
    {
        "id": 3,
        "title": "흑백요리사: 요리 계급 전쟁 시즌 2",
        "date": "2025-12-16 ~",
        "ott": "Netflix",
        "poster": "bwcook.jpg",
        "desc": "세계를 사로잡은 요리 서바이벌 시리즈가 돌아온다. 신선한 돌풍을 일으킬 흑수저와 존재만으로도 압도적인 백수저 요리사들. 뜨거운 경쟁의 열기 속에서 살아남을 최후의 승자는 누구인가.",
        "link": "https://www.netflix.com/kr/title/81728365?fromWatch=true" 
    },
    {
        "id": 4,
        "title": "대홍수",
        "date": "2025-12-19",
        "ott": "Netflix",
        "poster": "daehongsu.jpg",
        "cast": "김다미, 박해수, 권은성",
        "desc": "대홍수가 덮친 지구 종말의 날. 물에 잠겨가는 아파트에 갇힌 연구원과 어린 아들이 탈출을 시도한다. 그 순간 도착한 중대 임무. 그녀는 인류의 운명이 걸린 과제를 끝까지 완수할 수 있을까.",
        "link": "https://www.netflix.com/kr/title/81579978?fromWatch=true" 
    },
    {
        "id": 5,
        "title": "캐셔로",
        "date": "2025-12-26",
        "ott": "Netflix",
        "poster": "cash.jpg",
        "cast": "이준호, 김혜준, 김병철, 김향기",
        "desc": "초능력을 얻게 된 평범한 남자. 그러나 초능력을 사용할 때마다 지갑 속 돈이 줄어드는 탓에 마음 편히 싸울 수가 없다. 설상가상 초능력을 훔치려는 나쁜 놈마저 기승을 부리고 있으니.",
        "link": "https://www.netflix.com/kr/title/81028446?fromWatch=true" 
    },
    {
        "id": 6,
        "title": "",
        "date": "2026-02-01",
        "ott": "Wavve",
        "poster": "",
        "desc": "",
        "link": "https://www.wavve.com",
 
    }
]

# 사용 가능한 모든 OTT 목록 추출 (중복 제거)
ALL_OTTS = sorted(list(set(item['ott'] for item in MOCK_DATA)))

# 데이터 정렬 함수
def sort_movies(data):
    """주어진 데이터를 날짜 순으로 정렬합니다."""
    return sorted(data, key=lambda x: x['date'])

@app.route('/')
def home():
    # 전체 작품 (메인 페이지)
    movies = sort_movies(MOCK_DATA)
    # 템플릿에 'all_otts'와 'active_ott' 정보도 함께 전달
    return render_template('index.html', 
                           movies=movies, 
                           all_otts=ALL_OTTS, 
                           active_ott='all')

@app.route('/ott/<ott_name>')
def filter_by_ott(ott_name):
    # OTT 이름에 따라 작품 필터링
    filtered_data = [item for item in MOCK_DATA if item['ott'] == ott_name]
    
    movies = sort_movies(filtered_data)
    
    # 템플릿에 현재 활성화된 OTT 정보를 전달
    return render_template('index.html', 
                           movies=movies, 
                           all_otts=ALL_OTTS, 
                           active_ott=ott_name)

if __name__ == '__main__':
    app.run(debug=True)