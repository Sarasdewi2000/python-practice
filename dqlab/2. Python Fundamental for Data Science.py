#helloworld
print(10*2+5)
print("Academy DQLab")

#comment
print(10*2+5) #fungsi matematika 
print("Academy DQLab") #fungsi mencetak kalimat

#checkdatatype
var_string = "Belajar Python DQLAB"
var_int=10
var_float=3.14
var_list=[1,2,3,4]
var_tuple=("satu","dua","tiga")
var_dict={"nama":"Ali","umur":20}

print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))

#Ifstatement
i = 7
if(i==10):
	print("ini adalah angka 10")
  
i = 5
if (i==10):
	print ("ini adalah angka 10")
else:	
	print("bukan angka 10")
  
i = 3
if (i==5):
  	print("ini adalah angka 5")
elif(i>5):
	print("lebih besar dari 5")
else:
	print("lebih kecil dari 5")

#nested if
i = 2
if (i<7):
	print("nilai i kurang dari 7")
	if (i<3):
	  	print ("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")

 #operatormath
a=10
b=5
selisih = a - b
jumlah = a+b
kali = a*b
bagi = a/b
print("Hasil penjumlahan a dan b adalah",jumlah)
print("Selisih a dan b adalah:", selisih)
print("Hasil perkalian a dan b adalah:",kali)
print("Hasil pembagian a dan b adalah:",bagi)

#modulus
c=10
d=3

modulus=c%d
print("Hasil modulus",modulus)

#task
angka=5

if(angka%2==0):
    print("angka termasuk bilangan genap")
else:
    print("angka termasuk bilangan ganjil")
    
#looping

j= 0
while j<6:
	print("Ini adalah perulangan ke -",j)
	j=j+1
  
for i in range (1,6):
	print("Ini adalah perulangan ke-",i)

for i in range (1,11):
    if(i%2==0):
        print("Angka genap",i)
    else:
         print("Angka ganjil",i)
      
count=[1,2,3,4,5] #elemen list
for number in count: #looping untuk menampilkan semua elemen pada count
    print("Ini adalah element count : ", number) #menampilkan elemen list pada count

#function
def salam():
	print ("Hello, Selamat Pagi")

salam()

#parameters
def luas_segitiga(alas, tinggi):
	luas = (alas*tinggi)/2
	print("Luas segitiga: %f" % luas);

luas_segitiga(4,6)

#return
def luas_segitiga(alas,tinggi):
	luas = (alas*tinggi)/2
	return luas

print ("Luas segitiga: %d" % luas_segitiga(4,6))


#modules
import math as m
print ("Nilai pi adalah:", m.pi)

#import functions
from math import pi
print ("Nilai pi adalah", pi)

#import all functions
from math import *
print ("Nilai e  adalah:", e)

#readfile

import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
     print (row)

# menutup file csv
f.close()

#read
import requests
from contextlib import closing
import csv

url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
		
	reader = csv.reader(f, delimiter=',')
		 
	for row in reader:
		 print (row)

#readfile using pandas
import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)
