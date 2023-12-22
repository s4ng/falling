import os
import time

def main():
    read_file()
    while True:
        write()
        falling()
        time.sleep(0.05)
        clear()

def write():
    global text
    for i in range(0, len(text)):
        for j in range(0, len(text[i])):
            print(text[i][j], end = '')
        if i < len(text):
            print()

def clear():
    global line_size
    print('\033[' + str(line_size + 1) + 'A\033[2K', end='')

def falling():
    global text
    for i in range(len(text) - 1, -1, -1):
        for j in range(len(text[i]) - 1, -1, -1):
            if text[i][j] != ' ':
                if i + 1 < len(text):
                    if text[i + 1][j] == ' ':
                        text[i + 1][j] = text[i][j]
                        text[i][j] = ' '
                        continue
                    else:
                        if j + 1 < len(text[i]):
                            if text[i + 1][j + 1] == ' ':
                                text[i + 1][j + 1] = text[i][j]
                                text[i][j] = ' '
                                continue
                        if j - 1 >= 0:
                            if text[i + 1][j - 1] == ' ':
                                text[i + 1][j - 1] = text[i][j]
                                text[i][j] = ' '
                                continue

def read_file():
    global text
    global line_size
    terminal_size = os.get_terminal_size()
    column_size = terminal_size.columns
    line_size = terminal_size.lines - 1
    total_size = column_size * line_size
    fs = open('./falling.py', 'r')
    textStr = fs.read()
    text = []
    tmp = []
    for i in range(0, len(textStr)):
        if len(text) >= line_size:
            break
        if len(tmp) >= column_size:
            text.append(tmp)
            tmp = []
            continue
        if textStr[i] == '\n':
            for j in range(len(tmp), column_size):
                tmp.append(' ')
            text.append(tmp)
            tmp = []
            continue
        tmp.append(textStr[i])
    for i in range(len(text), line_size):
        for j in range(0, column_size):
            tmp.append(' ')
        text.append(tmp)
        tmp = []
    fs.close()

if __name__ == "__main__":
    main()
