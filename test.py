import requests
import xml.etree.ElementTree as ET

def apiRequests(user,query,display,page) :
    # URL 설정
    url = f'https://www.law.go.kr/DRF/lawSearch.do?OC={user}&target=prec&type=XML&query={query}&display={display}&page={page}&search=2'

    # API 요청
    response = requests.get(url)
    xml_data = response.text

    return xml_data

def main() :
    # 설정
    USER    = "sjh0804_22" 
    QUERY   = "자동차"      
    DISPLAY = "20"         # 보여지는 검색결과 수
    page    = "1"          # 페이지 설정

    # XML 파싱
    root = ET.fromstring(apiRequests(USER,QUERY,DISPLAY,page))

    totalCnt = int(root.find('totalCnt').text) # 검색 결과 수
    max_page = round(totalCnt / int(DISPLAY))  # 마지막 페이지

    # 마지막 페이지까지 검색
    for page in range(max_page):
        root = ET.fromstring(apiRequests(USER,QUERY,DISPLAY,page))
        # 검색 결과에서 세부 정보 가져오기
        for prec in root.findall('prec') :
            print(prec.find('사건명').text)

if __name__ == "__main__":
    main()

