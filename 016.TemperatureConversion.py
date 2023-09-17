# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
# temperatureConversion.py

print("||||||||||||||||||||||")
print("  CELSIUS TEMPERATURE CONVERTER  ")
print("||||||||||||||||||||||")
she = input('Please enter the temperature in Celsius：').strip('')


def is_number(s):  # 判断数字是否为浮点数
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


if is_number(she):
    she = float(she)  # 摄氏温度
    hua = she * 1.8 + 32  # 华氏温度
    kai = she + 273.15  # 开氏温度
    lie = she * 0.8  # 列氏温度
    lan = (she + 273.15) * 1.8  # 兰金温度

    print("Celsius：{:.2f}".format(she))
    print("Fahrenheit：{:.2f}".format(hua))
    print("Kelvin temperature：{:.2f}".format(kai))
    print("Lieutenant Temperature：{:.2f}".format(lie))
    print("Rankine temperature：{:.2f}".format(lan))
else:
    print("Wrong temperature entered！")
