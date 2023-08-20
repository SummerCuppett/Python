# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
#  RGBtoHex.py

print('RGB Mode decimal color to hexadecimal color conversion'.center(55))
print('='*60)
def rgbhex(rgbr,rgbg,rgbb):
    return hex(int(rgbr)).replace('0x','')+hex(int(rgbg)).replace('0x','') +hex(int(rgbb)).replace('0x','')
r=input('Enter the R value of the RGB color value of the anchor point, the value range0--255 :')
g=input('Enter the R value of the RGB color value of the anchor point, the value range0--255 :')
b=input('Enter the R value of the RGB color value of the anchor point, the value range0--255 :')
print('The hexadecimal color value of the anchor point is:',rgbhex(r,g,b) )
