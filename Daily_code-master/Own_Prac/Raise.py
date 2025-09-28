 #x = -5
# if x < 0: 
#  raise valueError('x should be postive')

#raise is a manuall way to throw the exception 


try:
  num = int("abc")
except valueError as e:
  print("caught an error",e)
