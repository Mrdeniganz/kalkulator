# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";

nama = raw_input ("masukan nama : ")
password = raw_input  ("masukan password : ")
if nama == "deniganz" and password == "ganz":
  print "welcome"
elif nama == "user1" and password == "user1":
  print "welcome"
elif nama == "user2" and password == "user2":
  print "hay welcome"
else:
  print "sapa lu woy"
  sys.exit()
print ""
print ""
print O+"create by : MrDs/Deniiganz"
print P+"contant me : 081274083829"
print R+"kalkulatorrRecode"
print R+"bissmilah dulu cuy:v"
print O+"============================="
print O+"  ///////        ///////"
print B+"    //  //   // //   // ///////"
print B+"   //  //   // /////// //   //"
print R+"  //  /////// //   // //   //"
print R+"============================="
print R+"    ////,   /////"
print P+"   //  //  //"
print P+"  //  //  /////"
print G+" /// //     //"
print G+"/////`  /////"
print G+"============================="
print "author: Deniganz"
print "kalkulator buat praktik"

# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu operasi
print ("pilih operasi boedjank")
print ("1.jumlah")
print ("2.kurang")
print ("3.kali")
print ("4.bagi")

# meminta input dari user
choice = input("masukan pilihan(1/2/3/4): ")

num1 = int(input("masukan bilangan pertama: "))
num2 = int(input("masukan bilangan kedua: "))

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("input salah goblok kuretakan jantung kau")

