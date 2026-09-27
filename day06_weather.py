import requests
city = input("城市：") 
# 第 1 个请求：把"杭州"翻译成经纬度（地理编码 API）
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_resp = requests.get(geo_url, params={"name": city, "count": 1})
geo_data = geo_resp.json()          # 把返回的 JSON 文本变成 Python 字典

try:
    city_info = geo_data["results"][0]
except KeyError:
    print("找不到这个城市，请检查英文拼写")
    exit()

lat = city_info["latitude"]     # 直接用 try 里取好的结果
lon = city_info["longitude"]
print(f"城市坐标：{lat}, {lon}")

# 第 2 个请求：拿天气（天气预报 API）
w_url = "https://api.open-meteo.com/v1/forecast"
w_resp = requests.get(w_url, params={
    "latitude": lat,
    "longitude": lon,
    "current_weather": True
})
w_data = w_resp.json()
temp = w_data["current_weather"]["temperature"]
print(f"该城市当前气温：{temp}°C")