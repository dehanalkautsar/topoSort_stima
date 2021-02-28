#Muhammad Dehan Al Kautsar
#13519200
#Tucil 2 Stima
#Penyusunan Rencana Kuliah dengan Topological Sort (Decrease and Conquer)


grafGlobal = {} #inisialisasi graf mata kuliah berupa type dictionary dalam python
arrayRomawi = ["I   ","II  ","III ","IV  ","V   ","VI  ","VII ","VIII","IX  ","X   "] #arrayRomawi

def isFoundinList(str,list): #melihat apakah sebuah elemen terdapat dalam list (dlm hal ini: values of dictionary)
     found = False
     index = 0
     while (not found and index < len(list)):
          if (str == list[index]):
               found = True
          else:
               index+=1
     return found

def isAllListEmpty(list): #return boolean apakah list values of dictionary empty
     return len(list) == 0

def isAllDictEmpty(dict): #return boolean apakah seluruh values dalam dict empty
     for keys in dict:
          if (not isAllListEmpty(dict[keys])):
               return False
     return True

def searchCandidate(dict): #return keys, mencari kandidat pertama yang akan dihapus dari dict
     for keys in dict:
          if (isAllListEmpty(dict[keys])):
               return keys

def graphLength(dict): #panjang dict -> banyaknya keys
     return len(dict)

def removeEdges(dict, str): #menghapus sisi yg sudah tidak diperlukan (dalam ini elemen dalam values of dict)
     for keys in dict:
          if (isFoundinList(str,dict[keys])):
               dict[keys].remove(str)

def countEmptyEdges(dict): #menghitung banyaknya graf yg memiliki sisi masuk 0
     count = 0
     for i in dict:
          if (len(dict[i]) == 0):
               count += 1
     return count

def saveEmptyEdges(dict): #mencatat keys apa saja yang mempunyai 0 value.
     arrayTemps = []
     for keys in dict:
          if (len(dict[keys]) == 0):
               arrayTemps.append(keys)
     return arrayTemps

print("               o -------------------------------- o")
print("               |  ▀█▀ █▀█ █▀█ █▀█ █▀ █▀█ █▀█ ▀█▀  |")
print("               |  ░█░ █▄█ █▀▀ █▄█ ▄█ █▄█ █▀▄ ░█░  |")
print("               o -------------------------------- o")
print()
filename = str(input("Nama File: ")) #input file
f = open("../test/"+filename,"r")

for lines in f:
     for line in lines.splitlines():
          sentence = line.replace(",", "").replace(".","") #koma dan titik dihilangkan
          tempMatkulPrereq = [] #inisialisasi array sebagai penampung elemen yang akan diassign ke keys value
          for word in sentence.split():
               tempMatkulPrereq.append(word) #memasukkan sentences per line ke array
          if (len(tempMatkulPrereq) > 1):
               grafGlobal.update({tempMatkulPrereq[0] : tempMatkulPrereq[1:]}) #apabila mempunyai value
          else:
               grafGlobal.update({tempMatkulPrereq[0] : []}) #apabila tidak mempunyai value

######################################
#|        ~Buat Test-Test~          |#
#| print(type(grafGlobal["C1"]))    |#
#| print(grafGlobal)                |#
#| print(isAllDictEmpty(grafGlobal))|#
######################################

countSemester = 1 #untuk keperluan mencatat semester

print()
print("---------------------------------------------------------------------")
print("              \ö/  Here are your courses plan!  \ö/")
print("---------------------------------------------------------------------")
while (countSemester <= 10 and  graphLength(grafGlobal) > 0): #asumsi semester hanya sampai X
     print(">  Semester "+arrayRomawi[countSemester-1]+": ", end="")

     countMatkul = countEmptyEdges(grafGlobal)              #hitung matkul untuk keperluan print 
     arrayCandidateToLose = saveEmptyEdges(grafGlobal)      #catat matkul untuk keperluan print -> conquer

     while (countMatkul > 0):
          candidateKey = arrayCandidateToLose[0]       #diambil satu persatu, hingga arrayCandidateToLose kosong
          removeEdges(grafGlobal, candidateKey)        #erase edges -> decrease
          grafGlobal.pop(candidateKey)                 #erase key -> decrease
          arrayCandidateToLose.pop(0)                  #elemen arrayCandidateToLose dihilangkan satu persatu 
          
          #keperluan print agar elok
          if (countMatkul != 1):
               print(candidateKey, end=", ")
          elif (len(grafGlobal) == 0):
               print(candidateKey+".")
          else:
               print(candidateKey)

          countMatkul -= 1
     
     countSemester += 1


print("---------------------------------------------------------------------")
print("                 \ö/ Hope you are doing well \ö/")
print("---------------------------------------------------------------------")

#last algorithm updated : 2021/02/25 22:12
