import twitter

t =  twitter.Twitter(OAuth("4487244372-0x1nCnyKbvB8bECb3prKqnWaGOrvsAx7RTXbtST", "f8fbbgeRQMHSfdYIGZs9Iw5SpvzsWm5e2cOsoEWBUPYGa", "REXcjh2T7GF0xohdfw5Is9SgT", "6pRMQiAXZ09Rc9uQ2Zjy3FiXnmZXTpxpATWAV6C6PU5vnMw14X"))
pythonTweets = t.search.tweets(q = "#python")
print pythonTweets