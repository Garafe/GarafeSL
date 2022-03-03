import requests

url = "link"

r = requests.get(url, allow_redirects=True)

open('PROGRAMMING_1.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")


url = "link"

r = requests.get(url, allow_redirects=True)

open('PROGRAMMING_2.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")
