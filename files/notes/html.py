import requests

url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-INTRODUCTION.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-INTRODUCTION.pdf', 'wb').write(r.content)

os.system ("mv HTML-INTRODUCTION.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_1.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_1.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_2.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_2.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_3.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_3.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_3.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_4.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_4.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_4.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")
