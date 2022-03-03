import requests

url = "link"

r = requests.get(url, allow_redirects=True)

open('HTML-INTRODUCTION.pdf', 'wb').write(r.content)

os.system ("mv HTML-INTRODUCTION.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "link"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_1.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "link"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_2.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "link"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_3.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_3.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url = "link"

r = requests.get(url, allow_redirects=True)

open('HTML-LESSON_4.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_4.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")
