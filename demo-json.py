import json
import os

class User:
	def __init__(self, username, passwd, email):
		self.username = username
		self.passwd = passwd
		self.email = email


class UserRepo:
	def __init__(self):
		self.users = []
		self.isLoggedIn = False
		self.currentUser = {}

		# load users from .json file
		self.loadUsers()

	def loadUsers(self):
		if os.path.exists("users.json"):
			with open("users.json",encoding="utf-8") as file:
				users = json.load(file)
				for user in users:
					user = json.loads(user)
					newUser = User(user["username"],user["passwd"],user["email"])
					self.users.append(newUser)
				print(self.users)

	def register(self,user: User):
		self.users.append(user)
		self.savetoFile()
		print("Kullanıcı oluşturuldu")

	def logout(self):
		self.isLoggedIn = False
		self.currentUser = {}
		print("Çıkış yapıldı.")

	def login(self,username,passwd):
		if self.isLoggedIn:
			print("halihazırda giriş yapıldı")
		else:
			for user in self.users:
				if user.username == username and user.passwd == passwd:
					self.isLoggedIn = True
					self.currentUser = user
					print("Başarılı giriş yapıldı.")
					break
	
	def identity(self):
		if self.isLoggedIn:
			print(f"username: {self.currentUser.username}")
		else:
			print("giriş yapılmadı")

	def savetoFile(self):
		list = []

		for user in self.users:
			list.append(json.dumps(user.__dict__))

		with open("users.json","w",encoding="utf-8") as file:
			json.dump(list, file)


repo = UserRepo()

while True:
	print("Menü".center(50,"*"))
	secim = input("1- Register\n2- Login\n3 - Logout\n4- Identity\n5- Exit\nSeciminiz:  ")
	if secim == "5":
		break
	else:
		if secim == "1":
			username = input("username: ")
			passwd = input("password: ")
			email = input("email: ")

			user = User(username,passwd,email)
			repo.register(user)

			print(repo.users)

		elif secim == "2":
			if repo.isLoggedIn:
				print("halihazırda oturumunuz açık")
			else:
				username = input("username: ")
				passwd = input("password: ")

			repo.login(username,passwd)
		elif secim == "3":
			repo.logout()
		elif secim == "4":
			repo.identity()
		else:
			print("Geçersiz seçim.")
