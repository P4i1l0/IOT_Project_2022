from cgi import parse_multipart
from tkinter import *
from PIL import ImageTk,Image
import requests

state = [False, False, False, False, False, False, False, False, False]
max_num = 8
url = 'http://58.122.59.104/iot'

class App():
    def __init__(self):
        self.window = Tk()
        self.window.title('어라운드스터디카페 숙대점')
        self.window.resizable(width=False, height=False)
        self.window.geometry("1080x720")

        self.main()
        self.window.mainloop()

    def main(self):
        self.container1 = Label(self.window, text='이용문의 010-0101-0101', fg='black', font=('Malgun Gothic', 16, 'bold'))
        self.container1.place(x=10, y=10)

        self.img = ImageTk.PhotoImage(Image.open('./bg.png').resize((300, 300)))
        self.container2 = Label(self.window, image=self.img)
        self.container2.place(x=390, y=60)

        self.container3 = Label(self.window, text='Sunrin', font=('Malgun Gothic', 30, 'bold'))
        self.container3.place(x=480, y=370)

        self.container4 = Label(self.window, text='어라운드스터디카페 숙대점', font=('Malgun Gothic', 20, 'bold'))
        self.container4.place(x=380, y=440)

        self.container5 = Button(self.window, text='1회 시간', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.payment)
        self.container5.place(x=150, y=550)

        self.container6 = Button(self.window, text='기간권', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.payment)
        self.container6.place(x=350, y=550)

        self.container7 = Button(self.window, text='정액권', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.payment)
        self.container7.place(x=520, y=550)

        self.container8 = Button(self.window, text='사물함\n이용권', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.payment)
        self.container8.place(x=690, y=525)

        self.container9 = Button(self.window, text='퇴장', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.payment_end)
        self.container9.place(x=860, y=550)

    def payment(self):
        self.items = []
        self.container1.place_forget()
        self.container2.place_forget()
        self.container3.place_forget()
        self.container4.place_forget()
        self.container5.place_forget()
        self.container6.place_forget()
        self.container7.place_forget()
        self.container8.place_forget()
        self.container9.place_forget()
        self.items.clear()

        self.item_container1 = Label(self.window, width=140, height=35, relief='solid')
        self.item_container1.place(x=50, y=50)
        self.item_container2 = Button(self.window, text='뒤로가기', relief='solid', font=('Malgun Gothic', 16, 'bold'), command=self.item_container2_command)
        self.item_container2.place(x=480, y=600)

        self.item1 = Button(self.item_container1, text='[1] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item1_command)
        self.items.append(self.item1)
        self.item2 = Button(self.item_container1, text='[2] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item2_command)
        self.items.append(self.item2)
        self.item3 = Button(self.item_container1, text='[3] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item3_command)
        self.items.append(self.item3)
        self.item4 = Button(self.item_container1, text='[4] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item4_command)
        self.items.append(self.item4)
        self.item5 = Button(self.item_container1, text='[5] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item5_command)
        self.items.append(self.item5)
        self.item6 = Button(self.item_container1, text='[6] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item6_command)
        self.items.append(self.item6)
        self.item7 = Button(self.item_container1, text='[7] 2인실', height=3, bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item7_command)
        self.items.append(self.item7)
        self.item8 = Button(self.item_container1, text='[8] 4인실', height=8, bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item8_command)
        self.items.append(self.item8)
        
        for i, val in enumerate(self.items):
            if state[i]:
                val.config(bg='green', state=DISABLED)
            else:
                val.config(bg='white', state=NORMAL)

        self.item1.place(x=20, y=220)
        self.item2.place(x=20, y=320)
        self.item3.place(x=20, y=420)
        self.item4.place(x=400, y=20)
        self.item5.place(x=400, y=120)
        self.item6.place(x=400, y=220)
        self.item7.place(x=400, y=320)
        self.item8.place(x=780, y=20)

    def payment_end(self):
        self.items = []
        self.container1.place_forget()
        self.container2.place_forget()
        self.container3.place_forget()
        self.container4.place_forget()
        self.container5.place_forget()
        self.container6.place_forget()
        self.container7.place_forget()
        self.container8.place_forget()
        self.container9.place_forget()
        self.items.clear()

        self.item_container1 = Label(self.window, width=140, height=35, relief='solid')
        self.item_container1.place(x=50, y=50)
        self.item_container2 = Button(self.window, text='뒤로가기', relief='solid', font=('Malgun Gothic', 16, 'bold'), command=self.item_container2_command)
        self.item_container2.place(x=480, y=600)

        self.item1 = Button(self.item_container1, text='[1] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item1_command)
        self.items.append(self.item1)
        self.item2 = Button(self.item_container1, text='[2] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item2_command)
        self.items.append(self.item2)
        self.item3 = Button(self.item_container1, text='[3] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item3_command)
        self.items.append(self.item3)
        self.item4 = Button(self.item_container1, text='[4] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item4_command)
        self.items.append(self.item4)
        self.item5 = Button(self.item_container1, text='[5] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item5_command)
        self.items.append(self.item5)
        self.item6 = Button(self.item_container1, text='[6] 1인실', bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item6_command)
        self.items.append(self.item6)
        self.item7 = Button(self.item_container1, text='[7] 2인실', height=3, bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item7_command)
        self.items.append(self.item7)
        self.item8 = Button(self.item_container1, text='[8] 4인실', height=8, bg='white', relief='solid', font=('Malgun Gothic', 24, 'bold'), command=self.item8_command)
        self.items.append(self.item8)
        
        for i, val in enumerate(self.items):
            if state[i]:
                val.config(bg='green', state=NORMAL)
            else:
                val.config(bg='white', state=DISABLED)

        self.item1.place(x=20, y=220)
        self.item2.place(x=20, y=320)
        self.item3.place(x=20, y=420)
        self.item4.place(x=400, y=20)
        self.item5.place(x=400, y=120)
        self.item6.place(x=400, y=220)
        self.item7.place(x=400, y=320)
        self.item8.place(x=780, y=20)

    def item1_command(self):
        state[0] = not state[0]
        self.Complete()

    def item2_command(self):
        state[1] = not state[1]
        self.Complete()

    def item3_command(self):
        state[2] = not state[2]
        self.Complete()

    def item4_command(self):
        state[3] = not state[3]
        self.Complete()

    def item5_command(self):
        state[4] = not state[4]
        self.Complete()

    def item6_command(self):
        state[5] = not state[5]
        self.Complete()

    def item7_command(self):
        state[6] = not state[6]
        self.Complete()

    def item8_command(self):
        state[7] = not state[7]
        self.Complete()

    def Complete(self):
        len_person = len([i for i in state if i])
        params = {'title':'어라운드스터디카페 숙대점','len_person':len_person, 'max_person':max_num, 'x':37.567352278741836, 'y':126.96415512413726}
        res = requests.get(url=url, params=params)
        print(res.text)

        self.canv = Label(self.window, width=50, height=15, relief='solid')
        self.canv.place(x=350, y=200)
        self.canv_item1 = Label(self.canv, text='완료되었습니다', width=30, height=5, relief='solid', font=('Malgun Gothic', 11, 'bold'))
        self.canv_item1.place(x=40, y=20)
        self.canv_item2 = Button(self.canv, text='확인', relief='solid', font=('Malgun Gothic', 20, 'bold'), command=self.canv_item2_command)
        self.canv_item2.place(x=135, y=140)

    def canv_item2_command(self):
        self.canv.place_forget()
        self.canv_item1.place_forget()
        self.canv_item2.place_forget()

        self.item_container2_command()

    def item_container2_command(self):
        self.item_container1.place_forget()
        self.item_container2.place_forget()
        self.item1.place_forget()
        self.item2.place_forget()
        self.item3.place_forget()
        self.item4.place_forget()
        self.item5.place_forget()
        self.item6.place_forget()
        self.item7.place_forget()
        self.item8.place_forget()
        self.main()

if __name__ == '__main__':
    app = App()