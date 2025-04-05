name = 'Fifa 23'

character = name[0].lower()
new = name.replace(character, '#')
new = character +  new[1:]
print(new)


st1 = 'abc'
st2 = 'xyz'

print(st1,st2)

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")


st1 = 'Dionatha'
st2 = 'Rodrigues'

print(st1,st2)

new_st1 = st2[:3] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")