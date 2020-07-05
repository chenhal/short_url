import requests
import urllib.parse
import re

headers = {
    'Cookie':
    'SUB=', #微博的Cookie中获取SUB
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Referer': 'https://www.weibo.com',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def get_short_url(long_url):
    url = "https://www.weibo.com/aj/v6/comment/add"

    payload = urllib.parse.urlencode({
        'mid': '', #测试微博评论的mid
        'content': long_url
    })
    response = requests.post(url, headers=headers, data=payload)

    try:
        data = response.json()['data']['comment']
        short_url = re.search(r'(https?)://t.cn/\w+', data).group(0)
        comment_id = re.findall(r'comment_id="(.+\d)"', data)[-1]
        print('微博短链：' + short_url)
        del_comment(comment_id)  # 如不需要删除评论，可以将该行注释
    except:
        pass


# 删除评论
def del_comment(comment_id):
    url = 'https://www.weibo.com/aj/comment/del'

    payload = urllib.parse.urlencode({
        'mid': '', #测试微博评论的mid
        'cid': comment_id
    })
    response = requests.post(url, headers=headers, data=payload)
    try:
        if response.json()['code'] == '100000':
            print('评论已删除')
    except:
        pass


if __name__ == '__main__':
    get_short_url(input('请输入长地址：'))

#函数暂停
os.system("pause")