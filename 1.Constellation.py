# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
#      1.Constellation.py 

sdate=[20,19,21,20,21,22,23,23,23,24,23,22]     # Constellation Judgment List
conts =['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius' ,'Capricorn']
signs=['♑','♒','♓','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑']

# Input birthday, output constellation
birth = input('Please enter your date of birth in the format:2001-02-21\n').strip(' ')
cbir=birth.split('-')    # split year month day into list
cmonth=str(cbir[1])      # Extract monthly data
cdate=str(cbir[2])       # Extract daily data
def sign(cmonth,cdate):  # Judgment constellation function
    if int(cdate)<sdate[int(cmonth)-1]:   # If the day data is earlier than the corresponding date in the corresponding month list
        print(conts[int(cmonth)-1])       # Directly output the constellation list corresponding to the constellation corresponding to the month
        print(signs[int(cmonth)-1])       # Directly output the constellation list corresponding to the constellation corresponding to the month
    else:
        print(conts[int(cmonth)])         # Otherwise, output the constellation list corresponding to the constellation in the next month
        print(signs[int(cmonth)])         # Otherwise, output the constellation list corresponding to the constellation in the next month       
sign(cmonth,cdate)      # Call the constellation judgment program
