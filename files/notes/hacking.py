import requests

url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HACKING_1.pdf"

r = requests.get(url, allow_redirects=True)

open('HACKING_1.pdf', 'wb').write(r.content)

os.system ("mv HACKING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HACKING_LESSONS/")


