# def mental_protector(messages: list):
#     result = []
#     errormessage = ["ERROR", "ERR", "err", "error", "Error", "E", "e",
#                     "WARNING", "WARN", "Warn, warning", "Warning", "W", "w"]
#     for message in messages:
#         if message.split(":")[0][1:-1] in errormessage:
#             continue
#         result.append(message)
#     return result

def mental_protector(messages: list):
    result = []
    errormessage = ["ERROR", "ERR", "err", "error", "Error", "E", "e",
                    "WARNING", "WARN", "Warn", "warn", "warning", "Warning", "W", "w"]
    for message in messages:
        mes_type = message.split(":")[0][1:-1]
        if mes_type in errormessage:
            continue
        result.append(message)
    return result

print(mental_protector([
    "[Info]: Starting training process.",
    "[Warn]: Learning rate is low.",
    "[Info]: Invalid value.",
    "[Info]: Epoch 10 finished.",
    "[Err]: Out of memory.",
    "[Debug]: Checking tensor shapes."
]))