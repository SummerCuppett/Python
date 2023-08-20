# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
#   ChineseID.py

dic={'11':'北京市','12':'天津市','13':'河北省','14':'山西省','15':'内蒙古自治区','22':'吉林省',
     '23':'黑龙江省','31':'上海市',  '32':'江苏省','33':'浙江省','35':'福建省','36':'江西省',
     '37':'山东省','41':'河南省','42':'湖北省','44':'广东省','45':'广西壮族自治区','46':'海南省',
     '50':'重庆市','51':'四川省','53':'云南省','54':'西藏自治区','61':'陕西省','62':'甘肃省',
     '63':'青海省','65':'新疆维吾尔自治区','71':'台湾省','81':'香港','82':'澳门'       }
def idget(str):
    newstr='' 
    if dic.get(str):
        newstr=dic[str]
    return newstr
instr=input('请输入您的身份证号:\n')

if instr[:16].isdigit()and len(instr) == 18:
    print('你来自:',idget(instr[0:2]))
    print('你的生日是:' + instr[6:10] + '年' +instr [10:12] + '月' + instr[12:14] + '日')
    gender = '女' if int(instr[16]) % 2 == 0 else '男'
    print('你的性别是:' + gender )
