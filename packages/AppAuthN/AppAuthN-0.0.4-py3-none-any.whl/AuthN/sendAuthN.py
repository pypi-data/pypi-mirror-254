def input_authentication_code():
    while True:
        authentication_code = input("請輸入36位的認證碼: ")
        if len(authentication_code) == 36:
            return authentication_code
        print("輸入的認證碼無效，請重新輸入。")

if __name__ == "__main__":
    authentication_code = input_authentication_code()
    print("您輸入的認證碼是:", authentication_code)