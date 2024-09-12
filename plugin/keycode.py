
#https://developer.android.google.cn/reference/android/view/KeyEvent

keycode_dict = {
    "KEYCODE_UNKNOWN": 0,
    "KEYCODE_HOME": 3,
    "KEYCODE_BACK": 4,
    "KEYCODE_CALL": 5,
    "KEYCODE_ENDCALL": 6,
    "KEYCODE_0": 7,
    "KEYCODE_1": 8,
    "KEYCODE_2": 9,
    "KEYCODE_3": 10,
    "KEYCODE_4": 11,
    "KEYCODE_5": 12,
    "KEYCODE_6": 13,
    "KEYCODE_7": 14,
    "KEYCODE_8": 15,
    "KEYCODE_9": 16,
    "KEYCODE_STAR": 17,
    "KEYCODE_POUND": 18,
    "KEYCODE_DPAD_UP": 19,
    "KEYCODE_DPAD_DOWN": 20,
    "KEYCODE_DPAD_LEFT": 21,
    "KEYCODE_DPAD_RIGHT": 22,
    "KEYCODE_VOLUME_UP": 24,
    "KEYCODE_VOLUME_DOWN": 25,
    "KEYCODE_CHANNEL_UP": 166,
    "KEYCODE_CHANNEL_DOWN": 167,
    "KEYCODE_ENTER": 66,
    "KEYCODE_OK": 23,
    "KEYCODE_MEDIA_PLAY": 126,
    "KEYCODE_MEDIA_PAUSE": 127,
    "KEYCODE_MEDIA_PLAY_PAUSE": 85,
    "KEYCODE_MEDIA_STOP": 86,
    "KEYCODE_MEDIA_NEXT": 87,
    "KEYCODE_MEDIA_PREVIOUS": 88,
    "KEYCODE_MUTE": 91,
    "KEYCODE_MENU": 82,
    "KEYCODE_APP_SWITCH": 187,
    "KEYCODE_TV_INPUT": 178,
    # Add more keycodes as needed
}

def find_keys(key=None, value=None):
    key_matches = []
    value_matches = []
    
    if key is not None:
        key = key.upper()
        for k in keycode_dict.keys():
            if key in k:
                key_matches.append(k)
        if key_matches:
            return ["{}=>{}".format(key,keycode_dict[key]) for key in key_matches]
        else:
            return ["Key not found"]
    elif value is not None:
        for k, v in keycode_dict.items():
            if v == value:
                value_matches.append(k)
        if value_matches:
            return ["{}=>{}".format(key,keycode_dict[key]) for key in value_matches]
        else:
            return ["Value not found"]
    else:
        return ["Please provide a key or a value"]
    
    

if __name__ == "__main__":
    # 根据键名查找值
    print(find_keys(key="vol"))  # 输出 [24, 25]
    print(find_keys(key="channel"))  # 输出 [166, 167]
    print(find_keys(key="enter"))  # 输出 [66]
    print(find_keys(key="ok"))  # 输出 [23]

    # 根据值查找键名
    print(find_keys(value=13))  # 输出 ['KEYCODE_6']
