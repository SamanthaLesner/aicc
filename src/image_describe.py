import sys
import json
import base64
import requests


url_prefix = 'https://868dda56045d60c8ae.gradio.live'

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def send_image_to_api(image_base64):
    url = url_prefix + '/run/predict'
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7',
        'DNT': '1',
        'Origin': url_prefix + '',
        'Referer': url_prefix + '/?',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    data = json.dumps({
        "data": ["Photograph", f"data:image/png;base64,{image_base64}"],
        "event_data": None,
        "fn_index": 36,
        "session_hash": "dmxzu5nw6ab"
    })

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    image_base64 = encode_image_to_base64(image_path)
    result = send_image_to_api(image_base64)

    print(result)

if __name__ == "__main__":
    main()
