import time
import json, requests

class Counter:
    def __init__(self):
        self.value = int(time.time())

    def get_value(self):
        int(time.time())-self.value
        print("now.time", int(time.time()), "before.time", self.value)
        print(int(time.time())-self.value)
        return (int(time.time())-self.value)

    def reset(self):
        self.value = int(time.time())

# 在這裡創建一個全局計數器變數
global_counter = Counter()

def send_closed_loop(data):

    # API endpoint for closed_loop
    closed_loop_endpoint = f"""{data["api_url"]}/closed_loop"""

    data["closed_loop"]["value"] = global_counter.get_value()
    payload = {
        "application_uid": data["closed_loop"]["application_uid"],
        "position_uid": data["closed_loop"]["position_uid"],
        "packet_uid": data["closed_loop"]["packet_uid"],
        "inference_client_uid": data["closed_loop"]["inference_client_uid"],
        "value": data["closed_loop"]["value"]
    }
    print("Data to be sent:")
    print(json.dumps(payload, indent=2))

    try:
        # Make the POST request
        response = requests.post(closed_loop_endpoint, json=payload)
        access_data = response.json()
        print("response_payload:", access_data)

        # Check the response status code
        if response.status_code == 200:
            print("status:", response.status_code, "<closed_loop_data>/<ClosedLoopHandler>/<closed_loop_data_receiving>")
        else:
            print("ERROR", response.status_code, "<closed_loop_data_receiving>")

    except Exception as e:
        print(f"Error during registration: {e}")
    return data

