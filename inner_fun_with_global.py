temp = 10 	

def func():
      global temp
      temp = 20  
      print(temp)

print(temp) 	
func() 		
print(temp)