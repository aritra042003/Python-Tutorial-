# s1="mysirg education services"
# s2='1234'
# print(type(s1))
# print(len(s1))
# print(s1.index('i'))
# print(s1.index('sir'))
# print(s1.count('i'))
# print(s1.startswith('my'))
# print(s1.endswith('services'))
# print(s2.isdigit())
# print(s1.isupper())
# print(s1.islower())
# print(s1.upper())
# print(s1.replace('m','M'))
# print(s1.replace('i','I',s1.count('i')))

# a,b=10,20
# s3="sum of {} and {} is {}"
# print(s3.format(a,b,a+b))
# s4="sum of {2} and {1} is {0}"
# print(s4.format(a,b,a+b))


# s1="mysirg education services private limited"
# print(s1.split(' '))
# s2=input("enter numbers separated by comma")
# l1=s2.split(',')
# print(l1)
# l2=[int(x) for x in l1]
# print(l2)

# l3=[ int(x) for x in input("enter numbers separated by comma").split(',')]
# print(l3)
s1="mysirg education services private limited"
l1=s1.split(' ')
l1
['mysirg', 'education', 'services', 'private', 'limited']
strobj=' '
strobj.join(l1)
'mysirg education services private limited'
'-'.join(l1)
'mysirg-education-services-private-limited'
