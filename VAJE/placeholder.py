#cela števila int
x=5
y=15
z=-10


print(x+y)
print(x-y)
print(x*z)
print(x/z)

#deljenje z ostankom
print(10%2)
print(11%2)


#potenca
print(10**3)

#celo številsko //
print(10//3)


# decimalna (float) števila

x=3.14
y=10.012


print(0.5+0.5==1)
print(0.1+0.2==0.3)


# string

ime = "Luka"
print(len(ime))

naslov="kifričrva 55"
print(naslov.lower())


ime ="Žan Kunstič"
imeupper= ime.upper()
kratice=imeupper[0]+". "+imeupper[4]+"."
splitime=imeupper.split()
ime1=splitime[0]
pri1=splitime[1]
print(f"{ime1[0]}. {pri1[0]}.")
print(kratice)