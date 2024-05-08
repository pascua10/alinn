listaa= [1,2,3,4,5,6,7,8,9,10]

def funct(a,*args):
  a.extend(args)
  return a

b = funct(listaa,11,12,13,14,15,16,17)
print(b)

def func2(**kwargs):
  print(f"Numele meu este {kwargs['nume']} si am {kwargs['varsta']} ani")

func2(nume="Ion",varsta=23)




    
        


            
    