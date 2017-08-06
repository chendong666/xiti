# -*- coding:utf-8 -*-
print '>>>>>>>>>>>>>xiti 2-1,2>>>>>>>>>>>>>>>>>>'
a = 'hello,word'
print a
a = 'hello,github'
print a
print '>>>>>>>>>>>>>>xiti 2-3,4>>>>>>>>>>>>>>>>>'
name = raw_input("what's your name?")
print 'hello'+ name +',would you like learn some python today?'
print  'hello'+ name.title() +',would you like learn some python today?'
#title每个单词首字母大写
print 'hello'+ name.upper() +',would you like learn some python today?'
#字符串全部大写
print 'hello'+ name.lower() +',would you like learn some python today?'
#字符串全部小写
print '>>>>>>>>>>>>>>>xiti 2-5,6,7,10,11>>>>>>>>>>>>>>>>'
import this
a = 'Albert Einstien once said, "A person who never made a mistake never tried anything new."'
print a
famous_person =  a[0:15]
message = a[28:-1]
print famous_person + message
a = '\t albert einstien\n '
print a
print a.lstrip() #去掉开头空白
print a.rstrip() #去掉结尾空白
print a.strip()  #去掉开头和结尾空白
print '>>>>>>>>>>>>>>>xiti 2-8,9>>>>>>>>>>>>>>>>'
print  4+4
print  9-1
print  8*1
print 16/2
a = 8
b = 'my favorite number is '+ str(a)+'.'
print b
