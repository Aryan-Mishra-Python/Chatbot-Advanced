""" This File is the skeleton for the file-to-be-created 'main.py' """
import os
import ctypes
from random import choice
from time import strftime, sleep
from urllib.request import urlopen
import smtplib
import subprocess
import shutil
import sys
from pyjokes import get_joke
from bs4 import BeautifulSoup as soup
import wikipedia
import winshell
from googlesearch import search


# To Generate random Quotes
def get_quote():
    """Get Qoutes for some sensible personality"""
    quotes = open("Quotes.txt", encoding="utf-8").read().splitlines()
    line = choice(quotes)
    print(line)


# To Get A Joke!
def joke():
    """Well everybody loves jokes isn't it?"""
    print(get_joke())



# To get the current time
def get_time():
    """This Function Gets The current Time!"""
    time = strftime("%c")
    print(time)



# To make the assistant sleep
def sleep_now(seconds):
    """This function makes the assistant sleep for 'x' seconds"""
    print("Sleeping... zzzz")
    sleep(seconds)
    print("AWAKE!")



# To send email
# IMPORTANT: This is a delicate piece of software so think twice before you change this!
def send_email(reciver, content):
    """This function sends emails!"""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('umasaryan@gmail.com', '21@12@2008')
    server.sendmail('umasaryan@gmail.com', reciver, content)
    server.close()
    print(f"Content Was Recived to {reciver} As\n\n{content}")




# To Write a note
def make_note(name, content, title="Not Provided"):
    """This Function simply makes notes!"""
    file = open(str(name), "a", encoding="utf-8")
    # Some Formating
    file.write("Note Written On: ")
    file.write(strftime("%c")+"\n")
    file.write("Title: ")
    file.write(str(title)+"\n")
    file.write(f":-\n\n")
    # Real Content
    file.write("Content: \n")
    file.write(content+"\n\n\n")
    # Closing the file
    file.close()




# To Change the background of the desktop
def change_background():
    """This Function changes the desktop background randomly"""
    backgrounds = ["E:\\Aryan\\Most Advanced Chatbot\\Images\\First.png",
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Second.png",
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Third.png", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Fourth.png",
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Fifth.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Sixth.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Seventh.png",
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Eighth.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Nineth.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Tenth.jpg",
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Eleventh.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Twelth.jpg", 
                   "E:\\Aryan\\Most Advanced Chatbot\\Images\\Thirteenth.jpg"]


    path = choice(backgrounds)
    print(f"Changing Background To: '{path}'")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 0)




# To Get the latest news
def get_news(true_or_false=False):
    """This Function Open News Eithier Virtually or a text-based version of it from google news"""
    if true_or_false is True:
        os.startfile("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    elif true_or_false is False:
        news_url = "https://news.google.com/news/rss"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()

        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        # Print news title, url and publish date
        for news in news_list:
            print(news.title.text)
            print(news.pubDate.text)
            print("="*60)



def search_google(query):
    """This Function Searches Google Engine Based On The query
    Input: search_google("Sundar Pichia")
    Output: Webrowser Opened With The query- Sundar Pichia
    """
    os.startfile(f"http://www.google.com/search?q={query}")



def search_map(place):
    """This Function Searches Google Maps Based On The place
    Input: search_map("Los Angles")
    Output: Webrowser Opened With The place- Los Angles
    """
    os.startfile(f"https://www.google.com/maps/place/{place}")


def search_youtube(video):
    """This Function Searches Youtube Based On The video
    Input: search_map("Tech With Tim")
    Output: Youtube Opened With The query - Tech With Tim
    """
    os.startfile(f"https://www.youtube.com/results?search_query={video}")




def get_wiki(topic, get_virtual=False, lang="en"):
    """This function connects from wikipedia and
    gets a summary about the topic
    """
    if get_virtual is True:
        os.startfile(f"https://en.wikipedia.org/wiki/{topic}")

    elif get_virtual is False:
        topic = topic.title()
        wikipedia.set_lang(lang)
        print("Your Topic:", topic, "\n")
        print(wikipedia.summary(str(topic)))




# Interacting with the windows!
def lock_computer():
    """This Function Locks your device!"""
    print("Locking Your Device!")
    sleep(4)
    ctypes.windll.user32.LockWorkStation()
def empty_recylcle_bin():
    """This Function Emyties Your Dirty Recyle Bin"""
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
    print("Recyle Bin is Emptied!")
def restart():
    """This Function Restarts Your Device"""
    subprocess.call(["shutdown", "/r"])
def shutdown():
    """THis Function Shutsdown the device and you!!"""
    subprocess.call('shutdown / p /f')



# To Open up a program
def open_program(word=""):
    """This function opens up a program based upon the input!"""
    word = word.lower()
    if "chrome" in word.split():
        print("Starting Google Chrome, Hold On")
        os.startfile("chrome.exe")

    elif "sublime" in word.split():
        print("Opening Your Workspace, Aryan Mishra")
        os.startfile("D:\\Sublime Text\\sublime_text.exe")

    elif "notepad" in word.split():
        print("Starting Notepad")
        os.startfile("notepad.exe")

    elif "sticky" in word.split():
        print("Sticky Notes Here!")
        os.startfile("StikyNot.exe")

    elif "code" in word.split():
        print("Microsoft Visual Code Starting, Hold On a Second")
        os.startfile("D:\\Visual Studio Code\\Code.exe")

    elif "youtube" in word.split():
        print("Starting Chrome with Youtube, Wait Please")
        os.startfile("https://www.youtube.com")

    elif "cmd" in word.split():
        print("Microsoft Windows Command Prompt, At your call")
        os.startfile("cmd.exe")

    elif "git" in word.split():
        print("Git Bash, Starting Up")
        os.startfile("C:\\Program Files\\Git\\git-bash.exe")

    elif "powershell" in word.split():
        print("Microsoft Windows Powershell, Up and running")
        os.startfile("powershell.exe")

    elif "conda" in word.split():
        os.system("start /B start cmd.exe @cmd /k conda")
        print("conda is Up!")


    elif "python" in word.split():
        print("Python 3.7 (32-bit), Launching Now")
        os.startfile("C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe")

    else:
        print("Program To Be added soon!!")


# To copy an existing file or folder or directory
def copy(file, dest):
    """This Function copies an existing file or folder or directory"""
    shutil.copy(file, dest)


def move(file, dest):
    """This Function moves an existing file or folder or directory"""
    shutil.move(file, dest)



def make_folder(name):
    """This function makes a floder is exists overwrites it BE CAREFUL WITH IT!"""
    os.mkdir(name)

def remove_folder(name):
    """This function removes an existing folder"""
    os.rmdir(name)


def make_file(name, extension, content=""):
    """This functions makes a file if exists overwrites it BE CAREFUL WITH IT!"""
    new_file = open(str(name)+"."+str(extension), "w+")
    new_file.write(content)


def rename(old_name, new_name):
    """This function renames an existing file or folder or directory"""
    os.rename(old_name, new_name)


def getsizeof(obj):
    """This function get size of an given object"""
    size_in_bytes = sys.getsizeof(obj)
    size_in_kilobytes = size_in_bytes/1024
    size_in_megabytes = size_in_kilobytes/1024
    print(size_in_megabytes, "Megabytes")



# To search google!
def search_it(question):
    """This function browses the web and opens up google
    and gives you an text-based version search results"""

    query = question
    print("Searching The Web for you, Hold on a second...\n")
    for results in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(results)

    print("\n")
