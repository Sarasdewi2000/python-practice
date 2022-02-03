#if
i = 7
if(i==10):
	print("ini adalah angka 10")

#else if
i = 5
if (i==10):
	print ("ini adalah angka 10")
else:	
	print("bukan angka 10")
  
#elif
i = 3
if(i==5):
  	print("ini adalah angka 5")
elif(i>5):
	print("lebih besar dari 5")
else:
	print("lebih kecil dari 5")
  
  
#nested-if
i = 2
if (i<7):
	print("nilai i kurang dari 7")
	if (i<3):
	  	print ("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")

