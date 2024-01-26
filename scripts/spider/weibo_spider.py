# scripts/spider

import requests
from bs4 import BeautifulSoup

def fetch_weibo_content():
  # 微博请求的URL和参数
  url = "https://weibo.com/ajax/statuses/mymblog?uid=5840080408&page=2&feature=0&since_id=4993321992454421kp2"
  params = {
    "uid": "5840080408",
    "page": 1,
    "feature": 0
  }

  # 用于请求的头部信息
  headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer": "https://weibo.com/u/5840080408",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "X-Xsrf-Token": "wRshDUWt_OpEuvkFJ4iJqf-c",
    "Cookie": "SINAGLOBAL=912869638359.6813.1697710139455; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh7bdwKck40wuI.BMIIyA.S5JpX5KMhUgL.Fo-cShM7eK-4eo.2dJLoIf2LxKqL1KqLBo5LxKqL1KMLBoqLxKBLB.zLBKeLxKML1KBLBo-LxK-LB-BL1K5LxKnL1-zL1hqLxKnL1K.LB-zLxK-L1h-L1h.LxKMLB.-LB.Bt; SCF=AtAS8Ui1iUt5xJACpuSK9NNprafl8bSgDInJr8QRvx3e8fcUyfIULlMTnYfVKRDLUdqM9BqlgWoZgQUkCQMK408.; ULV=1703342896265:4:1:1:9986963273412.73.1703342896263:1700148930727; XSRF-TOKEN=wRshDUWt_OpEuvkFJ4iJqf-c; ALF=1708888370; SUB=_2A25IsHRiDeRhGeNI71UR8SvFyTWIHXVrzImqrDV8PUJbkNAGLRf2kW1NSHPv20uAjDVpBOErYueoSlsfxx6rcwHm; WBPSESS=3v-qpO0mmLJXfcpbEMQPP69e6clsA8vJkSjyOErpzGjEYS6cpiv5s5UrUds3STE830GG76N_NSqDUFruYXq1Hv-bxnYUN7PLcYgh_fl72iRkgmqRaw8FqFe9VBYEtH3EzmH4WrccdgRNwopvZytMmg=="
  }

  response = requests.get(url, headers=headers, params=params)


  # 解析数据
  # ...

  # 检查请求是否成功
  if response.status_code == 200:
      data = response.json()
      print(data)  # 或者进行其他处理
  else:
      print("请求失败，状态码：", response.status_code)


def main():
  # 微博请求的URL和参数

  fetch_weibo_content()


if __name__ == "__main__":
  main()
