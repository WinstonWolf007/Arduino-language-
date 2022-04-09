def scare(x, y):
    print(x*"*  ")
    for el in range(y-2):
        print(f'*{((x*3)-4)*" "}*')
    print(x * "*  ")


for x in range(1000):
    scare(x, 1)
