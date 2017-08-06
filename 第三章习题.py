# -*- coding:utf-8 -*-

print '>>>>>>>>>>3-1,2,3>>>>>>>>>>'
a = ['Bob','Jack','Tom']
b= ['bike','car','text']
for aa in range(3):
    print a[aa]
    print 'hello '+a[aa]+' !'
    print 'I would like take '+b[aa]
print '>>>>>>>>>>3-4,5,6,7>>>>>>>>>>'
for aa in a:
    if aa == 'Tom':
        print "Tom can't"
    else:
        print 'eat diner with '+aa
print 'I get a bigger desk'
a.insert(0,'Jim')
#在开头插入一个元素
a.insert(2,'Sim')
#在中间插入一个元素
a.append('Penny')
#在末尾插入元素
for aa in a:
    print 'eat diner with '+aa
print 'sorry,i can eat dinner with two person tonigeht!'
print a[1:3]
a.pop(0)
a.pop(2)
a.pop(2)
a.pop(2)
for aa in a:
    print 'eat diner with '+aa
del a[0]
del a[0]
print a

print '>>>>>>>>>>3-8,9,10>>>>>>>>>>'
b=['beijing','shanghai','tianjin','guangzhou','qingdao','guilin']
print b
print sorted(b)
#sorted()不会改变b只是临时排序
print b
b.reverse()
print b
b.sort()
print b
b.sort(reverse=True)
print b
print 'i eat dinner with '+ str(len(a)) +' person'
print '3-10'
pass

print '>>>>>>>>>3-11>>>>>>>>>>>'
pass
