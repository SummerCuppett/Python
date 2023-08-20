# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
# GameTenSecond.py

from tkinter import *
from tkinter.messagebox import *
import time
import random
root=Tk()
rans=[0.1,0.08,0.06,0.04]
count=0
start=False
def ten():                                           # game theme function
    global start                                    # Define the global variable start to record the game state
    global count                                     # Define the global variable count to record the number of seconds
    num=random.choice(rans)                         # Randomly generate intervals to increase game difficulty
    fight['text']='stop'                            
    if not start:                                    # if stop
        start=True
        while start:
            time.sleep(num)
            count+=0.2
            show['text']=format(count,'.1f')
            show.update()                             
        if show['text']==str(10.0):                # 如果等于10秒，即挑战成功
            warn=showwarning(title='10 second challenge', message='challenge is successful, all your consumption can be free！')
        else:
            warn=showwarning(title='10 second challenge', message='fail the challenge, you can receive a voucher！')
    else:
        start=False
        fight['text']='continue to challenge'
        count=0
root.title('10 second challenge')                                        #  Set the form title
root.wm_attributes('-topmost', 1)                            #  Set form to top
root.geometry('200x80')                                       #  set form size
root.resizable(width=False, height=False)                   #  Setting the size of the form cannot be changed
topic = Label(root, text='10 second challenge')                        #  Set the title of the game in the form
topic.pack()
show=Label(root,text=str(count))
show.pack()
fight=Button(root,text='start challenge',command=ten)
fight.pack()
mainloop()
