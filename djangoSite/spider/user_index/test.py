from spider.Utils.loopRequest import LoopRequest
request = LoopRequest()

proxy = False

res = request.get('https://httpbin.org/get', proxy=False).content.decode('utf-8')

print(res)