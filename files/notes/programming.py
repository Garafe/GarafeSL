import requests

url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/PROGRAMMING_1.pdf"

r = requests.get(url, allow_redirects=True)

open('PROGRAMMING_1.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")


url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/PROGRAMMING_2.pdf"

r = requests.get(url, allow_redirects=True)

open('PROGRAMMING_2.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")
