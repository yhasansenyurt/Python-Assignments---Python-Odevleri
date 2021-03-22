#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A1
#########################################################################################


#########################################################################################
# QUESTION V
# Description: This program uses hash table and it upgrades size of table when you add more slot.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION V:")
print("The objective of this question is to learn hash functions and collision handling.")

class HashTable:
    def __init__(self):
        self.size = 7
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.timer = 0
    def put(self,key,data):
      # This part is resizing the 'self.size'.
      if self.timer >= 7:
          self.slots.append(None)
          self.data.append(None)
      self.timer += 1
      hashvalue = self.hashfunction(key,len(self.slots))
      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace


    def hashfunction(self,astring, tablesize):
        sum = 0
        for pos in range(len(astring)):
            sum = sum + ord(astring[pos])

        return sum % tablesize

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H = HashTable()
H["Abandon"] = "TERK ETMEK"
H["Ability"] = "YETENEK"
H["Able"] = "MUKTEDIR"
H["Aboard"] = "İÇİNDE OLMAK"
H["About"] = "1.HAKKINDA 2.YAKLAŞIK OLARAK"
H["Above"] = "YUKARIDAKİ"
H["Abroad"] = "YURT DIŞI"
H["Absence"] = "YOKLUK"
H["Absent"] = "1.YOK 2.EKSİK"
H["Absolute"] = "MUTLAK, KESİN"
H["Absurd"] = "SAÇMA"
H["Accept"] = "KABUL ETMEKK"
H["Accident"] = "KAZA"
H["Accommodate"] = "YERLEŞTİRMEK"
H["Accommodation"] = "KONAKLAMA YERİ"
H["Accompany"] = "EŞLİK ETMEK"
H["According To"] = "GÖRE"
H["Account"] = "HESAP"
H["Accurate"] = "DOĞRU, HATASIZ"
H["Accuse"] = "SUÇLAMAK"
H["Ache"] = "AĞRI"
H["Acquaint"] = "TANIMAK, BİLMEK"
H["Across"] = "1.BİR UÇTAN DİĞERİNE 2.DİĞER TARAFTA"
H["Act"] = "1.DAVRANIŞ 2.DAVRANMAK"
H["Active"] = "ETKİN,FAAL"
H["Actor"] = "ERKEK OYUNCU"
H["Actress"] = "KADIN OYUNCU"
H["Actual"] = "GERÇEK"
H["Add"] = "TOPLAMAK,EKLEMEK"
H["Address"] = "ADRES"
H["Administration"] = "İDARE"
H["Admire"] = "BEĞENMEK,HAYRAN OLMAK"
H["Admit"] = "1.KABUL ETMEK 2.İZİN VERMEK"
H["Adult"] = "YETİŞKİN"
H["Advance"] = "1.İLERİ 2.AVANS"
H["Advanced"] = "GELİŞMİŞ"
H["Advantage"] = "AVANTAJ"
H["Adventure"] = "MACERA"
H["Advertise"] ="REKLAM YAPMAK,İLAN VERMEK"
H["Advice"] ="TAVSİYE"
H["Advise"] = "TAVSİYE ETMEK"
H["Aerial"] = "ANTEN"
H["Aeroplane"] = "UÇAK"
H["Affair"] ="1.OLAY 2.İŞ 3.İLİŞKİ"
H["Affect"] = "ETKİLEMEK"
H["Afford"] = "SATIN ALMA GÜCÜ OLMAK"
H["Afraid"] = "KORKMAK"
H["After"] = "SONRA"

print(H.slots)
print(H.data)
print(H["Abandon"])
print(H["Able"])
print(H["Affair"])
print(H["Advance"])
