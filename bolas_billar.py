import random
cant_result = 0
results = []
config = random.sample(set([1, 2, 3, 4, 5, 6]), 6)

def is_especular(config, results):
    for result in results:
        if is_first_line_especular(config, result) and is_second_line_especular(config, result) and is_third_line_especular(config, result):
            return True
    return False

def is_first_line_especular(config, result):
    return config[0] == result[2] and config[1] == result[1] and config[2] == result[0]

def is_second_line_especular(config, result):
    return config[3] == result[4] and config[4] == result[3]

def is_third_line_especular(config, result):
    return config[5] == result[5]

while cant_result < 4:
    if abs(config[0] - config[1]) == config[3] and abs(config[1] - config[2]) == config[4] and abs(config[3] - config[4]) == config[5]:
        if not config in results and not is_especular(config, results):
            cant_result += 1
            print(config)
            results.append(config)
    config = random.sample(set([1, 2, 3, 4, 5, 6]), 6)
# Funciona pero tengo que sacar las especulares

