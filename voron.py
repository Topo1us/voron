import socket
import os
import time
import requests
import html2text
import termcolor
from termcolor import colored
from time import sleep, strftime
color_red='\033[31m'
#-1-modul
os.system('clear')
mb='1.69 мб'
progs=('\n\033[32m\n   сканер сайтов- - -\033[31mscan yzel\033[32m.\n   сканер портов- - -\033[31mscan port\033[32m.\n   сканер ip- - - - - -\033[31mscan ip\033[32m.\n   сканер номера- - -\033[31mscan tp\033[32m.')
ver='1.6'
def code_200():
    try:
        requests.get("https://google.com", timeout=4)
        print('\033[32mподключенно к сети')
    except:
        print('\033[31mне подключенно к сети')
code_200()
print('''
\033[32mдоступ к системе voron открыт.
\033[35mверсия 1.6
\033[32m
''')
print('\033[32m-v-o-r-o-n-\n')
#-2-start_comands
def a_1():
#-3-start_progs-a_1
    def enter():
#-4-start_enter
        enter=input('--'+strftime('\033[31m%H:%M')+'\n\033[32mdark@root- ')
#        enter=enter.lower()
        if enter=='help' or enter=='h' or enter=='-h' or enter=='помощь' or enter=='помоги' or enter=='хелп' or enter=='he' or enter=='hr' or enter=='Help' or enter=='H' or enter=='-H' or enter=='Помощь' or enter=='Помоги' or enter=='Хелп' or enter=='He' or enter=='Hr':
            print('''доступные команды:
autors      - авторы программы voron.
-----------
ost         - основные команды системы.
-----------
voron       - полный доступ к системе.
ytil        - документация системы.
v-v         - обновления voron.
''')
        elif enter=='port_scan' or enter=='сканер портов' or enter=='port' or enter=='Port_scan' or enter=='Сканер портов' or enter=='Port' or enter=='scan port':
            po='порт '
            cl=color_red+' закрыт'
            b=0
            nm=0
            fg=[21, 22, 23, 25,31,41, 43, 45, 53,59, 68, 79, 80, 99, 110, 113, 115, 119, 121, 123, 135, 139, 143, 161, 179, 220, 389, 421, 443, 445, 456, 531, 555, 666, 911,
                         993, 999, 1001, 1010, 1011,1012,1015,1024,1024,1042,1045,1090,1170,1243,1245,1269,1492,1509,1600, 1723,1807,1981,1999,2023,2115, 2140, 2155, 2283, 2600, 2801, 3024,
                         2049, 3128, 3129, 3150, 3459, 3700, 3791, 4092, 3459, 3700, 3791,3306, 3389, 4321, 4567, 4590, 5000, 5001, 5011, 5031, 5321, 5400, 5401, 5550, 5555, 5556, 5060, 8080,
                         5569, 5631, 5742, 6400, 6669, 5631, 5742, 6400, 6669, 6670, 6771, 6776, 6912, 6939, 6970, 7000, 7300, 7301, 7306, 7307, 7308, 7789, 9091, 9400, 9090, 9872, 9873, 9874,
                         9875, 9876, 9878, 9989, 10101, 10520, 10607, 11000, 11225, 12076, 12223, 12345, 12346, 12361, 12362, 12631, 13000, 16969, 17300, 20000, 20001, 20203, 21544, 22222, 23456,
                         23476, 23477, 27374, 30029, 30100, 30101, 30102, 30103, 30999, 31336, 31337, 31339, 31666, 31785, 31787, 31789, 31791, 33333, 33911, 34324, 33911, 40412, 40421, 40422, 40423,
                         40426, 50505, 50766, 53001, 54320, 54321, 60000, 61466, 65000, 1349, 2989, 3801, 10067, 10167, 26274, 29891, 31337, 31338, 31789, 31791, 47262,54321]

            def openports(ip):
                x=1
                port_open=0
                port_close=0
                op=[]
                ops=[]
                for port in fg:
                    try:
                        sock = socket.socket()
                        sock.settimeout(0.1)
                        sock.connect((ip, port))
                        print('\033[32mпорт:: %s' % port, ':: открыт')
                        port_open+=1
                        op.append(port)
                        sock.close()
                    except:
