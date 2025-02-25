# Task 1 Строки с заданным символом
def finder(text):
    result = ""
    for i in text:
        if i != '#':
            result += i
        else:
            result = result[:-1]
    return result


print(finder("a#bc#d"))
print(finder("abc#d##c"))
print(finder("abc##d######"))
print(finder("#######"))
print(finder(""))


# Task 2 Свечи
def svechi(candle_number, make_new):
    sjenie = candle_number
    leftov = candle_number
    while leftov >= make_new:
        new_candles = leftov // make_new
        sjenie += new_candles
        leftov = leftov % make_new + new_candles
    return sjenie


print(svechi(5, 2))
print(svechi(1, 2))
print(svechi(15, 5))
print(svechi(12, 2))
print(svechi(6, 4))
print(svechi(13, 5))
print(svechi(2, 3))


# Task 3 Подсчет количества букв
def bykvi(txt):
    reslt = ''
    schet_bykv = 0
    tek_bykv = ''
    for i in range(len(txt)):
        pred_bykv = tek_bykv
        tek_bykv = txt[i]
        if tek_bykv == pred_bykv:
            schet_bykv += 1
        else:
            reslt += pred_bykv
            if schet_bykv > 1:
                reslt += str(schet_bykv)
            schet_bykv = 1
    reslt += tek_bykv
    if schet_bykv > 1:
        reslt += str(schet_bykv)
    return reslt


print(bykvi("cccbba"))
print(bykvi("abeehhhhhccced"))
print(bykvi("aaabbceedd"))
print(bykvi("abcde"))
print(bykvi("aaabbdefffff"))
