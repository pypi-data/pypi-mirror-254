import pron

with open('test.pron', 'r') as fp:
    obj = pron.load(fp)

print(type(obj))
print()
print(pron.dumps(obj))
print()
print(pron.dumps(obj, indent=4))
print()
print(pron.dumps(obj, indent=4, suppress=[list]))
print()
print(pron.dumps(obj, indent=4, suppress=[list, tuple]))
print()