#                        print('\033[31mпорт:: %s' % port, ':: закрыт')
                        port_close+=1
                        ops.append(port)
                         

                print('закрытых портов '+str(port_close))
                print('\033[32mоткрытых портов '+str(port_open),op)
            def openports2():
                ip=input('IP: ')
                port=int(input('PORT: '))
                for lol in[port]:
                    try:
                        sock = socket.socket()
                        sock.settimeout(0.2)
                        sock.connect((ip, lol))
                        print('\033[32mпорт:: %s' % lol, ':: открыт')
                        sock.close()
                    except:
                        print('\033[31mпорт:: %s' % lol, ':: закрыт')
                print('\033[32mготово.')
            print('''
[1] сканирование стандартных портов.
[2] сканирование определенного порта. 

''')
            x=input('~ ')
            if x=='1':
                openports(input('IP: '))
            elif x=='2':
                openports2()
        elif enter=='autors' or enter=='Autors':
            a=('T', 'To', 'Top', 'Topo', 'Topo1', 'Topo1u', 'Topo1us', 'Topo1us-', 'Topo1us- -')
            b=0
            while True:
                print(colored(a[b % len(a)], 'red'), sep='', end='\r')
                sleep(0.1)
                b+=1
                if b>9:
                    print('')
                    break
        elif enter=='ost' or enter=='Ost':
            print('''
o         - очистка экрана.
progs - показ установленых программ в Voron.
mb        - вес системы voron.''')  
        elif enter=='o' or enter=='O':
            os.system('clear')
        elif enter=='voron' or enter=='Voron':
            x=input('код доступа: ')
            print('\033[31mотказано в доступе.')
            print('\033[32m:).')
            print('за кодом доступа Вы можете обратиться к автору.\nтак как автор любит комедии, Вы должны пройти испытание.')
            time.sleep(5)
            os.system('clear')
            print('пасхалка.\nищите записи с кодовым словом \033[31mTopo1us\033[32m.')
        elif enter=='block_111' or enter=='progs' or enter=='Progs':
            print(progs)
        elif enter=='voron-inf' or enter=='voron-info' or enter=='inf' or enter=='info' or enter=='информация' or enter=='Ytil' or enter=='ytil':
            print('обновление voron будут релизоваться по выходным дням.\nверсия '+str(ver)+' содержит:'+str(progs))
        elif enter=='scan site' or enter=='yzel' or enter=='узел' or enter=='сканер сайта':
            def re():
                f=input('ссылка: ')
                s=requests.get(f)
                print(s.text)
            def rer():
                f=input('ссылка: ')
                s=requests.get(f)
                d=html2text.HTML2Text().handle(s.text)
                print(d)
            try:
                cer=input('[1] код страницы.\n[2] текст страницы.\n\n~  ')
                if cer=='1':
                    re()
                elif cer=='2':
                    rer()
            except:
                print(color_red+'неправильная ссылка.')
        elif enter=='v-v':
            print('''
1.1 август 2020 год.
1.2 ноябрь 2020 год.
1.3 ноябрь 2020 год.
1.4 декабрь 2020 год.
1.5 декабрь 2020 год.
1.6 декабрь 2020 год.
''')
        elif enter=='mb' or enter=='Mb':
            print('вес системы voron составляет '+str(mb))
        elif enter=='scan ip' or enter=='Scan ip' or enter=='Ip' or enter=='ip':
            f=input('IP: ')
            f=('https://ipinfo.io/'+f+'/json')
            s=requests.get(f)
            s=s.text
            s=s.replace('"','')
            s=s.replace(' ','')
            s=s.replace('{','')
            s=s.replace('}','')
            s=s.replace(',','')
            s=s.replace(':',': ')
            s=s.replace('hostname: cloud.revoluz.io','-----')
            s=s.replace('city','город')
            s=s.replace('region','регион')
            s=s.replace('country','страна')
            s=s.replace('loc','геолокация')
            s=s.replace('readme: https: //ipinfo.io/missingauth','-----')
            s=s.replace('org: AS55688PT.BeonIntermedia','')
            s=s.replace('timezone','континент')
            print(s)
        elif enter=='scan tp' or enter=='Scan tp':
            import urllib.request
            import json
            print('пример::7 900 777 11 22\n')
            phone=input('номер: ')
            getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
            infoPhone = urllib.request.urlopen( getInfo )
            infoPhone = json.load( infoPhone )
            print( u"Номер      --->", "+" + phone )
            print( u"Страна     ---> ", infoPhone["country"]["name"] )
            print( u"Регион     ---> ", infoPhone["region"]["name"] )
            print( u"Округ      ---> ", infoPhone["region"]["okrug"] )
            print( u"Оператор   ---> ", infoPhone["0"]["oper"] )
            print( u"Континент  ---> ", infoPhone["country"]["location"] )
        else:
            os.system(enter)
            print('\033[32m--внутрение команды os--')
#-5-inkor---
    while True:
        enter()
#try:
a_1()
#except:
#    print('ошибка 101.\nобратитесь к создателю.')
#    renable=input('перезапустить voron?\n: ')
#    renable=renable.lower()
#   if renable=='y' or renable=='yes' or renable=='д' or renable=='да' or renable=='Y' or renable=='Yes' or renable=='Д' or renable=='Да':
#        print('voron успешно перезагружен.')
#       a_1()
#   elif renable=='n' or renable=='no' or renable=='н' or renable=='нет' or renable=='N' or renable=='No' or renable=='Н' or renable=='Нет':
#        print('voron закрыт.')













