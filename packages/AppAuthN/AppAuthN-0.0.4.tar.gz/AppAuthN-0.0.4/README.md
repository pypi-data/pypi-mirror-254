# AppAuthN

`AppAuthN` 是一個用於驗證 xApp 身份的 Python 模塊。

## 使用方法

1. 修改 AppAuthN/config.json 檔案：

    請確保替换自己的 Application 資訊
    ### "register": application_token、position_uid 和 inference_client_uid
    ### "raw_data": application_uid、position_uid、inference_client_uid 和 value
    ### "closed_loop": application_uid、position_uid 和 inference_client_uid

2. run AppAuthN/InferenceResult.py：

   ```bash
   python3 InferenceResult.py

# 注意事项

-請確保提供有效的输入，否則驗證可能會失败。