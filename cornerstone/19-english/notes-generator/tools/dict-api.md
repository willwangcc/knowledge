# Dictionary API 


## Why?

需要得到单词的各种信息，最简单的方法就是从API中读取，从 rapidAPI 网站，找到了排行第一的 Oxford Dictionaries API 来研究一下。

##  Oxford Dictionaries API Example 

```python
# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = 'beed99a1'
app_key = '33f531ce2353d5f73bedb9ee0f6175c6'

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
```

## Reference 

* [10 Best Dictionary APIs That You Should Be Using Right Now](https://blog.rapidapi.com/dictionary-apis/)
* [JSON在线阅读器](https://www.bejson.com/jsonviewernew/)
* [如何在命令行下优雅的查看JSON文件 | 利器](http://www.10tiao.com/html/568/201607/2650829408/1.html)