import requests

url = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-INTRODUCTION.pdf"

r = requests.get(url, allow_redirects=True)

open('HTML-INTRODUCTION.pdf', 'wb').write(r.content)

os.system ("mv HTML-INTRODUCTION.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url1 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_1.pdf"

r = requests.get(url1, allow_redirects=True)

open('HTML-LESSON_1.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url2 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_2.pdf"

r = requests.get(url2, allow_redirects=True)

open('HTML-LESSON_2.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url3 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_3.pdf"

r = requests.get(url3, allow_redirects=True)

open('HTML-LESSON_3.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_3.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")


url4 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HTML-LESSON_4.pdf"

r = requests.get(url4, allow_redirects=True)

open('HTML-LESSON_4.pdf', 'wb').write(r.content)

os.system ("mv HTML-LESSON_4.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HTML_LESSONS/")



url5 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/PROGRAMMING_1.pdf"

r = requests.get(url5, allow_redirects=True)

open('PROGRAMMING_1.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")


url6 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/PROGRAMMING_2.pdf"

r = requests.get(url6, allow_redirects=True)

open('PROGRAMMING_2.pdf', 'wb').write(r.content)

os.system ("mv PROGRAMMING_2.pdf /sdcard/GARAFE_OFFICIAL_NOTES/PROGRAMMING_LESSONS/")



url7 = "https://github.com/Garafe/GarafeSL/blob/ecbb5ffad2ab20b4f1e8dc571683ce6963e658b6/files/notes/HACKING_1.pdf"

r = requests.get(url7, allow_redirects=True)

open('HACKING_1.pdf', 'wb').write(r.content)

os.system ("mv HACKING_1.pdf /sdcard/GARAFE_OFFICIAL_NOTES/HACKING_LESSONS/")
