#Librerie
import random
from colored import fg, bg, attr
import os
import time
from time import sleep
import sys
import climage
#Colori
reset = attr('reset')
rossoscuro = fg(1)
rossochiaro = fg(9)
verde = fg(47)
bianco = attr(0)
rosso = fg(160)
blu = fg(21)
marrone = fg(95)
giallo = fg(184)
#Animazione
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
#Crediti del programma
def crediti():
    input("Premi qualsiasi tasto per la fine del gioco")
    print(f"""{verde}
  ___ ___  ___   ___ ___    _   __  __ __  __   _     ___ _ _____ _____ ___    ___   _   _ 
 | _ \ _ \/ _ \ / __| _ \  /_\ |  \/  |  \/  | /_\   | __/_\_   _|_   _/ _ \  |   \ /_\ (_)
 |  _/   / (_) | (_ |   / / _ \| |\/| | |\/| |/ _ \  | _/ _ \| |   | || (_) | | |) / _ \ _ 
 |_|_|_|_\\\\___/ \___|_|_\/_/ \_\_|  |_|_|  |_/_/ \_\ |_/_/ \_\_|   |_| \___/  |___/_/ \_(_)
 |_   _| _ \ __| _ ) _ )_ _|                                                               
   | | |   / _|| _ \ _ \| |                                                                
  _|_| |_|_\___|___/___/___|  _  _  ___ ___                                                
 |   \| __| |  | _ )_ _| /_\ | \| |/ __/ _ \                                               
 | |) | _|| |__| _ \| | / _ \| .` | (_| (_) |                                              
 |___/|___|____|___/___/_/ \_\_|\_|\___\___/ _   ___  ___                                  
  / __|_ _| /_\ | _ \  /_\ |  \/  |_ _|   \ /_\ | _ \/ _ \                                 
 | (__ | | / _ \|   / / _ \| |\/| || || |) / _ \|   / (_) |                                
  \___|___/_/ \_\_|_\/_/ \_\_|  |_|___|___/_/ \_\_|_\\\\___/ {bianco}                                    
                                                                                                                        
                                                                                                                             
                                                                                                 
          """)
