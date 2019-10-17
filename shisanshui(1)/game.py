import tkinter as tk
import pickle
from tkinter import messagebox
import urllib.request
import json
import tkinter.messagebox 
import pk
from PIL import Image, ImageTk
import requests
class Game():

	def __init__(self,s,s1):
		self.root=tk.Tk();
		self.id=s1
		self.token=s
		self.create()
		#self.root.mainloop()	
	
	def create(self):
		def ppk():
			self.root.destroy()
			pk.Pk(self.token,self.id)

		def rank():
			url4='https://api.shisanshui.rtxux.xyz/rank'
			headers4 = {'Content-Type': 'application/json'}
			Body4={}
			rr = requests.get(url=url4, json=Body4, headers=headers4)
			rank_li=rr.json()
			#print(rank_li)
			root_rank = tk.Toplevel(self.root)
			root_rank.geometry('270x500')
			root_rank.title('排行榜')
			theLB = tk.Listbox(root_rank,height=24,width=33)
			theLB.place(x=20,y=30)
			num=0
			paiming= tk.Label(root_rank,text='排名')
			paiming.place(x=15,y=8)
			idd= tk.Label(root_rank,text='id')
			idd.place(x=65,y=8)
			jifen= tk.Label(root_rank,text='积分')
			jifen.place(x=110,y=8)
			name= tk.Label(root_rank,text='姓名')
			name.place(x=170,y=8)
			for item in rank_li:
				num+=1
				theLB.insert("end", str(num).ljust(11)+str(item['player_id']).ljust(11)+str(item['score']).ljust(11)+item['name'].ljust(11))

		def history():
			url5= 'https://api.shisanshui.rtxux.xyz/history'
			headers5 = {"X-Auth-Token":self.token}
			params5={"player_id":self.id,"limit":15,"page":0}
			rrr=response=requests.get(url5,params=params5,headers=headers5)
			hh=rrr.json()
	
			hhh=hh['data']
			
			root_rank = tk.Toplevel(self.root)
			root_rank.geometry('550x500')
			root_rank.title('历史战绩')
			theLB = tk.Listbox(root_rank,height=24,width=73)
			theLB.place(x=20,y=30)
			num=0
			paiming= tk.Label(root_rank,text='战局id')
			paiming.place(x=15,y=8)
			idd= tk.Label(root_rank,text='手牌')
			idd.place(x=100,y=8)
			jifen= tk.Label(root_rank,text='得分')
			jifen.place(x=400,y=8)
			name= tk.Label(root_rank,text='timestamp')
			name.place(x=440,y=8)
			for i in hhh:
				s=''
				s+=str(i['id']).ljust(11)
				if len(i['card']) == 1:
					s +=i['card'][0]+'(特殊牌型)'
				else :
					for j in i['card']:
						s+='"'+j+'"   '
				s+=str(i['score']).center(10)
				s+=str(i['timestamp']).ljust(11)
				theLB.insert("end", s)
		



		self.root.title('福建十三水')
		self.root.geometry('1280x720')
		#背景创建
		canvas =tk.Canvas(self.root,width = 1280, height =720)

		img1= Image.open('IMA/12345.png')
		#global photo1
		#photo1 = ImageTk.PhotoImage(img1)

		image1 = tk.PhotoImage(file='IMA/grd.gif')
		canvas.create_image(0,0,anchor = 'nw',image= image1)
		canvas.pack()


		button_img_gif=tk.PhotoImage(file = 'IMA/start.gif')
		global star_login
		star_login =tk.Button(self.root, image =button_img_gif ,relief="flat",text = '带图按钮',command=ppk)
		star_login.place(x = 460,y = 300)


		#paihangbang
		button_img1_gif=tk.PhotoImage(file = 'IMA/rank.gif')
		star_rank =tk.Button(self.root,image =button_img1_gif,relief="flat",command=rank)

		star_rank.place(x=400,y=450)

		button_img2_gif=tk.PhotoImage(file = 'IMA/history.gif')
		star_his =tk.Button(self.root, image =button_img2_gif,relief="flat",command=history)
		star_his.place(x=650,y=450)

		self.root.mainloop()



