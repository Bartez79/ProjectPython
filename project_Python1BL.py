# -*- coding: utf-8 -*-
import pymysql

class Zawodnik:
    def zawodnik(self):
        self.sql = "SELECT * FROM zawodnik"    
        try:
            self.cursor.execute(self.sql)
            self.results = self.cursor.fetchall()
            print ("id_uczestnik \t Name \t Surname \t Team \t id rejestracja" )
            for row in self.results:
                self.id_uczestnik = row[0]
                self.imie = row[1]
                self.nazwisko = row[2]
                self.zespol = row[3]
                self.id_rejestracja = row[4]                  
                print ("%s \t %s \t %s \t %s \t %s" % (self.id_uczestnik, self.imie, self.nazwisko, self.zespol, self.id_rejestracja))
        except:
            print("Błąd: Nie można wyświetlić danych")
            
class OrganizatorImp(Zawodnik):
    def __init__(self):
        self.conn=pymysql.connect("localhost" ,"root", "bartez79", "imprezy_nowa_2")
        print("polaczono ok")
        self.cursor =self.conn.cursor()    
    def org(self):
        self.sql = "SELECT * FROM org "    
        try:
            self.cursor.execute(self.sql)
            self.results = self.cursor.fetchall()
            print ("id_organizator \t organizator " )
            for row in self.results:
                self.id_organizator = row[0]
                self.organizator = row[1]
                print ("%s \t %s " % (self.id_organizator, self.organizator))
        except:
            print("Błąd: Nie można wyświetlić danych")
    
    def sezon(self):
        
            self.sql = "Select * FROM sezon2017"
            try:
                self.cursor.execute(sql)
                self.results = self.cursor.fetchall()
                print ("id_uczestnik \t Name \t Surname" )
                for row in results:
                    self.id_sezon= row[0]
                    self.id_uczestnik = row[1]
                    self.id_imprezy = row[2]               
                    print ("%s \t %s \t %s" % (self.id_sezon, self.id_uczestnik, self.id_imprezy))
            except:
                print("Błąd: Nie można wyświetlić danych")		

    def sezonInsert(self):
        self.id_uczestnik = input ("Podaj id uczestnika")
        self.id_imprezy= input("Podaj Numer Imprezy")
        self.sql= "insert into Sezon2017 (id_uczestnik,id_imprezy) values("  + self.id_uczestnik  + ", " + self.id_imprezy +");"
        self.cursor.execute("SET foreign_key_checks = 0;")
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        self.conn.commit()
       
        
           
    def sezonUpdate(self):
        self.id_sezon = input ("Podaj id Sezonu")
        self.id_organizator= input ("Podaj id organizatora ")
        self.id_imprezy= input("Podaj Numer Imprezy")
        self.sql= "update Sezon2017 set id_uczestnik =" + self.id_organizator + ", id_imprezy=" + self.id_imprezy + " where id_sezon =" + self.id_sezon + ";"
        self.cursor.execute("SET foreign_key_checks = 0;")
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        self.conn.commit()
        
    
        
class Logowanie(OrganizatorImp):
    def __init__(self):
        self.conn=pymysql.connect("localhost" ,"root", "bartez79", "imprezy_nowa_2")
        print("polaczono ok")
        self.cursor =self.conn.cursor()
        self.login = str(input("Podaj login: "))
        self.zapytanie1 = "SELECT * FROM org;" 
        print('poszlo')
        #WHERE organizator="+self.login+";"
        self.cursor.execute(self.zapytanie1)
        print('poszlo')

        if(self.login == 'SRP' or self.login =='2B Enduro Team' or self.login =='Joy Ride' or self.login == 'EMTB' or self.login == 'Pepiki' or self.login == 'sportaiment'):
            print("Zalogowano orgazatora: "+self.login)
        elif(self.login == 'Roman' or 'Jozef' or 'Christian' or 'Pawel' or 'Jacek' or 'Radoslaw' or 'Piotr' or 'Daniel' or 'Michal' or 'Mariusz' or 'Martin'): 
            print("Zalogowano zawodnika: "+self.login)    
        else:
            print("Blad logowania")
            #Logowanie.zapytanie1(self)        

o1= OrganizatorImp()
o1.sezonUpdate()

