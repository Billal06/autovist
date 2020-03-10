import requests, asyncio, random, os
from sys import exit

class Visit:
	def __init__(self, target):
		self.url = target
		self.proxy_ = {}
		self.headers = {}
		self.p = False
		self.ua = False
		self.pilih = ""
		self.s_ua = ""

	async def set_proxy(self):
		if self.proxy_:
			del self.proxy_["http"]
			del self.proxy_["https"]
		else: pass
		d = []
		try:
			pr = open("data/proxy.txt", "r").read()
			for a in pr.splitlines():
				d.append(a)
			self.pilih = random.choice(d)
			self.proxy_["http"] = "http://"+self.pilih
			self.proxy_["https"] = "https://"+self.pilih
			self.p = True
		except IOError:
			print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mFile 'proxy.txt' not found, please add proxy in 'data/proxy.txt'\033[0m")
			exit()
	async def set_ua(self):
		if self.ua:
			del self.headers["User-Agent"]
		else: pass
		d = []
		try:
			data = open("data/ua.txt","r").read()
			for a in data.splitlines():
				d.append(a)
			self.s_ua = random.choice(d)
			self.headers["User-Agent"] = self.s_ua #random.choice(d)
			self.ua = True
		except IOError:
			print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mFile 'ua.txt' not found, please add User Agent in 'data/ua.txt'\033[0m")
			exit()

	def cek(self):
		try:
			r = requests.get(self.url)
			if r.status_code < 301 or r.status_code > 199: pass
			else:
				print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mPage not found\033[0m")
				exit()
		except requests.exceptions.MissingSchema:
			print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mPlease input 'protocol'\033[0m")
			exit()
		except requests.exceptions.InvalidURL:
			print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mURL error\033[0m")
			exit()
		except requests.exceptions.ConnectionError:
			print ("\033[33;1m[\033[31;1m×\033[33;1m] \033[31;1mConnection Error\033[0m")
			exit()

	async def gas(self, no):
		ss = requests.Session()
		ss.headers = self.headers
		print ("\033[33;1m[\033[32;1m!\033[33;1m] Using UA: \033[32;1m"+self.s_ua)
		try:
			r = ""
			if self.p == True:
				print ("\033[33;1m[\033[32;1m!\033[33;1m] Using Proxy: \033[32;1m"+self.pilih)
				ss.proxies = self.proxy_
				ss.verify = False
				ss.get(self.url)
			elif self.p == False:
				ss.get(self.url)
			print ("\033[33;1m[\033[32;1m"+no+"\033[33;1m] \033[32;1mTry -> success")
		except requests.exceptions.ProxyError:
			print ("\033[33;1m[\033[31;1m"+no+"\033[33;1m] Proxy Error -> skip")
		except requests.exceptions.InvalidProxyURL:
			print ("\033[33;1m[\033[31;1m"+no+"\033[33;1m] Proxy Error -> skip")
	def visit(self, no):
		asyncio.run(self.gas(no))

def about():
	print ("""
\033[37;1m# \033[35;1mINFO
\033[33;1mAuthor \033[31;1m:\033[32;1m Billal Fauzan
\033[33;1mVersion\033[31;1m:\033[32;1m 0.1
\033[33;1mLicense\033[31;1m:\033[32;1m MIT
\033[33;1mTeam   \033[31;1m:\033[32;1m Cyber Ghost ID and BLACK CODER CRUSH
\033[33;1mThanks \033[31;1m:\033[32;1m ALLAH SWT, and my masters

\033[37;1m# \033[35;1mFind Me On
\033[33;1mYoutube \033[31;1m:\033[32;1m https://m.youtube.com/channel/UCgMLygCASD8ec4ftaddgUZQ
\033[33;1mFacebook\033[31;1m:\033[32;1m https://facebook.com/billal.id.9
\033[33;1mWhatsApp\033[31;1m:\033[32;1m https://wa.me/6285xxxxxxxx

\033[37;1m## \033[35;1m        Copyright 2020 BILLAL FAUZAN        \033[37;1m##
""")
def banner():
	os.system("clear")
	ban = """
\033[32;1m     _         _     __     ___     _   
    / \  _   _| |_ __\ \   / (_)___| |_ 
   / _ \| | | | __/ _ \ \ / /| / __| __|
  / ___ \ |_| | || (_) \ V / | \__ \ |_ 
 /_/   \_\__,_|\__\___/ \_/  |_|___/\__|\033[33;1m
   Author\033[31;1m:\033[32;1m BILLAL\033[33;1m        Version\033[31;1m:\033[32;1m 0.1
"""
	return ban

def vist():
	print (banner())
	url = input("\033[33;1m[\033[31;1m?\033[33;1m] \033[35;1mTARGET: \033[32;1m")
	visit = Visit(url)
	visit.cek()
	jml = input("\033[33;1m[\033[31;1m?\033[33;1m] \033[35;1mTOTAL: \033[32;1m")
	p = input("\033[33;1m[\033[31;1m?\033[33;1m] \033[35;1mUSE PROXY \033[37;1m(Y/n): \033[32;1m")
	jml = int(jml) + int(jml)
	for a in range(jml):
		if p in ["Y", "y"]:
			asyncio.run(visit.set_proxy())
		else: pass
		asyncio.run(visit.set_ua())
		visit.visit(str(a))
#asyncio.run(index())
def index():
	os.system("clear")
	print (banner())
	print ("\033[33;1m[\033[32;1m1\033[33;1m]. \033[32;1mGo to tools")
	print ("\033[33;1m[\033[32;1m2\033[33;1m]. \033[32;1mAbout")
	print ("\033[33;1m[\033[32;1m3\033[33;1m]. \033[31;1mExit")
	i = input("\033[33;1m{\033[35;1m AUTO VIST\033[33;1m }>>\033[32;1m ")
	if i in ["1", "01"]:
		vist()
	elif i in ["2", "02"]:
		about()
	elif i in ["3", "03"]:
		sys.exit()
	else:
		index()
index()
