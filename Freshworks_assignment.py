import time
import csv

def create(key,value,timeout=0):
    d=[]
    with open('Freshworks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            d.append(row[0])
    if key in d:
        print("KEY ALREADY EXISTS!") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout!=0:
                    timeout=time.time()+timeout
                if len(str(key))<=32: 
                    print("VALUE CREATED")
                    with open('freshworks.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([key, value, timeout])
            else:
                print("MEMORY LIMIT EXCEEDED!! ")
        else:
            print("INVALID KEY NAME!! KEY MUST CONTAIN ALPHABETS")

def read(key):
    d=[]
    with open('Freshworks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            d.append(row[0])
            if row[0]==key:
                value=row[1]
                timeout=row[2]
    if key not in d:
        print("KEY DOES NOT EXIST IN DATABASE") 
    else:
        if float(timeout)!=0:
            if time.time()<float(timeout): 
                result=key+":"+str(value) 
                print(result)
            else:
                print("KEY HAS EXPIRED") 
        else:
            result=key+":"+str(value)
            print(result)

def delete(key):
    d=[]
    lines=[]
    with open('Freshworks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            d.append(row[0])
            if row[0]==key:
                value=row[1]
                timeout=row[2]
            else:
                lines.append(row)
    if key not in d:
        print("KEY DOES NOT EXIST IN DATABASE")
    #else:
     #   return 0
    if float(timeout)!=0:
            if time.time()>float(timeout):
                print("KEY HAS EXPIRED") 
      #      else:
       #         return 0
    with open('Freshworks.csv', 'w', newline='') as file:
            for i in lines:
                writer = csv.writer(file)
                writer.writerow([i[0], i[1], i[2]])
            print("VALUE DELETED")
