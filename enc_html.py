#!/usr/bin/python
# Author Kingtebe
import os,sys,time
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    exit("# Module requests and bs4 not installed ")

c = '\033[1;36m'
p = '\033[1;37m'
h = '\033[1;32m'
k = '\033[1;33m'
m = '\033[1;31m'
q = '\033[30m'
t = '\033[0;32m'
u = '\033[0;37m'
z = '\033[2;107m'
o = '\033[0m'
r = '\033[0;36m'

def enc_html(file):
    url = "https://www.smartgb.com/free_encrypthtml.php"
    req = BeautifulSoup(requests.get(url).text,"html.parser")
    cah = req.find("input",{"name":"ch","type":"hidden"})
    url = "https://www.smartgb.com/free_encrypthtml.php?do=crypt"
    req = requests.post(url,data={
       "h":file,
       "s":"extended",
       "ch":cah.get("value"),
       "Skicka":"Encrypt+HTML"
    })
    out = BeautifulSoup(req.text,"html.parser").findAll("textarea")[0].text
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"\n{r}  {r}▄    ▄▄▄▄▄▄▄    ▄\n {r}▀▀▄─▄█████████▄─▄▀▀  {r}╔╗ {p}┬┌┬┐┌┐ ┌─┐┬ ┬   {r}╔═╗{p}┬ ┬┌─┐┌┐┌┌─┐┬\n {r}    ██ {k}▀{r}███{k}▀ {r}██      {r}╠╩╗{p}│ │ ├┴┐│ │└┬┘{q}───{r}║  {p}├─┤├─┤│││├┤ │\n {r}  ▄─▀████{k}▀{r}████▀─▄    {r}╚═╝{p}┴ ┴ └─┘└─┘ ┴    {r}╚═╝{p}┴ ┴┴ ┴┘└┘└─┘┴─┘\n {u}▀█    ██▀█▀██   █▀   {z}{q} By : Kingtebe | Yt : Bitboy Channel {o}{p}\n")
    print(f"  {t}⏣ {p}Waiting...")
    time.sleep(1.5)
    print(out)
    nam = file.replace(".html","_enc.html")
    with open(nam,"a+") as save:
         save.write(out)
    print(f"  {t}⏣ {p}File saved in",nam,"\n")

if __name__=='__main__':
    if len(sys.argv) < 2:
        exit("# Usage: python "+ sys.argv[0] +" <File>")
    else:
        enc_html(sys.argv[1])

