import requests
import json

class Github:
	def __init__(self):
		self.api_url = "https://api.github.com"
		self.token = "< Your Personal Access Token >"
		self.auth = {
		"Authorization": "token " + self.token
		}
		self.json = {
			"name": "test-repo",
			"description": "This is a OAuth App.",
			"homepage": "https://github.com",
			"private": False,
			"has_issues": True,
			"has_projects": True,
			"has_wiki": True
			}

	def getUser(self,username):
		response = requests.get(self.api_url + "/users/" + username)
		return response.json()

	def getRepos(self,username):
		response = requests.get(self.api_url+"/users/"+username+"/repos")
		return response.json()

	def createRepo(self,repoName):
		self.json["name"] = repoName
		response = requests.post(self.api_url+"/user/repos?access_token="+self.token,data=json.dumps(self.json),headers=self.auth)
		return response.json()

github = Github()

while True:
	secim = input("1 - Find User\n2 - Get Repository\n3 - Create Repository\n4 - Exit\nSeçiminiz: ")
	
	if secim == "4":
		break
	else:
		if secim == "1":
			username = input("username: ")
			result = github.getUser(username)
			print(f'TALEP EDİLEN KULLANICI BİLGİLERİ:\nKULLANICI ADI: {result["name"]}\nHESAP TÜRÜ: {result["type"]}\nŞİRKETİ: {result["company"]}\nBLOG: {result["blog"]}\nLOKASYON: {result["location"]}\nEMAIL: {result["email"]}\nBIO: {result["bio"]}\nPUBLIC REPOS: {result["public_repos"]}')
			
		elif secim == "2":
			username = input("username: ")
			result = github.getRepos(username)
			for repo in result:
				print(repo["name"])

		elif secim == "3":
			name = input("Repo Name: ")
			result = github.createRepo(name)
			print(result)

		else:
			"Yanlış tuşladınız."
			break
