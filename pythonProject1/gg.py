alf = ["int",  # 1
       "long",  # 2
       "short",  # 3
       "double",  # 4
       "char|float",  # 5
       " |\n|\t|\r",  # 6
       "_|a-z|A-Z",  # 7
       "1-9",  # 8
       "0",  # 9
       ";",  # 10
       ",",  # 11
       "[",  # 12
       "]",  # 13
       "\0"  # 14
       ]
ER = -1
HA = -2

delta = [   #                   ' '  a-z  1-9 0  ;   ,   [   ]
            # 1   2   3   4   5   6  7    8   9  10  11  12  13  14
            [13, 10,  8, 15,  1,  0, ER, ER, ER,  0, ER, ER, ER, HA], # 0
            [ER, ER, ER, ER, ER,  2, ER, ER, ER, ER, ER, ER, ER, ER], # 1
            [17, 17, 17, 17, 17,  2,  3, ER, ER, ER, ER, ER, ER, ER], # 2
            [ER, ER, ER, ER, ER,  4,  3,  3,  3,  0,  2,  5, ER, ER], # 3
            [ER, ER, ER, ER, ER,  4, ER, ER, ER,  0,  2,  5, ER, ER], # 4
            [ER, ER, ER, ER, ER,  5, ER,  6, ER, ER, ER, ER, ER, ER], # 5
            [ER, ER, ER, ER, ER,  7, ER,  6,  6, ER, ER, ER, 12, ER], # 6
            [ER, ER, ER, ER, ER,  7, ER, ER, ER, ER, ER, ER, 12, ER], # 7
            [ER, ER, ER, ER, ER,  9, ER, ER, ER, ER, ER, ER, ER, ER], # 8
            [13, ER, ER, ER, ER,  9, ER, ER, ER, ER, ER, ER, ER, ER], # 9
            [ER, ER, ER, ER, ER, 11, ER, ER, ER, ER, ER, ER, ER, ER], # 10
            [13, ER, ER, 15, ER, 11,  3, ER, ER, ER, ER, ER, ER, ER], # 11
            [ER, ER, ER, ER, ER, 12, ER, ER, ER,  0,  2, 5 , ER, ER], # 12
            [ER, ER, ER, ER, ER, 14, ER, ER, ER, ER, ER, ER, ER, ER], # 13
            [17,  1,  1, 17, 17, 14,  3, ER, ER, ER, ER, ER, ER, ER], # 14
            [ER, ER, ER, ER, ER, 16, ER, ER, ER, ER, ER, ER, ER, ER], # 15
            [17,  1, 17, 17, 17, 16,  3, ER, ER, ER, ER, ER, ER, ER], # 16
            [3,  3,  3,  3,  3, ER,  3,  3, ER, ER, ER, ER, ER, ER], # 17
        ]
actions = [
           # 1  2  3  4  5  6  7  8  9  10 11 12 13 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 2
            [0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 2, 2, 0, 0], # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 9
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 10
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 13
            [1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0], # 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 15
            [1, 1, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],  # 16
            [1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0]  # 17
        ]

def search_name(name): #поиск дублируемого имени
    i=0
    while i < len(name):
        list = name.count(name[i])
        if list > 1:
            return 1
        i = i+1

def action(id_):
    global id_buf, buffer, hash_buf
    if id_ == 0:
        return 1
    if id_ == 1:
        id_buf += buffer
        print("id = ", id_buf)
        return 1
    if id_ == 2:
        hash_buf.append(id_buf)
        if search_name(hash_buf) == 1:
            return 0

        id_buf =""
        return 1
    return 0


def get_words(list_alf):# проверка букв
    if len(list_alf) == 3 and list_alf[1] == '-' and list_alf[0] <= text[k] and text[k] <= list_alf[2]:
        return 1
    else:
        return 0


def get_sub(str, start_index, len_list):
    end = start_index + len_list
    return str[start_index:end]

def get_alf_index(text):# сбор данных
    i=0
    global k, row, col, buffer
    while i < len(alf):
        ii=0
        list_alf = alf[i].split("|")
        while ii < len(list_alf):
            #print(list_alf[ii])
            len_list = len(list_alf[ii])

            if get_words(list_alf[ii]) == 1:
               buffer = text[k]
               k += 1
               col += 1
               return i
            sub = get_sub(text, k, len_list)
            if sub == list_alf[ii]:
                buffer = sub
                k += len_list
                col += len_list
                return i
            ii+=1
        i+=1
    else:
        print("Символа нет")
        return ER

def work(text):#oshibka
    global row, col, buffer
    state = 0

    while True:
        alf_index = get_alf_index(text)
        if buffer == '\n':
            row += 1
            col = 0
        if alf_index == ER:
            print("ERR! Неизвестная лексема или символ", row, ":", col)
            break
        state_next = delta[state][alf_index]

        if action(actions[state][alf_index]) == 0:
            print("ERR! Error name", row, ":", col)
            break

        state = state_next

        if state == ER:
            print("ERR!", row, ":", col)
            break
        if state == HA:
            print("Good")
            break
        print("buffer =", buffer)
        #break

fail_input = open('input.txt', 'r')
text = fail_input.read()+'\0'
k, row, col = 0 , 1 , 1
buffer =""
id_buf=""
hash_buf = []
work(text)
