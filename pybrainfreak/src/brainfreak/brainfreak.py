def brainfreak(text):
    funcs = {}
    func_mode = False
    func_name = ""
    func_body = ""

    text = list(text)

    for i in range(len(text)):
        char = text[i]
        if func_mode:
            if char == "}":
                funcs[func_name[::-1]] = func_body
                func_mode = False
                func_body = ""
                func_name = ""
            else:
                func_body += char
            text[i] = "*"
            continue

        if char == "{":
            text[i] = "*"
            j = i - 1
            still_a_function_name = text[j] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890"
            while j != -1 and still_a_function_name:
                func_name += text[j]
                text[j] = "*"
                j -= 1
                still_a_function_name = text[j] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-1234567890"
            func_mode = True
        if char == "\\":
           if text[i:i+3] == list("\\\\\\"):
               text[0:i+3] = []
               break

    text = "".join(text)
    for func in funcs.keys():
        text=text.replace(func, funcs[func])

    return text
