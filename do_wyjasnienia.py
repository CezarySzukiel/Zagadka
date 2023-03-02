users_age = {'alan': 34, 'nikola': 28, 'anna': 25}
new_dict = {(i if i == 'alan' else 'anna') : m for i , m in users_age.items()  if m > 26}
print(new_dict)
#             ^         ^
# jak działa if    i   else   w tym przykładzie i dlaczego ten if na końcu zamienił miejscami wartości w kluczach?