def caratteristiche2():    
    #Per dare a b2 il numero delle classi presenti nella lista dei png
    b2 = len(listaclassipng)
    print(f"\n  {rossoscuro}Creazione delle schede {rossochiaro}PNG{rossoscuro}...")
    time.sleep(0.5)
    #Ciclo per la creazione della scheda dei PNG
    for k in range(b2):
        def caratteristichebackup2():
            #Chiedo allineamento e verifica se l'utente ha inserito il giusto allineamento
            allineamento = input(f"  {rossoscuro}Inserisci tipo di allineamento ({rossochiaro}legale, neutrale o caotico{rossoscuro}): {rossochiaro}")
            time.sleep(1)
            #Genera statistiche random
            for1=random.randint(1,6)
            for2=random.randint(1,6)
            for3=random.randint(1,6)
            forza=for1+for2+for3
            #Bonus e malus di for
            if forza == 3:
                forbm = f"{rossoscuro}➖3"
                forbmi = 0
            elif forza == 4 or forza == 5:
                forbm = f"{rossoscuro}➖2"
                forbmi = 0
            elif forza == 6 or forza == 7 or forza == 8 or forza == 9:
                forbm = f"{rossoscuro}➖1"
                forbmi = 0
            elif forza == 10 or forza == 11 or forza == 12:
                forbm = f"{rossoscuro}no bonus/malus"
                forbmi = 0
            elif forza == 13 or forza == 14 or forza == 15:
                forbm = f"{verde}➕1"
                forbmi = 1
            elif forza == 16 or forza == 17:
                forbm = f"{verde}➕2"
                forbmi = 2
            elif forza == 18:
                forbm = f"{verde}➕3"
                forbmi = 3
            des1=random.randint(1,6)
            des2=random.randint(1,6)
            des3=random.randint(1,6)
            des=des1+des2+des3
            #Bonus e malus di des
            if des == 3:
                desbm = f"{rossoscuro}➖3"
                desbmi = 0
            elif des == 4 or des == 5:
                desbm = f"{rossoscuro}➖2"
                desbmi = 0
            elif des == 6 or des == 7 or des == 8 or des == 9:
                desbm = f"{rossoscuro}➖1"
                desbmi = 0
            elif des == 10 or des == 11 or des == 12:
                desbm = f"{rossoscuro}no bonus/malus"
                desbmi = 0
            elif des == 13 or des == 14 or des == 15:
                desbm = f"{verde}➕1"
                desbmi = 1
            elif des == 16 or des == 17:
                desbm = f"{verde}➕2"
                desbmi = 2
            elif des == 18:
                desbm = f"{verde}➕3"
                desbmi = 3
            cos1=random.randint(1,6)
            cos2=random.randint(1,6)
            cos3=random.randint(1,6)
            cos=cos1+cos2+cos3
            #Bonus e malus di cos
            if cos == 3:
                cosbm = f"{rossochiaro}➖3"
            elif cos == 4 or cos == 5:
                cosbm = f"{rossochiaro}➖2"
            elif cos == 6 or cos == 7 or cos == 8 or cos == 9:
                cosbm = f"{rossochiaro}➖1"
            elif cos == 10 or cos == 11 or cos == 12:
                cosbm = f"{rossoscuro}no bonus/malus"
            elif cos == 13 or cos == 14 or cos == 15:
                cosbm = f"{verde}➕1"
            elif cos == 16 or cos == 17:
                cosbm = f"{verde}➕2"
            elif cos == 18:
                cosbm = f"{verde}➕3"
            int1=random.randint(1,6)
            int2=random.randint(1,6)
            int3=random.randint(1,6)
            int=int1+int2+int3
            #Bonus e malus di int
            if int == 3:
                intbm = f"{rossochiaro}➖3"
            elif int == 4 or int == 5:
                intbm = f"{rossochiaro}➖2"
            elif int == 6 or int == 7 or int == 8 or int == 9:
                intbm = f"{rossochiaro}➖1"
            elif int == 10 or int == 11 or int == 12:
                intbm = f"{rossoscuro}no bonus/malus"
            elif int == 13 or int == 14 or int == 15:
                intbm = f"{verde}➕1"
            elif int == 16 or int == 17:
                intbm = f"{verde}➕2"
            elif int == 18:
                intbm = f"{verde}➕3"
            sag1=random.randint(1,6)
            sag2=random.randint(1,6)
            sag3=random.randint(1,6)
            #Bonus e malus di sag
            sag=sag1+sag2+sag3
            if sag == 3:
                sagbm = f"{rossochiaro}➖3"
            elif sag == 4 or sag == 5:
                sagbm = f"{rossochiaro}➖2"
            elif sag == 6 or sag == 7 or sag == 8 or sag == 9:
                sagbm = f"{rossochiaro}➖1"
            elif sag == 10 or sag == 11 or sag == 12:
                sagbm = f"{rossoscuro}no bonus/malus"
            elif sag == 13 or sag == 14 or sag == 15:
                sagbm = f"{verde}➕1"
            elif sag == 16 or sag == 17:
                sagbm = f"{verde}➕2"
            elif sag == 18:
                sagbm = f"{verde}➕3"
            car1=random.randint(1,6)
            car2=random.randint(1,6)
            car3=random.randint(1,6)
            car=car1+car2+car3
            #Bonus e malus di car
            if car == 3:
                carbm = f"{rossochiaro}➖3"
            elif car == 4 or car == 5:
                carbm = f"{rossochiaro}➖2"
            elif car == 6 or car == 7 or car == 8 or car == 9:
                carbm = f"{rossochiaro}➖1"
            elif car == 10 or car == 11 or car == 12:
                carbm = f"{rossoscuro}no bonus/malus"
            elif car == 13 or car == 14 or car == 15:
                carbm = f"{verde}➕1"
            elif car == 16 or car == 17:
                carbm = f"{verde}➕2"
            elif car == 18:
                carbm = f"{verde}➕3"
            #La variabile classe diventa l'elemento successivo della lista ogni volta che il ciclo si ripete
            classe = listaclassipng[k]
            #Verifica se le classi hanno i requisiti per essere giocati
            if classe.lower() == "guerriero":
                if forza >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 8
                attacco = 20 - forbmi
            elif classe.lower() == "mago":
                if int >= 13:
                    a = "✅"
                else:
                    a = "❌"  
                dado = 4
                attacco = 20 - desbmi        
            elif classe.lower() == "ladro":
                if int >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 4
                attacco = 20 - forbmi
            elif classe.lower() == "ranger":
                if forza >= 9 and sag >= 9 and des >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 10
                attacco = 20 - desbmi
            psalute = random.randint(1,dado)
            
            #Scheda del PNG         
            print(f"""
  {bianco}╔═══════════════════════════════════════
  {bianco}║  {rossoscuro}Le caratteristiche del {rossochiaro}{k+1}° PNG sono{rossoscuro}:  
  {bianco}║  {rossoscuro}Forza 💪: {rossochiaro}{forza} {forbm}
  {bianco}║  {rossoscuro}Destrezza 🎯: {rossochiaro}{des} {desbm}                   
  {bianco}║  {rossoscuro}Costituzione 🏋️: {rossochiaro}{cos} {cosbm}                
  {bianco}║  {rossoscuro}Intelligenza 🧠: {rossochiaro}{int} {intbm}              
  {bianco}║  {rossoscuro}Saggezza 👨‍🦳: {rossochiaro}{sag} {sagbm}                    
  {bianco}║  {rossoscuro}Carisma 🙏: {rossochiaro}{car} {carbm}                  
  {bianco}║  {rossoscuro}Classe 🧢: {rossochiaro}{classe.title()}            
  {bianco}║  {rossoscuro}Allineamento: {rossochiaro}{allineamento.title()}
  {bianco}║  {rossoscuro}Punti salute ❤️: {rossochiaro}{psalute}    
  {bianco}║  {rossoscuro}Giocabile: {rossochiaro}{a}
  {bianco}║  {rossoscuro}Livello: {rossochiaro}1
  {bianco}║  {rossoscuro}TxC 🤜: {rossochiaro}{attacco}     
  {bianco}╚═══════════════════════════════════════""")   
        caratteristichebackup2()
    crediti()
