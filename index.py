from websocket import create_connection
from json import dumps,loads
from time import sleep, time
import os,sys
from concurrent.futures import ThreadPoolExecutor
from shared_memory_dict import SharedMemoryDict

executor = ThreadPoolExecutor(max_workers=4)
url     = 'wss://polygon-mainnet.g.alchemy.com/v2/tGb32Cyl35DXFXXlOuJqbAAf6MbXPn0o'
filtre = {"jsonrpc":"2.0","id": 0, "method": "eth_subscribe", "params": ["alchemy_filteredNewFullPendingTransactions", {"address": "0xa5e0829caced8ffdd4de3c43696c57f7d7a678ff"}]},{"jsonrpc":"2.0","id": 1, "method": "eth_subscribe", "params": ["alchemy_filteredNewFullPendingTransactions", {"address": "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"}]}
json_data = dumps(filtre).encode("utf-8")
jsonMemory = SharedMemoryDict(name="blackList", size=2048)
jsonMemory["comingData"] = ""
def dataFilter(data):
    try:
        data = loads(data)
        array = []
        if "params" in data:
            if data["params"]["result"]['from'] != "":
                toAppend = {
                    "hash": data["params"]["result"]['hash'],
                    "from" : data["params"]["result"]['from'],
                    "time" : time() * 1000
                }
                if jsonMemory["comingData"]:
                    array = list(loads(dumps(jsonMemory["comingData"]).encode("utf-8")))

                    array.append(toAppend)
                    jsonMemory["comingData"] = array
                else:
                    array.append(toAppend)
                    jsonMemory["comingData"] = array

            # print(jsonMemory["comingData"])

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(str([exc_type,fname,exc_tb.tb_lineno,err]))

try:
    
    ws = create_connection(url)

    print("connected")

    ws.send(json_data)

    while True:
        try:
            response = ws.recv()
            # args = response,ws
            
            executor.submit(dataFilter,response)
            sleep(5)
        except:
            continue

except Exception as err:

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(str([exc_type,fname,exc_tb.tb_lineno,err]))
    