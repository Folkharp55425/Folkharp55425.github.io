"""
namn = "Matteus"
nummer = 2

nummer2 = 8

nummer3 = nummer + nummer2

print("hej! skriv (x * y) / z")

nummer = input()
nummer1 = input()

nummer2 = int(nummer) * int(nummer1)

nummer3 = input()

print(int(nummer2) / int(nummer3))
"""
"""
nummer = int(input())

if nummer < 10:
    print("Nummret är mindre än 10")

if nummer > 10:
    print("Nummret är större än 10")

if nummer == 10:
    print("Nummret är 10")

if nummer < 10:
    print("Nummret är mindre än 10")
elif nummer > 10:
    print("Nummret är större än 10")
else: 
    print("Nummret är 10")
"""
nummer1 = int(input())
nummer2 = int(input())

if nummer1 < 100:
    print(nummer1 * nummer2)
elif nummer1 > 100:
    print(nummer1 / nummer2)
else:
    print("skriv första nummret som högre eller lägre än 100")