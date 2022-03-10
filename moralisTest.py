from concurrent.futures import ThreadPoolExecutor
from websocket import  WebSocketApp
import rel
from json import dumps
url = "wss://speedy-nodes-nyc.moralis.io/02799b1f72329a0eefa3b741/polygon/mainnet/ws"

filtre = {"jsonrpc":"2.0","id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}
json_data = dumps(filtre).encode("utf-8")

rel.safe_read()

def manager(message):
    filtre = {"jsonrpc": "2.0","id": 0,"method": "eth_getTransactionByHash","params": ["0x867c87f120fefafdc3e34334a3b098d7d02fb7602fa00b9c316847a968301895"]}

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    ws.send(json_data)

def on_message(ws, message):
    ThreadPoolExecutor().submit(manager,message)

def on_open1(ws):
    print("Opened Second connection")
    

def on_message1(ws, message):
    print(message)

ws1 = WebSocketApp(url,on_open=on_open1,on_message=on_message1,on_error=on_error,on_close=on_close)
ws = WebSocketApp(url,on_open=on_open,on_message=on_message,on_error=on_error,on_close=on_close)

ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
ws1.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()