def caratteristiche():  
    #Per dare a b il numero delle classi presenti nella lista dei pg      
    b = len(listaclassipg)
    print(f"\n  {rossoscuro}Creazione delle schede {rossochiaro}PG{rossoscuro}...")
    time.sleep(0.5)
    #Ciclo per la creazione della scheda dei PG
    for l in range(b):
        def caratteristichebackup1():
            #Chiedo allineamento e verifica se l'utente ha inserito il giusto allineamento
            allineamento = input(f"  {rossoscuro}Inserisci tipo di allineamento ({rossochiaro}legale, neutrale o caotico{rossoscuro}): {rossochiaro}")
            time.sleep(1)
            #Genera statistiche random
            for1=random.randint(1,6)
            for2=random.randint(1,6)
            for3=random.randint(1,6)
            forza=for1+for2+for3
            #Bonus e malus di for
            if forza == 3:
                forbm = f"{rossoscuro}➖3"
                forbmi = 0
            elif forza == 4 or forza == 5:
                forbm = f"{rossoscuro}➖2"
                forbmi = 0
            elif forza == 6 or forza == 7 or forza == 8 or forza == 9:
                forbm = f"{rossoscuro}➖1"
                forbmi = 0
            elif forza == 10 or forza == 11 or forza == 12:
                forbm = f"{rossoscuro}no bonus/malus"
                forbmi = 0
            elif forza == 13 or forza == 14 or forza == 15:
                forbm = f"{verde}➕1"
                forbmi = 1
            elif forza == 16 or forza == 17:
                forbm = f"{verde}➕2"
                forbmi = 2
            elif forza == 18:
                forbm = f"{verde}➕3"
                forbmi = 3
            des1=random.randint(1,6)
            des2=random.randint(1,6)
            des3=random.randint(1,6)
            des=des1+des2+des3
            #Bonus e malus di des
            if des == 3:
                desbm = f"{rossoscuro}➖3"
                desbmi = 0
            elif des == 4 or des == 5:
                desbm = f"{rossoscuro}➖2"
                desbmi = 0
            elif des == 6 or des == 7 or des == 8 or des == 9:
                desbm = f"{rossoscuro}➖1"
                desbmi = 0
            elif des == 10 or des == 11 or des == 12:
                desbm = f"{rossoscuro}no bonus/malus"
                desbmi = 0
            elif des == 13 or des == 14 or des == 15:
                desbm = f"{verde}➕1"
                desbmi = 1
            elif des == 16 or des == 17:
                desbm = f"{verde}➕2"
                desbmi = 2
            elif des == 18:
                desbm = f"{verde}➕3"
                desbmi = 3
            cos1=random.randint(1,6)
            cos2=random.randint(1,6)
            cos3=random.randint(1,6)
            cos=cos1+cos2+cos3
            #Bonus e malus di cos
            if cos == 3:
                cosbm = f"{rossochiaro}➖3"
            elif cos == 4 or cos == 5:
                cosbm = f"{rossochiaro}➖2"
            elif cos == 6 or cos == 7 or cos == 8 or cos == 9:
                cosbm = f"{rossochiaro}➖1"
            elif cos == 10 or cos == 11 or cos == 12:
                cosbm = f"{rossoscuro}no bonus/malus"
            elif cos == 13 or cos == 14 or cos == 15:
                cosbm = f"{verde}➕1"
            elif cos == 16 or cos == 17:
                cosbm = f"{verde}➕2"
            elif cos == 18:
                cosbm = f"{verde}➕3"
            int1=random.randint(1,6)
            int2=random.randint(1,6)
            int3=random.randint(1,6)
            int=int1+int2+int3
            #Bonus e malus di int
            if int == 3:
                intbm = f"{rossochiaro}➖3"
            elif int == 4 or int == 5:
                intbm = f"{rossochiaro}➖2"
            elif int == 6 or int == 7 or int == 8 or int == 9:
                intbm = f"{rossochiaro}➖1"
            elif int == 10 or int == 11 or int == 12:
                intbm = f"{rossoscuro}no bonus/malus"
            elif int == 13 or int == 14 or int == 15:
                intbm = f"{verde}➕1"
            elif int == 16 or int == 17:
                intbm = f"{verde}➕2"
            elif int == 18:
                intbm = f"{verde}➕3"
            sag1=random.randint(1,6)
            sag2=random.randint(1,6)
            sag3=random.randint(1,6)
            sag=sag1+sag2+sag3
            #Bonus e malus di sag
            if sag == 3:
                sagbm = f"{rossochiaro}➖3"
            elif sag == 4 or sag == 5:
                sagbm = f"{rossochiaro}➖2"
            elif sag == 6 or sag == 7 or sag == 8 or sag == 9:
                sagbm = f"{rossochiaro}➖1"
            elif sag == 10 or sag == 11 or sag == 12:
                sagbm = f"{rossoscuro}no bonus/malus"
            elif sag == 13 or sag == 14 or sag == 15:
                sagbm = f"{verde}➕1"
            elif sag == 16 or sag == 17:
                sagbm = f"{verde}➕2"
            elif sag == 18:
                sagbm = f"{verde}➕3"
            car1=random.randint(1,6)
            car2=random.randint(1,6)
            car3=random.randint(1,6)
            car=car1+car2+car3
            #Bonus e malus di car
            if car == 3:
                carbm = f"{rossochiaro}➖3"
            elif car == 4 or car == 5:
                carbm = f"{rossochiaro}➖2"
            elif car == 6 or car == 7 or car == 8 or car == 9:
                carbm = f"{rossochiaro}➖1"
            elif car == 10 or car == 11 or car == 12:
                carbm = f"{rossoscuro}no bonus/malus"
            elif car == 13 or car == 14 or car == 15:
                carbm = f"{verde}➕1"
            elif car == 16 or car == 17:
                carbm = f"{verde}➕2"
            elif car == 18:
                carbm = f"{verde}➕3"
            #La variabile classe diventa l'elemento successivo della lista ogni volta che il ciclo si ripete
            classe = listaclassipg[l]
            #Verifica se le classi hanno i requisiti per essere giocati
            if classe.lower() == "guerriero":
                if forza >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 8
                attacco = 20 - forbmi
            elif classe.lower() == "mago":
                if int >= 13:
                    a = "✅"
                else:
                    a = "❌"  
                dado = 4
                attacco = 20 - desbmi     
            elif classe.lower() == "ladro":
                if int >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 4
                attacco = 20 - forbmi
            elif classe.lower() == "ranger":
                if forza >= 9 and sag >= 9 and des >= 13:
                    a = "✅"
                else:
                    a = "❌"
                dado = 10
                attacco = 20 - desbmi 
            psalute = random.randint(1,dado)
            
            #Scheda del PG         
            print(f"""
  {bianco}╔═══════════════════════════════════════
  {bianco}║  {rossoscuro}Le caratteristiche del {rossochiaro}{l+1}° PG sono{rossoscuro}:  
  {bianco}║  {rossoscuro}Forza 💪: {rossochiaro}{forza} {forbm}
  {bianco}║  {rossoscuro}Destrezza 🎯: {rossochiaro}{des} {desbm}                   
  {bianco}║  {rossoscuro}Costituzione 🏋️: {rossochiaro}{cos} {cosbm}                
  {bianco}║  {rossoscuro}Intelligenza 🧠: {rossochiaro}{int} {intbm}              
  {bianco}║  {rossoscuro}Saggezza 👨‍🦳: {rossochiaro}{sag} {sagbm}                    
  {bianco}║  {rossoscuro}Carisma 🙏: {rossochiaro}{car} {carbm}                  
  {bianco}║  {rossoscuro}Classe 🧢: {rossochiaro}{classe.title()}            
  {bianco}║  {rossoscuro}Allineamento: {rossochiaro}{allineamento.title()}
  {bianco}║  {rossoscuro}Punti salute ❤️: {rossochiaro}{psalute}    
  {bianco}║  {rossoscuro}Giocabile: {rossochiaro}{a}
  {bianco}║  {rossoscuro}Livello: {rossochiaro}1    
  {bianco}║  {rossoscuro}TxC 🤜: {rossochiaro}{attacco} 
  {bianco}╚═══════════════════════════════════════""")   
        caratteristichebackup1()
    caratteristiche2()

