import requests, json
from AppAuthN.CloseLoopCounter import global_counter, send_closed_loop
from AppAuthN.CertificationReceiver import data_mgt, check_identity

## send rawdata to inference layer for receiving inference result
def send_rawdata(data):
    # API endpoint for inference_service
    inference_service_endpoint = f"""{data["api_url"]}/inference_service"""

    data["raw_data"]["packet_uid"] = str(int(data["raw_data"]["packet_uid"])+1)
    payload = {
        "application_uid": data["raw_data"]["application_uid"],
        "position_uid": data["raw_data"]["position_uid"],
        "packet_uid": data["raw_data"]["packet_uid"],
        "inference_client_uid": data["raw_data"]["inference_client_uid"],
        "value": data["raw_data"]["value"]
    }
    print("Data to be sent:")
    print(json.dumps(payload, indent=2))

    try:
        # Make the POST request
        global_counter.reset()
        response = requests.post(inference_service_endpoint, json=payload)
        # start a timer
        access_data = response.json()
        print("response_payload:", access_data)

        # Check the response status code
        if response.status_code == 200:
            data = send_closed_loop(data)
            print("status:", response.status_code, "<inference_exe>/<InferenceServiceHandler>/<inference_service>")
            data["result_receiver"]["status"] = access_data.get('status')
            data["result_receiver"]["value"] = access_data.get('data')
        else:
            print("ERROR", response.status_code, "<inference_service>")
            data["certificate_receiver"]["status"] = "error"

    except Exception as e:
        print(f"Error during registration: {e}")
    return data


if __name__ == "__main__":
    data = data_mgt.read_json()
    print(data)
    data = check_identity(data)
    receive_result = send_rawdata(data)
    data_mgt.write_json(receive_result)