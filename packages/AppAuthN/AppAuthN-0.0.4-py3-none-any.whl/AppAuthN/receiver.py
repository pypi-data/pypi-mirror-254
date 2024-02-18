from flask import Flask, request, jsonify, make_response
from test_send_closed_loop import global_counter, send_closed_loop
from AppAuthN.test import api_url

app = Flask(__name__)

storage = {'status': None, 'certificate': {'hash': None, 'timestamp': None}}

@app.route('/certifcate_receiver', methods=['POST'])
def inference_result_receiver():
    response_data = request.json  # 從請求中獲取 JSON 數據
    if response_data.get('status') == "success":
        storage['status'] = response_data.get('status')
        storage['certificate']['hash'], storage['certificate']['timestamp'] = response_data.get('certificate')[1:-1].split('}{')
        print("status:", storage['status'])
        print("Certificate Hash:", storage['certificate']['hash'])
        print("Timestamp:", storage['certificate']['timestamp'])
        # If the value is accessed correctly, return a response with status code 200
        return make_response(jsonify({'status': 'success'}), 200)
    else:
        # If there's an issue, return a response with an appropriate status code
        return make_response(400, jsonify("Bad Request: Invalid argument (invalid request payload)."))



storage = {'inference_result': None}

@app.route('/result_receiver', methods=['POST'])
def inference_result_receiver():
    response_data = request.json  # 從請求中獲取 JSON 數據
    counts = global_counter.get_value()
    send_closed_loop(api_url, counts)
    if response_data.get('data_type') == "inference_result":
        storage['inference_result'] = response_data.get('value')
        print("inference_result:", storage['inference_result'])
        # If the value is accessed correctly, return a response with status code 200
        return make_response(jsonify({'status': 'success'}), 200)
    else:
        print("data_type:", response_data.get('data_type'))
        # If there's an issue, return a response with an appropriate status code
        return make_response(400, jsonify("Bad Request: Invalid argument (invalid request payload)."))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在端口 5000 上運行 Flask 應用程式

