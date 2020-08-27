import socket
import os
import time
os.system('clear')
print('''
\033[32mдоступ к системе voron открыт.
\033[35mверсия 1.1
\033[32m
''')
progs=('\n    Сканер портов.\n     Бомбер СМС.')
def a_1():
    print('\033[32m-v-o-r-o-n-')
    def enter():
    
        enter=input(': ')
        enter=enter.lower()
        if enter=='help' or enter=='h' or enter=='-h' or enter=='помощь' or enter=='помоги' or enter=='хелп':
            b_6()
        elif enter=='port_scan' or enter=='сканер портов':
            b_7()
        elif enter=='autors':
            b_8()
        elif enter=='ost':
            b_1()
        elif enter=='o':
            os.system('clear')
        elif enter=='voron':
            b_9()
        elif enter=='bomber':
            b_3()
        elif enter=='i':
            b_2()
        elif enter=='block_111':
            block_111()
        elif enter=='cal' or enter=='календарь.':
            os.system(cal)
        elif enter=='voron-inf' or enter=='voron-info':
            b_10()
        else:
            os.system(enter)
#---------------------
    def block_111():
        oper=open(r'C:\Users\ender\Desktop\voron\block_1.txt','r')
        oper=oper.read()
        print('в блоке 111 находится: \n'+str(oper))
    def b_1():
        print('''
o         - очистка экрана.
i         - обновление пакетов данных, повышение мобильности работы системы.
block_111 - показ установленых программ в Voron.''')
    def b_2():
        os.system('pkg install python')
        os.system('pip install socket')
        os.system('pip install time')
        os.system('apt upgrade')
        os.system('apt update')
        a_1()
    def b_3():
        os.system('clear')
        block_1=open(r'C:\Users\ender\Desktop\voron\block_1.txt','r')
        block_1=block_1.read()
        if 'impulse' in block_1:
            c_1()
        else:
            c_1_2()
    def b_6():
        print('''доступные команды:
autors    - авторы программы voron.
-----------
port_scan - сканер портов. Сканирует порты по IP адресу.
ost       - основные команды системы.
-----------
voron     - полный доступ к системе.
voron-inf - документация системы.
''')
    def b_7():
        def openports(ip):
            x=1
            for port in [21, 22, 23, 25,31,41, 43, 45, 53,59, 68, 79, 80, 99, 110, 113, 115, 119, 121, 123, 135, 139, 143, 161, 179, 220, 389, 421, 443, 445, 456, 531, 555, 666, 911,
                         993, 999, 1001, 1010, 1011,1012,1015,1024,1024,1042,1045,1090,1170,1243,1245,1269,1492,1509,1600, 1723,1807,1981,1999,2023,2115, 2140, 2155, 2283, 2600, 2801, 3024,
                         2049, 3128, 3129, 3150, 3459, 3700, 3791, 4092, 3459, 3700, 3791,3306, 3389, 4321, 4567, 4590, 5000, 5001, 5011, 5031, 5321, 5400, 5401, 5550, 5555, 5556, 5060, 8080,
                         5569, 5631, 5742, 6400, 6669, 5631, 5742, 6400, 6669, 6670, 6771, 6776, 6912, 6939, 6970, 7000, 7300, 7301, 7306, 7307, 7308, 7789, 9091, 9400, 9090, 9872, 9873, 9874,
                         9875, 9876, 9878, 9989, 10101, 10520, 10607, 11000, 11225, 12076, 12223, 12345, 12346, 12361, 12362, 12631, 13000, 16969, 17300, 20000, 20001, 20203, 21544, 22222, 23456,
                         23476, 23477, 27374, 30029, 30100, 30101, 30102, 30103, 30999, 31336, 31337, 31339, 31666, 31785, 31787, 31789, 31791, 33333, 33911, 34324, 33911, 40412, 40421, 40422, 40423,
                         40426, 50505, 50766, 53001, 54320, 54321, 60000, 61466, 65000, 1349, 2989, 3801, 10067, 10167, 26274, 29891, 31337, 31338, 31789, 31791, 47262,54321]:
                try:
                    sock = socket.socket()
                    sock.settimeout(0.2)
                    sock.connect((ip, port))
                    print('\033[32mпорт:: %s' % port, ':: открыт')
                    sock.close()
                except:
                    print('\033[31mпорт:: %s' % port, ':: закрыт')
            print('\033[32mготово.')
            a_1()
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
            a_1()
        print('''
[1]Сканирование стандартных портов.
[2]Сканирование определенного порта. 

''')
        x=input('~ ')
        if x=='1':
            openports(input('IP: '))
        if x=='2':
            openports2()
    def b_8():
        os.system(r'clear')
        print('W')
        time.sleep(0.1)    
        os.system(r'clear')
        print('Wo')
        time.sleep(0.1)    
        os.system(r'clear')
        print('Wol')
        time.sleep(0.1)    
        os.system(r'clear')
        print('WolF')
        time.sleep(0.1)    
        os.system(r'clear')
        print('WolFa')
        time.sleep(0.1)    
        os.system(r'clear')
        print('WolFak ')
        time.sleep(0.1)    
        os.system(r'clear')
        print('WolFak -')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - -')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - T')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - To')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - Top')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - Topo')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - Topo1')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - Topo1u')
        time.sleep(0.1)
        os.system(r'clear')
        print('WolFak - - Topo1us')
        time.sleep(0.1)
        #        cx=input('введите любой символ для выхода в систему voron.\n: ')
        a_1()
    def b_9():
        x=input('код доступа: ')
        print('\033[31mотказано в доступе.')
        print('\033[32m:).')
        a_1()
    def b_10():
        #voron-inf
        print('''
Система Voron разработана для повышения работы Termux.
Версия 1.1 содержит:'''+str(progs))
#----------------------     
    def c_1():
        number=input('номер: ')
        time_atack=input('время атаки в секундах: ')
        os.system(r'python C:\Users\ender\Desktop\voron\Impulse\impulse.py --method SMS --target '+str(number)+' --time '+str(time_atack)+' --threads 135')
        a_1()
    def c_1_2():
        y=input('\o33[31mрепозиторий impulse не установлен.\nустановить?[y/n]')
        y=y.lower()
        if y=='y':
            block_1=open(r'C:\Users\ender\Desktop\voron\block_1.txt','a')
            block_1=block_1.write('impulse')
#            os.system('git clone https://github.com/LimerBoy/Impulse')
#            os.system('pip3 install -r requirements.txt')
            print('\033[32mimpulse успешно установлен.')
            os.system('cd')
            c_1()
        elif y=='n':
            a_1()    
########################
    while True:
        enter()
a_1()