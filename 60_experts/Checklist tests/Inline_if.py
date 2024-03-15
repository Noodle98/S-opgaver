# Eksempel:
# Kør programmet og leg med koden
q = "a" if 3 > 8 else "b"
print(q)
my_array = [2, 3, 5, 10, 8]
new_array = [x if x > 5 else 1 for x in my_array]
for x in new_array:
    print(x)