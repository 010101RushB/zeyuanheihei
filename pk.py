import tkinter as tk
import pickle
from tkinter import messagebox
import urllib.request
import requests
import json
import game
import deal
from PIL import Image, ImageTk
#对战界面
canvas = None
photo0=None
class Pk():

	def __init__(self,s,s1):
		self.root=tk.Tk();
		self.id=s1
		self.token=s
		self.create()
		#self.root.mainloop()
	def create(self):
		def disc():
			
			
			discard.destroy()
			tk.messagebox.showinfo(title = 'Welcome',message='出牌成功')
			imglabel0.destroy()
			imglabel1.destroy()
			imglabel2.destroy()
			imglabel3.destroy()
			imglabel4.destroy()
			imglabel5.destroy()
			imglabel6.destroy()
			imglabel7.destroy()
			imglabel8.destroy()
			imglabel9.destroy()
			imglabel10.destroy()
			imglabel11.destroy()
			imglabel12.destroy()
			#调用出牌函数
			global star_login 
			star_login=tk.Button(self.root, image =play_image,command=start)
			star_login.place(x =565,y = 420)

		def start():
			head1={
				'Content-Type':'application/json',
				 'X-Auth-Token':self.token
			  }
			url1='https://api.shisanshui.rtxux.xyz/game/open'
			rr = requests.post(url=url1,headers=head1)
			global now
			now=rr.json()
			if now['status'] ==0:
				tk.messagebox.showinfo(title = 'Welcome',message='你的手牌是'+now['data']['card'])
				star_login.destroy()

				kkk=now['data']['card'].split(' ')
				for i in range(0,13):
					kkk[i]=kkk[i].replace('*','_')
				
				#显示手牌
				global photo00
				global imglabel00
				img00= Image.open('IMA/images/'+kkk[0]+'.jpg')
				photo00= ImageTk.PhotoImage(img00)
				imglabel00 = tk.Label(self.root,image=photo00)
				imglabel00.place(x=210,y=550)
				
				global photo01
				global imglabel01

				img01= Image.open('IMA/images/'+kkk[1]+'.jpg')
				photo01 = ImageTk.PhotoImage(img01)
				imglabel01 = tk.Label(self.root,image=photo01)
				imglabel01.place(x=280,y=550)

				global photo22
				global imglabel22
				img22= Image.open('IMA/images/'+kkk[2]+'.jpg')
				photo22 = ImageTk.PhotoImage(img22)
				imglabel22 = tk.Label(self.root,image=photo22)
				imglabel22.place(x=350,y=550)
			
				#zhongdun
				global photo33
				global imglabel33
				img33= Image.open('IMA/images/'+kkk[3]+'.jpg')
				photo33 = ImageTk.PhotoImage(img33)
				imglabel33 = tk.Label(self.root,image=photo33)
				imglabel33.place(x=420,y=550)
			
				global photo44
				global imglabel44
				img44= Image.open('IMA/images/'+kkk[4]+'.jpg')
				photo44 = ImageTk.PhotoImage(img44)
				imglabel44 = tk.Label(self.root,image=photo44)
				imglabel44.place(x=490,y=550)

				global photo55
				global imglabel55
				img55= Image.open('IMA/images/'+kkk[5]+'.jpg')
				photo55 = ImageTk.PhotoImage(img55)
				imglabel55 = tk.Label(self.root,image=photo55)
				imglabel55.place(x=560,y=550)
				
				global photo66
				global imglabel66
				img66= Image.open('IMA/images/'+kkk[6]+'.jpg')
				photo66 = ImageTk.PhotoImage(img66)
				imglabel66 = tk.Label(self.root,image=photo66)
				imglabel66.place(x=630,y=550)

				global photo77
				global imglabel77
				img77= Image.open('IMA/images/'+kkk[7]+'.jpg')
				photo77 = ImageTk.PhotoImage(img77)
				imglabel77 = tk.Label(self.root,image=photo77)
				imglabel77.place(x=700,y=550)
			
				#houdun
				global photo88
				global imglabel88
				img88= Image.open('IMA/images/'+kkk[8]+'.jpg')
				photo88 = ImageTk.PhotoImage(img88)
				imglabel88 = tk.Label(self.root,image=photo88)
				imglabel88.place(x=770,y=550)

				global photo99
				global imglabel99
				img99= Image.open('IMA/images/'+kkk[9]+'.jpg')
				photo99 = ImageTk.PhotoImage(img99)
				imglabel99 = tk.Label(self.root,image=photo99)
				imglabel99.place(x=840,y=550)

				global photo100
				global imglabel100
				img100= Image.open('IMA/images/'+kkk[10]+'.jpg')
				photo100 = ImageTk.PhotoImage(img100)
				imglabel100 = tk.Label(self.root,image=photo100)
				imglabel100.place(x=910,y=550)

				global photo111
				global imglabel111
				img111= Image.open('IMA/images/'+kkk[11]+'.jpg')
				photo111 = ImageTk.PhotoImage(img111)
				imglabel111 = tk.Label(self.root,image=photo111)
				imglabel111.place(x=980,y=550)

				global photo122
				global imglabel122
				img122= Image.open('IMA/images/'+kkk[12]+'.jpg')
				photo122 = ImageTk.PhotoImage(img122)
				imglabel122 = tk.Label(self.root,image=photo122)
				imglabel122.place(x=1050,y=550)

				tk.messagebox.showinfo(title = 'Welcome',message = '系统正在选择最佳牌型 ，耐心等候10~20秒' )
				kk=[]
				kk=deal.run(self.root,now['data']['card'],self.token,now['data']['id'])
				


				imglabel00.destroy()
				imglabel01.destroy()
				imglabel22.destroy()
				imglabel33.destroy()
				imglabel44.destroy()
				imglabel55.destroy()
				imglabel66.destroy()
				imglabel77.destroy()
				imglabel88.destroy()
				imglabel99.destroy()
				imglabel100.destroy()
				imglabel111.destroy()
				imglabel122.destroy()












				
				for i in range(0,13):
					kk[i]=kk[i].replace('*','_')
				#qiandun
				global photo0
				global imglabel0
				img0= Image.open('IMA/images/'+kk[0]+'.jpg')
				photo0 = ImageTk.PhotoImage(img0)
				imglabel0 = tk.Label(self.root,image=photo0)
				imglabel0.place(x=500,y=350)
				
				global photo1
				global imglabel1

				img1= Image.open('IMA/images/'+kk[1]+'.jpg')
				photo1 = ImageTk.PhotoImage(img1)
				imglabel1 = tk.Label(self.root,image=photo1)
				imglabel1.place(x=570,y=350)

				global photo2
				global imglabel2
				img2= Image.open('IMA/images/'+kk[2]+'.jpg')
				photo2 = ImageTk.PhotoImage(img2)
				imglabel2 = tk.Label(self.root,image=photo2)
				imglabel2.place(x=640,y=350)
			
				#zhongdun
				global photo3
				global imglabel3
				img3= Image.open('IMA/images/'+kk[3]+'.jpg')
				photo3 = ImageTk.PhotoImage(img3)
				imglabel3 = tk.Label(self.root,image=photo3)
				imglabel3.place(x=500,y=450)
			
				global photo4
				global imglabel4
				img4= Image.open('IMA/images/'+kk[4]+'.jpg')
				photo4 = ImageTk.PhotoImage(img4)
				imglabel4 = tk.Label(self.root,image=photo4)
				imglabel4.place(x=570,y=450)

				global photo5
				global imglabel5
				img5= Image.open('IMA/images/'+kk[5]+'.jpg')
				photo5 = ImageTk.PhotoImage(img5)
				imglabel5 = tk.Label(self.root,image=photo5)
				imglabel5.place(x=640,y=450)
				
				global photo6
				global imglabel6
				img6= Image.open('IMA/images/'+kk[6]+'.jpg')
				photo6 = ImageTk.PhotoImage(img6)
				imglabel6 = tk.Label(self.root,image=photo6)
				imglabel6.place(x=710,y=450)

				global photo7
				global imglabel7
				img7= Image.open('IMA/images/'+kk[7]+'.jpg')
				photo7 = ImageTk.PhotoImage(img7)
				imglabel7 = tk.Label(self.root,image=photo7)
				imglabel7.place(x=780,y=450)
			
				#houdun
				global photo8
				global imglabel8
				img8= Image.open('IMA/images/'+kk[8]+'.jpg')
				photo8 = ImageTk.PhotoImage(img8)
				imglabel8 = tk.Label(self.root,image=photo8)
				imglabel8.place(x=500,y=550)

				global photo9
				global imglabel9
				img9= Image.open('IMA/images/'+kk[9]+'.jpg')
				photo9 = ImageTk.PhotoImage(img9)
				imglabel9 = tk.Label(self.root,image=photo9)
				imglabel9.place(x=570,y=550)

				global photo10
				global imglabel10
				img10= Image.open('IMA/images/'+kk[10]+'.jpg')
				photo10 = ImageTk.PhotoImage(img10)
				imglabel10 = tk.Label(self.root,image=photo10)
				imglabel10.place(x=640,y=550)

				global photo11
				global imglabel11
				img11= Image.open('IMA/images/'+kk[11]+'.jpg')
				photo11 = ImageTk.PhotoImage(img11)
				imglabel11 = tk.Label(self.root,image=photo11)
				imglabel11.place(x=710,y=550)

				global photo12
				global imglabel12
				img12= Image.open('IMA/images/'+kk[12]+'.jpg')
				photo12 = ImageTk.PhotoImage(img12)
				imglabel12 = tk.Label(self.root,image=photo12)
				imglabel12.place(x=780,y=550)
				
				global discard
				discard=tk.Button(self.root,image =decard_image,command=disc)
				discard.place(x = 594,y = 300)
			else :
				tk.messagebox.showinfo(title = '哦吼',message = '网络可能出现了问题，再试一遍? ')
		def ret():
			 is_sign_up = tk.messagebox.askyesno('哦吼','你还在对战中，确定要退出吗?')
			 if is_sign_up:
				 self.root.destroy()
				 game.Game(self.token,self.id)

		self.root.title('福建十三水')
		self.root.geometry('1280x720')
		#背景创建
		canvas =tk.Canvas(self.root,width = 1280, height =720)
		image1 = tk.PhotoImage(file='IMA/gaming.gif')
		play_image= tk.PhotoImage(file='IMA/play.gif')
		decard_image= tk.PhotoImage(file='IMA/decard.gif')

		canvas.create_image(0,0,anchor = 'nw',image= image1)
		canvas.pack()
		button_img_gif=tk.PhotoImage(file = 'IMA/start.gif')
		global star_login 
		star_login =tk.Button(self.root, image =play_image ,command=start)#点击跳转到对战
		star_login.place(x = 565,y = 420)
		
		image_r = tk.PhotoImage(file='IMA/ret.gif')
		fanhui=tk.Button(self.root,text = '返回',image=image_r,command=ret)
		fanhui.place(x=0,y=0)

		self.root.mainloop()


