import websocket
import json
import time

def on_message(ws, message):
    data = json.loads(message)
    current_price = float(data['k']['c'])
    open_price = float(data['k']['o'])
    percent_change = abs(current_price - open_price) / open_price * 100

    if percent_change >= 1:
        print(f"Price change: {percent_change}% in the last 60 minutes")
    else:
        print(f"Current price: {current_price}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    ws.send('{"method":"SUBSCRIBE","params":["ethusdt@kline_1m"],"id":1}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
