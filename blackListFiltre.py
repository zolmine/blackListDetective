from shared_memory_dict import SharedMemoryDict
from json import dump,loads,dumps
from time import sleep, time
from collections import Counter

array = [{
    'hash': '0x3ffb24e1db8886a407a8e3b38467a0163b14bad555c73a2116f50173da4729ff',
    'from': '0xa7da8cf841ab1088820f792aee83304a4c90398f',
    'time': 1645366690789.893
}, {
    'hash': '0x78ec646578db57a9df9d955aec7ca51f90f57cf2cbfb8fad80b61c5241c0753e',
    'from': '0xa7da8cf841ab1088820f792aee83304a4c90398f',
    'time': 1645366695803.076
}, {
    'hash': '0x766f00187d660fcddac742fb6cd71c7e48beb37bb7f56ab4c235f7f1a067bed1',
    'from': '0xa7da8cf841ab1088820f792aee83304a4c90398f',
    'time': 1645366700813.049
}, {
    'hash': '0x62b7cfeeb85add4b5958c535c488deadbcee28df0fa33d5c217052531347d514',
    'from': '0x73a23b799434a21a407106d95b0aeeda8c6b3409',
    'time': 1645366705828.155
}, {
    'hash': '0x51c1454f89582a28c14465e5498cfdbae389e35f5b9c6702c43e080f5ba4f547',
    'from': '0x73a23b799434a21a407106d95b0aeeda8c6b3409',
    'time': 1645366710833.136
}]

counts = dict(Counter(sub for sub in array))

print(counts)
# freqs = Counter(frozenset(sub) for sub in array)
# print(freqs)
# for key in parsed:
#     print("Key: {} | Count: {}".format(key, len(parsed[key])))


# result = dict((i["from"], array.count(i)) for i in array)

# jsonMemory = SharedMemoryDict(name="blackList", size=2048)
# file = "logs.json"
# f = open(file)
# while True:
  
    # sleep(60)
    # array = list(loads(dumps(jsonMemory["comingData"]).encode("utf-8")))
    # w = open(file, 'w')

    # jsonMemory["comingData"] = ""
