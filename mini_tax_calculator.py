import math



print ("ΥΠΟΛΟΓΙΣΜΟΣ ΦΟΡΟΥ ΕΙΣΟΔΗΜΑΤΟΣ")

print ("")
print ("")
e = int ( input ( " Δωσε τo εισόδημα : " ) )

if e == 1000:
  print("Εχετε μηδενικό φόρο")
elif e <= 2000:
  f=(e*5)/100
  print("ο φόρος είναι ",f)
elif e <= 3000:
  f=(e*10)/100
  print("ο φόρος είναι ",f)
elif e >3000:
  f1=(e*14)
  f=f1/100
  print("ο φόρος είναι ",f)


    









