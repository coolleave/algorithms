"""
爬取蓝桥杯题
"""

import requests

# url = "https://www.lanqiao.cn/api/v2/problems/pc/?page_size=20&first_category_id=1&sort=difficulty&asc=1&page=3"
# res = requests.get(url)
import requests
import pandas as pd
import time

# 创建一个空的DataFrame来存储所有数据
all_data = pd.DataFrame()

# 遍历不同的页面
for page in range(200, 320):  # 假设你想要爬取前5页的数据
    url = f"https://www.lanqiao.cn/api/v2/problems/pc/?page_size=20&first_category_id=1&sort=difficulty&asc=1&page={page}"
    res = requests.get(url)

    # 确保请求成功
    if res.status_code == 200:
        # 将JSON数据转换为DataFrame
        data = res.json()
        df = pd.DataFrame(data['data'])

        # 将当前页的数据追加到all_data中
        all_data = pd.concat([all_data, df], ignore_index=True)
    else:
        print(f"请求失败，状态码：{res.status_code}")
    print(f"{page}已经完成")
    time.sleep(0.5)

# 将所有数据保存为Excel文件
all_data.to_excel('200-320页.xlsx', index=False, engine='openpyxl')

print("所有页面的数据已成功保存到Excel文件中")
