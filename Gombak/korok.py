korok=[]
for i in range(1,6):
    kor=int(input(f"Hanyadik: {i} Adj meg kort 0-120 között:"))
    korok.append(kor)


print(":".join(str(k) for k in korok))

index=0
for k_r in korok:
    if k_r > 70:
        index=korok.index(k_r)
        break

print(f"Első idős ember korának helye a listában: {index}")
with open("oreg.txt","w",encoding='utf-8') as f:
    f.write(f"Első idős ember korának helye a listában: {index}")
print("Sikeres volt a fájlbaírás!")


    
