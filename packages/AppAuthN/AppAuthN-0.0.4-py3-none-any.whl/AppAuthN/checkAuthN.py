import uuid

def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False

def is_validate_input(device_id, application_token, position_id):
    # check application_token
    if not is_valid_uuid(application_token):
        print(f"application_token: {application_token} 不是有效的。")

    # check position_id
    if not is_valid_uuid(position_id):
        print(f"position_id: {position_id} 不是有效的。")

    # both application_token and position_id are valid
    if is_valid_uuid(application_token) and is_valid_uuid(position_id):
        print(f'''{{'device_id': '{device_id}', 'application_token': '{application_token}', 'position_id': '{position_id}'}}''')