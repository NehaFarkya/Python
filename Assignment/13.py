n=input('enter a number:')
string_repr = str(n)
print 'first number',string_repr[0]
print 'last number',string_repr[-1]
print 'swapping',int(string_repr[-1] + string_repr[1:-1] + string_repr[0])
