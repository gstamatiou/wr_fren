import os, time, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

adblock_url = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dcjpalhdlnbpafiamejdnhcphjbkeiagm%26installsource%3Dondemand%26uc"
adblock_path = "./extension_0_1_23_4076.crx"

def get_query(word):
    word = str(word)
    return "https://www.wordreference.com/redirect/translation.aspx?w=" + word + "&dict=fren"

# Check if crx of uBlock origin is in the directory
if not os.path.exists("./extension_0_1_23_4076.crx"):
    r = requests.get(adblock_url)
    with open("extension_0_1_23_4076.crx", "wb") as f:
        f.write(r.content)


chop = webdriver.ChromeOptions()
chop.add_extension(adblock_path)
browser = webdriver.Chrome(options = chop)

prev = None

while True:
    new = os.popen('xsel').read()
    if new != prev:
        print(new)
        prev = new
        browser.get(get_query(new))
    time.sleep(1)

