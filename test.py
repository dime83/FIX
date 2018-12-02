FIXVer='FIX.4.2'
print(FIXVer)

my_dict={'FIX.4.2' : 'THIS FILE'}
print(my_dict['FIX.4.2'])

if FIXVer in my_dict:
    print("YAY")
else:
    print("NAY")
