# python3
import sys

def BWT(text):
    result = []
    result.append(text)
    text_transformed = ""
    for i in range(0, len(text)-1):
        text = text[-1] + text[0:len(text)-1] #+ text[1]
        result.append(text)
    result.sort()
    for i in range(0, len(text)):
        text_transformed += result[i][-1]
    return text_transformed

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))