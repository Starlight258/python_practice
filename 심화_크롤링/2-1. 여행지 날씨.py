import requests
import json
# 이탈리아 로마 날씨
lat = 41.8905  # 위도
lon = 12.4942  # 경도
apikey = "789742d4d69e0beb19968160b547475f"
api = f"""http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apikey}"""

result = requests.get(api)

# json파일로 만들기
data = json.loads(result.text)

print("제가 여행가고싶은 여행지의 대기 성분을 알려드립니다.")
print("이탈리아 로마의 날씨입니다")
print("일산화탄소(CO) 농도는", data["list"][0]["components"]["co"], "입니다.")
print("산화질소(NO) 농도는",  data["list"][0]["components"]["no"], "입니다.")
print("이산화질소(NO2) 농도는",  data["list"][0]["components"]["no2"], "입니다.")
print("오존(O3) 농도는",  data["list"][0]["components"]["o3"], "입니다.")
