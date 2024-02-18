import hashlib
import json, os, requests
import time


## 驗證certificate.hash
def generate_hash(data):
    # Combine values into a single string
    combined_string = f"""{data["register"]["application_token"]}{data["register"]["position_uid"]}{data["register"]["inference_client_uid"]}"""

    # Create a hash object using SHA-256 (you can choose a different algorithm)
    # Get the hexadecimal representation of the hash
    hash_value = hashlib.sha256(combined_string.encode()).hexdigest()
    print("local_hash_value:", hash_value)
    return hash_value


## data_mgt
class Data_mgt:
    def __init__(self, file_name="config.json"):
        # 获取脚本所在目录
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # 构建文件路径
        self.json_file_path = os.path.join(self.script_dir, file_name)
        print(self.json_file_path)

    def read_json(self):
        with open(self.json_file_path, "r") as json_file:
            data = json.load(json_file)
        return data

    def write_json(self, data):
        with open(self.json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)


## interact with inference_layer
def send_register_request(data):
    # API endpoint for registration
    registration_endpoint = f"""{data["api_url"]}/certificate"""

    # Data to be sent in the POST request
    payload = {
        "application_token": data["register"]["application_token"],
        "inference_client_uid": data["register"]["inference_client_uid"],
        "position_uid": data["register"]["position_uid"]
    }
    print("Data to be sent:")
    print(json.dumps(payload, indent=2))

    try:
        # Make the POST request
        response = requests.post(registration_endpoint, json=payload)
        access_data = response.json()
        print("response_payload:", access_data)

        # Check the response status code
        if response.status_code == 200:
            print("status:", response.status_code, "<application_source_mgt>/<SourceCertificateHandler>/<certificate_issuing>")
            data["certificate_receiver"]["status"] = access_data.get('status')
            data["certificate_receiver"]["certificate"] = access_data.get('certificate')
            # data = check_identity(data)
        else:
            print("ERROR", response.status_code, "<certificate_issuing> Register")
            data["certificate_receiver"]["status"] = "error"

    except Exception as e:
        print(f"Error during registration: {e}")
    return data


## 驗證certificate是否有效
def check_identity(data):
    if data["certificate_receiver"]["status"] == "success":
        if data["certificate_receiver"]["certificate"][:64] == generate_hash(data):
            if int(data["certificate_receiver"]["certificate"][64:]) >=  int(time.time()):
                print("certificate is vaild")
                print("the diff between timeout_timestamp and current_time:", int(data["certificate_receiver"]["certificate"][64:]) - int(time.time()))
            else:
                print("Timeout, certificate is invaild")
                data["certificate_receiver"]["status"] = "error"
                print("the diff between timeout_timestamp and current_time:", int(data["certificate_receiver"]["certificate"][64:]) - int(time.time()))
                data = send_register_request(data)
        else:
            print("Invaild hash, certificate is invaild")
            data["certificate_receiver"]["status"] = "error"
    else:
        print("unregister, status error")
        data["certificate_receiver"]["status"] = "error"
    return data


data_mgt = Data_mgt()
if __name__ == "__main__":
    data = data_mgt.read_json()
    receive_certificate = send_register_request(data)
    data_mgt.write_json(receive_certificate)
    
    




