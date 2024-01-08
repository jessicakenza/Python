#Bloc try
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

  #Bloc finally
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")