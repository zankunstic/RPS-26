
def hello():
    x=input("Vnesi svoj razred: ")
    if x.lower() == "1.ri":
        print(f"hello {x} ♥")
    else:
        print(f"helo {x}")


def poštevanka():
    x=int(input("vnesi število ki želiš poštevanko:  "))
    i=1
    while i!=11:
        print(x*i)
        i+=1
    print()
    for i in range(1,11):
        print(f"{i} * {x} = {i*x}")



if __name__ == "__main__":
    poštevanka()