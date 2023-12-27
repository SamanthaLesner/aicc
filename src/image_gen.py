import websocket
import json
import sys
import hashlib

host = '868dda56045d60c8ae.gradio.live'
last_message=""

def on_message(ws, message):
    # print("Received Message:")
    # print(message)
    # last_message = message
    global last_message
    last_message = message
    
def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    # print("### Closed ###")
    pass

def on_open(ws):
    # Send the first message
    first_message = json.dumps({"fn_index": 32, "session_hash": session_hash})
    ws.send(first_message)
    print("Sent:", first_message)

    # Read prompt from STDIN
    # prompt = sys.stdin.readline().strip()




    # Construct and send the second message
    second_message_data = [
        # prompt,
        input_string,
        "",
        ["Fooocus V2", "Fooocus Enhance", "Fooocus Sharp"],
        "Speed",
        "1024×1024 <span style=\"color: grey;\"> ∣ 1:1</span>",
        1,
        "2063888683916929300",
        2,
        4,
        "juggernautXL_version6Rundiffusion.safetensors",
        "None",
        0.5,
        "sd_xl_offset_example-lora_1.0.safetensors",
        0.1,
        "None",
        1,
        "None",
        1,
        "None",
        1,
        "None",
        1,
        False,
        "uov",
        "Disabled",
        None,
        [],
        None,
        "",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt"
    ]



    second_message = json.dumps({
        "data": second_message_data,
        "event_data": None,
        "fn_index": 32,
        "session_hash": session_hash
    })
    
    ws.send(second_message)
    
    print("Sent:", second_message)

if __name__ == "__main__":
    # Reading from STDIN and hashing
    input_string = sys.stdin.readline().strip()
    session_hash = hashlib.sha256(input_string.encode()).hexdigest()

    # WebSocket connection setup
    # websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://"+host+"/queue/join",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                header={
                                    "Pragma": "no-cache",
                                    #"Origin": "https://" + host ,
                                    "Accept-Language": "en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7",
                                    "Sec-WebSocket-Key": "u2O/a1GBsrr5Obq73BzSPA==",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                                    "Upgrade": "websocket",
                                    "Cache-Control": "no-cache",
                                    "Connection": "Upgrade",
                                    "Sec-WebSocket-Version": "13",
                                    # "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits"
                                })

    ws.run_forever()
    # print(last_message)
    data = json.loads(last_message)
    name_value = next((item['name'] for d in data['output']['data'] if d.get('visible') for item in d.get('value', []) if 'name' in item), None)
    print(f"https://{host}/file={name_value}")

# https://868dda56045d60c8ae.gradio.live/file=/tmp/gradio/12dae54d1e3a485f3ba580fcb16ef97332578d16/image.png