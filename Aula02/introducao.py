#coding=utf8

x = 3

if x>0:
    print"x é positivo"
elif x<0:
    print"x é negativo"
else:
    print"x é nulo"
    

for i in range(1,5):
    print i
    
print 'LISTA:'
    
e = ['python','scipy', 2.7]

e.pop(-1)

e.insert(2,'numpy')
e.insert(3,'swift')

e.sort()

for element in e:
    print element
    
print ''
 
print e[-1]
print e[0:2]

print ''

a = {
    'lang':'python',
    'version':'2.7.1'
    }
    
for keys in a:
    print a[keys]
    
m = [[1,2],[3,4]]

print m[0]

print m[0][0]

print ""

r = range(10)

print r

b = [x*x for x in r]

print b

for x in r:
    b.append(x*x)

print b


#Tuplas - não podem ser alteradas 
print ''

a = (1,2,3,4)

print a

b = (3,)

print b

c = ((1,2),(3,4))

print c

print ""
#Conjuntos

s1 = set([1,1,2,3,4])

print s1

s2 = set ((1,1,3,4))

print s2

a = [1,2,3,4,5]

b = set(a)

print b

c = list(b)

print c


print ''
#Dicionario

a ={
    'lang':'pyhton',
    'ver':'2.7.1'
    }

print a
print a['lang']

a['creator'] = 'Rafael'

del a ['ver']

print a