def pg():
    npg = int(input(f"  {rossoscuro}Quanti {rossochiaro}PG{rossoscuro} vuoi creare?: {rossochiaro}"))
    return npg
def png():
    npng = int(input(f"  {rossoscuro}Quanti {rossochiaro}PNG{rossoscuro} vuoi creare?: {rossochiaro}"))
    return npng
def listaclassi():
    listapg = []
    listapng = []
    return [listapg, listapng]
listaclassipg = (listaclassi())[0]
listaclassipng = (listaclassi())[1]

#CICLO PNG
def selettoreclasse2():
    os.system("cls")
    #Ciclo per il numero di volte presenti nella variabile png
    for b in range(png()):
        def classeb():
            os.system("cls")
            print(f"\n  {rossoscuro}Ora scegli la classe del {verde}{b+1}° PNG")
            print(f"""
{bianco}+**********************************+******************************************+************************************+**************************************+
|{rosso} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀   ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          {bianco}|                                    |{giallo}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀{bianco}|{giallo}   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso} ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀   {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      {bianco}|{marrone}    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀{bianco}|{giallo}   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀{bianco}|{giallo}   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  {bianco}|{blu}   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{giallo}   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  {bianco}|{blu}   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   {bianco}|{marrone}    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    {bianco}|{giallo}   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  {bianco}|{blu}   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   {bianco}|{marrone}    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀{bianco}|{giallo}  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       {bianco}|{bianco}⠀ 
|{rosso}  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  {bianco}|{blu}   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   {bianco}|{marrone}    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{giallo}   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       {bianco}|{bianco}⠀⠀
|{rosso}  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  {bianco}|{blu}   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀{bianco}|{bianco}
|{rosso}  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     {bianco}|{marrone}    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      {bianco}|{giallo}   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     {bianco}|{bianco}
|{rosso}  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        {bianco}|{marrone}    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    {bianco}|{giallo}  ⠀⠀⠀ ⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     {bianco}|{bianco}
|{rosso}  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      {bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀{bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ {bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}                                  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}             Guerriero            {bianco}|{blu}                   Mago                   {bianco}|                {marrone}Ladro               {bianco}|{giallo}                Ranger                {bianco}|{bianco}
+**********************************+******************************************+************************************+**************************************+
""")
            classe = input(f"  {rossoscuro}Seleziona la classe: {rossochiaro}")
            #Trasforma 1,2,3,4 in "guerriero", "mago", "ladro", "ranger"
            if classe == "1":
                classe = "guerriero"
            elif classe == "2":
                classe = "mago"
            elif classe == "3":
                classe = "ladro"
            elif classe == "4":
                classe = "ranger"
            if classe.lower() == "guerriero":
                os.system("cls")
                print(f"""
{verde}+**********************************+{bianco}******************************************+************************************+**************************************+
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |                                    |                                      |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |                                    |                                      |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|{bianco}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |                                    |  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
{verde}|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |{bianco}   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |{bianco}   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |{bianco}   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
{verde}|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |{bianco}   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
{verde}|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |{bianco}   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
{verde}|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |{bianco}   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
{verde}|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |{bianco}   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
{verde}|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |{bianco}   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
{verde}|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
{verde}|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
{verde}|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
{verde}|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |                                    |                                      |
{verde}|                                  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |                                    |                                      |
{verde}|             Guerriero            |{bianco}                   Mago                   |                Ladro               |                Ranger                |
{verde}+**********************************+{bianco}******************************************+************************************+**************************************+

{verde}  Hai scelto Guerriero!
""")
            elif classe.lower() == "mago":
                os.system("cls")
                print(f"""
{bianco}+**********************************{verde}+******************************************+{bianco}************************************+**************************************+
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |{bianco}                                    |                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |{bianco}                                    |                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |{bianco}                                    |  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |{bianco}    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  {verde}|   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |{bianco}    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  {verde}|   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |{bianco}    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  {verde}|   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |{bianco}    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  {verde}|   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |{bianco}    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  {verde}|   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |{bianco}    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  {verde}|   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |{bianco}    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  {verde}|   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |{bianco}    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  {verde}|   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |{bianco}                                    |                                      |
|                                  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |{bianco}                                    |                                      |
|             Guerriero            {verde}|                   Mago                   |{bianco}                Ladro               |                Ranger                |
+**********************************{verde}+******************************************+{bianco}************************************+**************************************+

{verde}  Hai scelto Mago!
""")       
            elif classe.lower() == "ladro":
                os.system("cls")
                print(f"""
{bianco}+**********************************+******************************************{verde}+************************************+{bianco}**************************************+
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         {verde}|                                    |{bianco}                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             {verde}|                                    |{bianco}                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          {verde}|                                    |{bianco}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      {verde}|    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|{bianco}   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      {verde}|    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|{bianco}   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|{bianco}   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   {verde}|    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   {verde}|    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |{bianco}   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   {verde}|    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|{bianco}  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   {verde}|    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   {verde}|    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     {verde}|    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |{bianco}   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        {verde}|    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |{bianco}   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     {verde}|    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |{bianco}   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        {verde}|    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 {verde}|                                    |{bianco}                                      |
|                                  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   {verde}|                                    |{bianco}                                      |
|             Guerriero            |                   Mago                   {verde}|                Ladro               |{bianco}                Ranger                |
+**********************************+******************************************{verde}+************************************+{bianco}**************************************+

{verde}  Hai scelto Ladro!              
""")
            elif classe.lower() == "ranger":
                os.system("cls")
                print(f"""
{bianco}+**********************************+******************************************+************************************{verde}+**************************************+{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |                                    {verde}|                                      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |                                    {verde}|                                      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |                                    {verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |{bianco}
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀{verde}|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀{verde}|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀{verde}|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    {verde}|   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀{verde}|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |{bianco}
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |{bianco}
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|{bianco}
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      {verde}|   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |{bianco}
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    {verde}|   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |{bianco}
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  {verde}|   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |{bianco}
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|{bianco}⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |                                    {verde}|                                      |{bianco}
|                                  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |                                    {verde}|                                      |{bianco}
|             Guerriero            |                   Mago                   |                Ladro               {verde}|                Ranger                |{bianco}
+**********************************+******************************************+************************************{verde}+**************************************+{bianco}
            
{verde}  Hai scelto Ranger!            
""")  
            #Se la classe ha un nome non valido, te la fa riscegliere
            elif classe.lower() != "guerriero"  and classe.lower() != "mago" and classe.lower() != "ladro" and classe.lower() != "ranger":
                print(f'  {rossoscuro}Classe invalida, seleziona "Guerriero", "Mago", "Ladro" o "Ranger')
                classeb()
            #Chiede la conferma all'utente
            print(f"  {rossoscuro}NB: Una volta scelta la classe non potrai più cambiarla!")
            conferma = input(f"  {rossoscuro}Sei sicuro di voler la classe {classe}? ({rossochiaro}Si{rossoscuro}/{rossochiaro}No{rossoscuro}): {rossochiaro}")
            if conferma.lower() == "si" or conferma.lower() == "s":
                listaclassipng.append(classe.lower())
            else:
                os.system("cls")
                classeb()           
        classeb()
    caratteristiche()

