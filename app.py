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
        "desc": "전역 후 다시 떠난, 예고 없이 시작된 지민과 정국의 두 번째 예측불가 우정 여행",
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
        "id": 6,
        "title": "이 사랑 통역 되나요?",
        "date": "2026-01-16",
        "ott": "Netflix",
        "poster": "lovetrans.jpg",
        "cast": "김선호, 고윤정, 후쿠시 소타",
        "desc": "촬영차 전 세계를 오가는 스타 배우와 그녀의 통역사. 서로를 향한 마음이 깊어지는 것과 달리 설렘의 감정은 자꾸만 오역이 되는데. 과연 둘만의 사랑의 언어를 찾을 수 있을까?",
        "link": "https://www.netflix.com/kr/title/81697769?preventIntent=true" 
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
        "id": 7,
        "title": "조각도시",
        "date": "2025-11-05 ~ 2025-12-03 수",
        "ott": "Disney+",
        "poster": "jogakdosi.jpg",
        "cast": "지창욱, 도경수, 김종수, 조윤수, 이광수",
        "desc": "평범한 삶을 살던 ‘태중’이 어느 날 억울하게 흉악한 범죄에 휘말려 감옥에 가게 되고, 모든 것은 ‘요한’에 의해 계획되었다는 것을 알게 되면서 그를 향한 복수를 실행하는 액션 드라마.",
        "link": "https://www.disneyplus.com/ko-kr/browse/entity-22e8ccc0-dae8-4171-89ff-342c004e66de?placement=searchEngine&distributionPartner=naver_kr"
    },
    {
        "id": 8,
        "title": "메이드 인 코리아 시즌 1",
        "date": "2025-12-24 ~ 2026-01-14 수",
        "ott": "Disney+",
        "poster": "madeinkorea.jpg",
        "cast": "현빈, 정우성, 우도환, 조여정, 서은수, 원지안, 정성일, 강길우, 노재원, 릴리 프랜키, 박용우",
        "desc": "1970년대 혼란과 도약이 공존했던 대한민국, 부와 권력의 정점에 오르기 위해 낮에는 중앙정보부 요원, 밤에는 위험한 비즈니스 맨으로 이중생활을 영위했던 한 사내와 그를 막아내기 위해 모든 것을 내던진 검사가 시대를 관통하는 거대한 사건과 직면하며 펼쳐지는 이야기.",
        "link": "https://www.disneyplus.com/ko-kr/browse/entity-5acf7909-5d2f-494e-91a9-2fe0555c220f"
    },
    {
        "id": 10,
        "title": "빌런즈",
        "date": "2025-12-18 ~ 2026-01-08 목",
        "ott": "TVING",
        "poster": "villains.jpg",
        "desc": "초정밀 위조지폐 슈퍼노트를 둘러싼 악인들의 피 튀기는 충돌과 대결을 그린 범죄 드라마",
        "cast": "유지태, 이민정, 이범수, 곽도원",
        "link": "https://www.tving.com/contents/E004106617" 
    },
    {
        "id": 11,
        "title": "친애하는 X",
        "date": "2025-11-06 ~ 2025-12-04 목",
        "ott": "TVING",
        "poster": "dearx.jpg",
        "desc": "지옥에서 벗어나 가장 높은 곳으로 올라가기 위해 가면을 쓴 여자 백아진 그리고 그녀에게 잔혹하게 짓밟힌 X들의 이야기",
        "cast": "김유정, 김영대, 김도훈, 이열음",
        "link": "https://www.tving.com/contents/E004454417" 
    },
    {
        "id": 6,
        "title": "",
        "date": "2026-02-01",
        "ott": "Wavve",
        "poster": "",
        "desc": "",
        "link": "https://www.wavve.com",
 
    },
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