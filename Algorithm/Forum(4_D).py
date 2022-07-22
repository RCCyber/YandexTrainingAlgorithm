"""
find a frequently discussed topic
"""
message = ['7',
           '0',
           'Олимпиада по информатике',
           'Скоро третья командная олимпиада?',
           '0',
           'Новая компьютерная игра',
           'Вышла новая крутая игра!',
           '1',
           'Она пройдет 24 ноября',
           '1',
           'В Санкт-Петербурге и Барнауле',
           '2',
           'Где найти?',
           '4',
           'Примет участие более 50 команд',
           '6',
           'Интересно, какие будут задачи'
           ]

num_dict = {}

for i in range(1, len(message)):
    if len(message[i]) == 1:
        if int(message[i]) == 0:
            print(message[i], message[i+1], message[i+2])
            num_dict[int(message[i])] = [message[i+1], message[i+2]]
        else:
            print(message[i], message[i + 1])
            num_dict[int(message[i])] = message[i + 1]
    else:
        print(message[i])

print(num_dict)