#PG
def selettoreclasse():
    os.system("cls")
    #Ciclo per il numero di volte presenti nella variabile pg
    for i in range(pg()):
        def classex():
            os.system("cls")
            print(f"\n  {rossoscuro}Ora scegli la classe del {verde}{i+1}° PG")
            print(f"""
{bianco}+**********************************+******************************************+************************************+**************************************+
|{rosso} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀   ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          {bianco}|                                    |{giallo}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀{bianco}|{giallo}   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso} ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀   {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      {bianco}|{marrone}    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀{bianco}|{giallo}   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀{bianco}|{giallo}   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  {bianco}|{blu}   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{giallo}   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  {bianco}|{blu}   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   {bianco}|{marrone}    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    {bianco}|{giallo}   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     {bianco}|{bianco}
|{rosso}  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  {bianco}|{blu}   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   {bianco}|{marrone}    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀{bianco}|{giallo}  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       {bianco}|{bianco}⠀ 
|{rosso}  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  {bianco}|{blu}   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   {bianco}|{marrone}    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   {bianco}|{giallo}   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       {bianco}|{bianco}⠀⠀
|{rosso}  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  {bianco}|{blu}   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   {bianco}|{marrone}    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀{bianco}|{bianco}
|{rosso}  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     {bianco}|{marrone}    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      {bianco}|{giallo}   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     {bianco}|{bianco}
|{rosso}  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        {bianco}|{marrone}    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    {bianco}|{giallo}  ⠀⠀⠀ ⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     {bianco}|{bianco}
|{rosso}  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        {bianco}|{marrone}    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  {bianco}|{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      {bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ {bianco}|{bianco}
|{rosso}  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀{bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               {bianco}|                                    |{giallo}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ {bianco}|{bianco}⠀
|{rosso}  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀{bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}                                  {bianco}|{blu}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   {bianco}|                                    |{giallo}                                      {bianco}|{bianco}
|{rosso}             Guerriero            {bianco}|{blu}                   Mago                   {bianco}|                {marrone}Ladro               {bianco}|{giallo}                Ranger                {bianco}|{bianco}
+**********************************+******************************************+************************************+**************************************+
""")
            classe = input(f"  {rossoscuro}Seleziona la classe: {rossochiaro}")
            #Trasforma 1,2,3,4 in "guerriero", "mago", "ladro", "ranger"
            if classe == "1":
                classe = "guerriero"
            elif classe == "2":
                classe = "mago"
            elif classe == "3":
                classe = "ladro"
            elif classe == "4":
                classe = "ranger"
            if classe.lower() == "guerriero":
                os.system("cls")
                print(f"""
{verde}+**********************************+{bianco}******************************************+************************************+**************************************+
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |                                    |                                      |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |                                    |                                      |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|{bianco}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |                                    |  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
{verde}|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |{bianco}   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |{bianco}   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
{verde}|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |{bianco}   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
{verde}|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |{bianco}   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
{verde}|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |{bianco}   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
{verde}|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |{bianco}   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
{verde}|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |{bianco}   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
{verde}|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |{bianco}   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
{verde}|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
{verde}|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
{verde}|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
{verde}|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
{verde}|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |                                    |                                      |
{verde}|                                  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |                                    |                                      |
{verde}|             Guerriero            |{bianco}                   Mago                   |                Ladro               |                Ranger                |
{verde}+**********************************+{bianco}******************************************+************************************+**************************************+

{verde}  Hai scelto Guerriero!
""")
            elif classe.lower() == "mago":
                os.system("cls")
                print(f"""
{bianco}+**********************************{verde}+******************************************+{bianco}************************************+**************************************+
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |{bianco}                                    |                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |{bianco}                                    |                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀{verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |{bianco}                                    |  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |{bianco}    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  {verde}|   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |{bianco}    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  {verde}|   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |{bianco}    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  {verde}|   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |{bianco}    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  {verde}|   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |{bianco}    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  {verde}|   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |{bianco}    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  {verde}|   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |{bianco}    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  {verde}|   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |{bianco}    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  {verde}|   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |{bianco}    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |{bianco}                                    |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀{verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |{bianco}                                    |                                      |
|                                  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |{bianco}                                    |                                      |
|             Guerriero            {verde}|                   Mago                   |{bianco}                Ladro               |                Ranger                |
+**********************************{verde}+******************************************+{bianco}************************************+**************************************+

{verde}  Hai scelto Mago!
""")       
            elif classe.lower() == "ladro":
                os.system("cls")
                print(f"""
{bianco}+**********************************+******************************************{verde}+************************************+{bianco}**************************************+
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         {verde}|                                    |{bianco}                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             {verde}|                                    |{bianco}                                      |
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          {verde}|                                    |{bianco}  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      {verde}|    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀|{bianco}   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      {verde}|    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀|{bianco}   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀|{bianco}   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   {verde}|    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   {verde}|    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    |{bianco}   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   {verde}|    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀|{bianco}  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |⠀
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   {verde}|    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   |{bianco}   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |⠀⠀
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   {verde}|    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     {verde}|    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      |{bianco}   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        {verde}|    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    |{bianco}   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     {verde}|    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  |{bianco}   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        {verde}|    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |⠀
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               {verde}|                                    |{bianco}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |⠀
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 {verde}|                                    |{bianco}                                      |
|                                  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   {verde}|                                    |{bianco}                                      |
|             Guerriero            |                   Mago                   {verde}|                Ladro               |{bianco}                Ranger                |
+**********************************+******************************************{verde}+************************************+{bianco}**************************************+

{verde}  Hai scelto Ladro!              
""")
            elif classe.lower() == "ranger":
                os.system("cls")
                print(f"""
{bianco}+**********************************+******************************************+************************************{verde}+**************************************+{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         |                                    {verde}|                                      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀             |                                    {verde}|                                      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀          |                                    {verde}|  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⠀               |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀      |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        |{bianco}
|  ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀      |    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀{verde}|   ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀      |    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⡀⠀     ⠀   ⠀{verde}|   ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀  |   ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀   |    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠛⠛⠀⠀⠀       ⠀{verde}|   ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀  |   ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀   |    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣷⡄⠀⣀⣀⠓⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|   ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆  |   ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀   |    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣦⣈⠻⣦⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀    {verde}|   ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀     |{bianco}
|  ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅  |   ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃   |    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠁⣼⡿⠻⣿⣿⣷⣄⣠⣴⠆⠀⠀⠀⠀⠀⠀    ⠀{verde}|  ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀       |{bianco}
|  ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟  |   ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀   |    ⠀⠀⠀⠻⣿⣿⣿⣿⡟⠀⢸⣿⣿⣦⣄⡉⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀   {verde}|   ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀       |{bianco}
|  ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀  |   ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀   |    ⠀⠀⠀⠀⠈⠛⠿⠋⠀⠀⢻⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀     ⠀|{bianco}
|  ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀  |   ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀     |    ⠀⠀⠀⣀⣀⣤⣶⣄⠀⠀⠈⠿⢿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀      {verde}|   ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀     |{bianco}
|  ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇  |   ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇        |    ⠀⠀⠸⠟⠛⠉⠻⣿⣧⡀⣼⣶⣤⣄⠉⠉⠛⠛⠻⢿⣿⣦⡀⠀⠀⠀⣠⡀    {verde}|   ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇     |{bianco}
|  ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁  |   ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀     |    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣆⣠⣾⠟⠁⠀⠀  {verde}|   ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉     |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀        |    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀  {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀      |{bianco}
|  ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀  ⠀|   ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀        |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀     ⠀ |{bianco}
|  ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀          |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀      ⠀|{bianco}⠀
|  ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀               |                                    {verde}|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀     ⠀ |{bianco}
|  ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀  ⠀⠀|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁                 |                                    {verde}|                                      |{bianco}
|                                  |   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀                   |                                    {verde}|                                      |{bianco}
|             Guerriero            |                   Mago                   |                Ladro               {verde}|                Ranger                |{bianco}
+**********************************+******************************************+************************************{verde}+**************************************+{bianco}

{verde}  Hai scelto Ranger!            
""")        
            #Se la classe ha un nome non valido, te la fa riscegliere
            elif classe.lower() != "guerriero"  and classe.lower() != "mago" and classe.lower() != "ladro" and classe.lower() != "ranger":
                print(f'{rossoscuro}Classe invalida, seleziona "Guerriero", "Mago", "Ladro" o "Ranger')
                classex()
            #Chiede la conferma all'utente
            print(f"  {rossoscuro}NB: Una volta scelta la classe non potrai più cambiarla!")
            conferma = input(f"  {rossoscuro}Sei sicuro di voler la classe {classe}? ({rossochiaro}Si{rossoscuro}/{rossochiaro}No{rossoscuro}): {rossochiaro}")
            if conferma.lower() == "si" or conferma.lower() == "s":
                listaclassipg.append(classe.lower())
            else:
                os.system("cls")
                classex()

        classex()
    selettoreclasse2()    
