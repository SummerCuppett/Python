# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/

# NumTranslateChinese.py

info=['零','一','二','三','四','五','六','七','八','九']
data=input("Please enter number:")
for i in range(len(data)):
     print(info[int(data[i])],end='')
