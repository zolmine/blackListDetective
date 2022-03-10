from tracemalloc import start
from websocket import create_connection
from json import dumps,loads
import time
import os,sys
from concurrent.futures import ThreadPoolExecutor

from eth_abi import encode_single, encode_abi

executor = ThreadPoolExecutor(max_workers=4)
# url     = 'wss://polygon-mainnet.g.alchemy.com/v2/tGb32Cyl35DXFXXlOuJqbAAf6MbXPn0o'
url = 'wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws'


def getReserveInput(pairAddress,ws):
    allData = {"jsonrpc":"2.0","method":"eth_call","params":[{"to": pairAddress, "data":"0x0902f1ac"}, "latest"],"id":1}
    json_data = dumps(allData).encode("utf-8")
    ws.send(json_data)
    start = time.time() * 1000
    response = ws.recv()
    print(f"printing {(time.time() * 1000 - start)}")
    data = loads(response)
    if data["result"] != "0x":
        reserve = decodeReserve(data["result"])
        return (reserve)
    else:
        print("error reserve")
        return None
    

def getAmountInput(amountIn,fromAddress,toAddress):
    input1 = encode_single('(uint256,uint256,uint256,address,address)',(int(amountIn),64,2,fromAddress,toAddress))
    data =  '0xd06ca61f'+ input1.hex()
    return (data)

def decodeReserve(input):
    rererve0 = int(input[2:66],16)
    rererve1 = int(input[66:130],16)
    return(rererve0,rererve1)

def decodeGetAmountWith2PathOnly(input):
    amountOut = int(input[194:258],16)
    return(amountOut)

def getAmountInput(amountIn,fromAddress,toAddress,routerAddress,id):
    input = encode_single('(uint256,uint256,uint256,address,address)',(int(amountIn),64,2,fromAddress,toAddress))
    data =  '0xd06ca61f'+ input.hex()
    allData = {"jsonrpc":"2.0","method":"eth_call","params":[{"to": routerAddress, "data":data}, "latest"],"id":id}
    return (allData)

try:
    
    ws = create_connection(url)
    print("connected")


    print ("test for GetAmount")
    time1 = time.time() * 1000
    # ws = create_connection(url)
    # print("connected")
    filtre = getAmountInput(100000000000000000,"0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0xc2132D05D31c914a87C6611C10748AEb04B58e8F","0xa5e0829caced8ffdd4de3c43696c57f7d7a678ff",1)
    # filtre = {'jsonrpc': '2.0', 'method': 'eth_call', 'params': [{'to': '0xa5e0829caced8ffdd4de3c43696c57f7d7a678ff', 'data': '0xd06ca61f000000000000000000000000000000000000000000000000016345785d8a0000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000d500b1d8e8ef31e21c99d1db9a6444d3adf1270000000000000000000000000c2132d05d31c914a87c6611c10748aeb04b58e8f'}, 'latest'], 'id': 1}
    json_data = dumps(filtre).encode("utf-8")
    ws.send(json_data)
    response = ws.recv()
    # print (response)
    data = loads(response)
    reserve = decodeGetAmountWith2PathOnly(data["result"])
    print ("amountOut :",reserve)

    print((time.time() * 1000) - time1)
    # print (response)



    print ("test for  reserve")
    time1 = time.time() * 1000
    # ws = create_connection(url)
    # print("connected")
    reserve = getReserveInput("0x6E53cB6942e518376E9e763554dB1A45DDCd25c4",ws)
    print ("reserve0 :",reserve[0])
    print ("reserve1 :",reserve[1])
    print((time.time() * 1000) - time1)
    # print (response)




except Exception as err:

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(str([exc_type,fname,exc_tb.tb_lineno,err]))
    