def tutorial():
    #Tutorial per i nuovi giocatori
    print(f"""{fg(87)}
#############################################################
In Dungeons & Dragons devi creare il tuo personaggio ideale 
per combattere contro altri giocatori.
Ci sono 4 classi: Guerriero, Mago, Ladro e Ranger 
Ogni PG ha 6 statistiche, ovvero:
Forza, Destrezza, Costituzione, Intelligenza, Saggezza e Carisma.
Scegli la classe e la razza che più preferisci!          
#############################################################""")
    input(f"{bianco}\nClicca qualsiasi tasto per continuare")
    os.system("cls")
def menu():
    try:
        os.system("cls")
        os.system("title Dungeons and Dragons ")
        print(f"""{rossoscuro}
                          .-._            _,---.      ,----.     _,.---._    .-._          ,-,--.         
  _,..---._  .--.-. .-.-./==/ \  .-._ _.='.'-,  \  ,-.--` , \  ,-.' , -  `. /==/ \  .-._ ,-.'-  _\        
/==/,   -  \/==/ -|/=/  ||==|, \/ /, /==.'-     / |==|-  _.-` /==/_,  ,  - \|==|, \/ /, /==/_ ,_.'        
|==|   _   _\==| ,||=| -||==|-  \|  /==/ -   .-'  |==|   `.-.|==|   .=.     |==|-  \|  |\==\  \           
|==|  .=.   |==|- | =/  ||==| ,  | -|==|_   /_,-./==/_ ,    /|==|_ : ;=:  - |==| ,  | -| \==\ -\          
|==|,|   | -|==|,  \/ - ||==| -   _ |==|  , \_.' )==|    .-' |==| , '='     |==| -   _ | _\==\ ,\         
|==|  '='   /==|-   ,   /|==|  /\ , \==\-  ,    (|==|_  ,`-._ \==\ -    ,_ /|==|  /\ , |/==/\/ _ |        
|==|-,   _`//==/ , _  .' /==/, | |- |/==/ _  ,  //==/ ,     /  '.='. -   .' /==/, | |- |\==\ - , /        
`-.`.____.' `--`..---'   `--`./  `--``--`------' `--`-----``     `--`--''   `--`./  `--` `--`---'         
  ,---.--.                                    ,---.          _,---.     _,.---._    .-._          ,-,--.  
 /  -_ \==\          _,..---._   .-.,.---.  .--.'  \     _.='.'-,  \  ,-.' , -  `. /==/ \  .-._ ,-.'-  _\ 
 |` / \/==/        /==/,   -  \ /==/  `   \ \==\-/\ \   /==.'-     / /==/_,  ,  - \|==|, \/ /, /==/_ ,_.' 
  \ \ /==/         |==|   _   _\==|-, .=., |/==/-|_\ | /==/ -   .-' |==|   .=.     |==|-  \|  |\==\  \    
  /  \==/          |==|  .=.   |==|   '='  /\==\,   - \|==|_   /_,-.|==|_ : ;=:  - |==| ,  | -| \==\ -\   
 /. / \==\         |==|,|   | -|==|- ,   .' /==/ -   ,||==|  , \_.' )==| , '='     |==| -   _ | _\==\ ,\  
| _ \_/\==\        |==|  '='   /==|_  . ,'./==/-  /\ - \==\-  ,    ( \==\ -    ,_ /|==|  /\ , |/==/\/ _ | 
\ . -  /\==\       |==|-,   _`//==/  /\ ,  )==\ _.\=\.-'/==/ _  ,  /  '.='. -   .' /==/, | |- |\==\ - , / 
 '----`-`--`       `-.`.____.' `--`-`--`--' `--`        `--`------'     `--`--''   `--`./  `--` `--`---'                                                                                                                                                                                                
      """)
        time.sleep(2)
        os.system("cls")
        print(f"""
                             )                  )                    )            (        )                            )   (         
   (        ( /(               ( /(          *   )  ( /(    (       )\ )  ( /(    (     (       *   )  ( /(   )\ )      
 ( )\  (    )\()) (   (   (    )\())    (  ` )  /(  )\())   )\ )   (()/(  )\())   )\    )\    ` )  /(  )\()) (()/( (    
 )((_) )\  ((_)\  )\  )\  )\  ((_)\     )\  ( )(_))((_)\   (()/(    /(_))((_)\  (((_)((((_)(   ( )(_))((_)\   /(_)))\   
((_)_ ((_)  _((_)((_)((_)((_)  _((_) _ ((_)(_(_())   ((_)   /(_))_ (_))    ((_) )\___ )\ _ )\ (_(_())   ((_) (_)) ((_)  
 | _ )| __|| \| |\ \ / / | __|| \| || | | ||_   _|  / _ \  (_)) __||_ _|  / _ \((/ __|(_)_\(_)|_   _|  / _ \ | _ \| __| 
 | _ \| _| | .` | \ V /  | _| | .` || |_| |  | |   | (_) |   | (_ | | |  | (_) || (__  / _ \    | |   | (_) ||   /| _|  
 |___/|___||_|\_|  \_/   |___||_|\_| \___/   |_|    \___/     \___||___|  \___/  \___|/_/ \_\   |_|    \___/ |_|_\|___| 
                                                                                                                        
                        (        )  (        )  (               (                                                                       )                (               ____ 
   (            (       )\ )  ( /(  )\ )  ( /(  )\ )    (       )\ )    (        *   )         (         (                           ( /(   *   )        )\ )    (      |   / 
 ( )\      (    )\     (()/(  )\())(()/(  )\())(()/(    )\     (()/(    )\     ` )  /(    (    )\        )\     (   (   (   (   (    )\())` )  /(    (  (()/(    )\     |  /  
 )((_)     )\((((_)(    /(_))((_)\  /(_))((_)\  /(_))((((_)(    /(_))((((_)(    ( )(_))   )\((((_)(   ((((_)(   )\  )\  )\  )\  )\  ((_)\  ( )(_))   )\  /(_))((((_)(   | /   
((_)_   _ ((_))\ _ )\  (_))   _((_)(_))   _((_)(_))   )\ _ )\  (_))   )\ _ )\  (_(_()) _ ((_))\ _ )\   )\ _ )\ ((_)((_)((_)((_)((_)  _((_)(_(_()) _ ((_)(_))   )\ _ )\  |/    
 / _ \ | | | |(_)_\(_) |_ _| | \| ||_ _| |_  / |_ _|  (_)_\(_) | |    (_)_\(_) |_   _|| | | |(_)_\(_)  (_)_\(_)\ \ / / \ \ / / | __|| \| ||_   _|| | | || _ \  (_)_\(_)(      
| (_) || |_| | / _ \    | |  | .` | | |   / /   | |    / _ \   | |__   / _ \     | |  | |_| | / _ \     / _ \   \ V /   \ V /  | _| | .` |  | |  | |_| ||   /   / _ \  )\     
 \__\_\ \___/ /_/ \_\  |___| |_|\_||___| /___| |___|  /_/ \_\  |____| /_/ \_\    |_|   \___/ /_/ \_\   /_/ \_\   \_/     \_/   |___||_|\_|  |_|   \___/ |_|_\  /_/ \_\((_)                
              
 (    (           *     (      {rossochiaro}(                     (             {rossoscuro}(         (      (        )  (        )  (              (         
 )\ ) )\ )      (  `    )\ )   {rossochiaro})\ )  *   )   (      )\ )  *   )   {rossoscuro})\ )      )\ )   )\ )  ( /(  )\ )  ( /(  )\ )    (      )\ )      
(()/((()/( (    )\))(  (()/(  {rossochiaro}(()/(` )  /(   )\    (()/(` )  /(  {rossoscuro}(()/( (   (()/(  (()/(  )\())(()/(  )\())(()/(    )\    (()/( (    
 /(_))/(_)))\  ((_)()\  /(_))  {rossochiaro}/(_))( )(_))(((_)(   /(_))( )(_))  {rossoscuro}/(_)))\   /(_))  /(_))((_)\  /(_))((_)\  /(_))((((_)(   /(_)))\   
(_)) (_)) ((_) (_()((_)(_))   {rossochiaro}(_)) (_(_()) )\ _ )\ (_)) (_(_())  {rossoscuro}(_)) ((_) (_))   (_))   _((_)(_))   _((_)(_))   )\ _ )\ (_)) ((_)  
| _ \| _ \| __||  \/  ||_ _|  {rossochiaro}/ __||_   _| (_)_\(_)| _ \|_   _|  {rossoscuro}| _ \| __|| _ \  |_ _| | \| ||_ _| |_  / |_ _|  (_)_\(_)| _ \| __| 
|  _/|   /| _| | |\/| | | |   {rossochiaro}\__ \  | |    / _ \  |   /  | |    {rossoscuro}|  _/| _| |   /   | |  | .` | | |   / /   | |    / _ \  |   /| _|  
|_|  |_|_\|___||_|  |_||___|  {rossochiaro}|___/  |_|   /_/ \_\ |_|_\  |_|    {rossoscuro}|_|  |___||_|_\  |___| |_|\_||___| /___| |___|  /_/ \_\ |_|_\|___| 
                                                                                                                                                   
              """)
        input()
        #Schermata di caricamento presa da https://github.com/Amitgajare2/LoadingAnimation
        for i in range(10):
            time.sleep(0.5)
            sys.stdout.write(f"\r  {bianco}Caricamento... " + animation[i % len(animation)])
            sys.stdout.flush()
        print("\r                                                              ")
        print(f"{fg(47)}  CARICAMENTO COMPLETATO!")
        #Chiedo l'username
        username = input(f"\n  {rossoscuro}Inserisci il tuo username: {rossochiaro}")
        print(f"  {rossoscuro}Benvenuto {username} su {rossochiaro}D&D{rossoscuro}!")
        #Chiedo l'età, se l'utente ha meno di 16 anni, non può giocare!
        età = int(input(f"{rossoscuro}  Inserisci età: {rossochiaro}"))
        if età < 16:
            print(f"  {rossoscuro}Devi avere almeno 16 anni per giocare a Dungeons & Dragons!")
            sys.exit()
        #Chiedo se l'utente ha mai giocato a D&D, nel caso gli viene spiegato il gioco.
        giocato = input(f"{rossoscuro}  Hai mai già giocato a Dungeons & Dragons? {rossochiaro}") 
        if giocato.lower() == "si" or giocato.lower() == "s":
            pass
        if giocato.lower() == "no" or giocato.lower() == "n":
            tutorial()
        selettoreclasse()
        
    #Nel caso l'utente prema CTRL + C
    except KeyboardInterrupt:
        print("\n\nProgramma interrotto forzatamente")
menu()