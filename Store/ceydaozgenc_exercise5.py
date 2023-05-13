data = open("store-data.txt","r")
totalsales = open("store-sales.txt","r")
onesales = totalsales.read().split("=")
divide = data.read().split("\n")
for x in range(len(onesales)) :
    total=0
    sales = onesales[x].split("\n")
    print("****** Bert's Buurtiwinkel ******")
    print("Artice \t\t\t\tPrice")
    for y in range(len(sales)):
        for i in range(len(divide)) :
            barcode = divide[i].split("\t")
            if len(sales[y])==13:
                if barcode[0]==sales[y]:
                    print(barcode[1]+"\t\t"+barcode[2])
                    total+=float(barcode[2])
    print("\n>>>>>>>>>>>> To be paid:", round(total,2),"\n\n***** Thank you for your business *****\n")
