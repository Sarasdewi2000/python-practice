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
