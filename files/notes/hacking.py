import requests

url = "link"

r = requests.get(url, allow_redirects=True)

open('HACKING_1.pdf', 'wb').write(r.content)

os.system ("mv HACKING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HACKING_LESSONS/")


