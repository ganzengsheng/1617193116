Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'gzs': 1617193116}
>>> dict1
{'gzs': 1617193116}
>>> dict1['gzs']
1617193116
>>> dict1['gzs']=16171931160
>>> dict1['gzs']
16171931160L
>>> dict1['gzs']
16171931160L
>>> dict1['gzs']=161
>>> dict1['gzs']
161
>>> del dict1['gzs']
>>> dict1
{}
>>> users = {
	'A':{
		'first':'yu',
		'last':'lei',
		'location':'hs',
		},
	}
>>> for username, userinfo in users.items ():
	print("userid:" + username)
	print("userinfo:" + userinfo)

	
userid:A

Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    print("userinfo:" + userinfo)
TypeError: cannot concatenate 'str' and 'dict' objects
>>> 
>>> for username, userinfo in users.items()
SyntaxError: invalid syntax
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>>  users = {
    'A':{
    'first':'yu',
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}
 
  File "<pyshell#39>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>>  users = {
	'A':{
		'first':'yu',
		'last':'lei',
		'location':'hs',
		},
	'B':{
		'first':'liu',
		'last':'wei',
		'location':'hs',
		},
	}
 
  File "<pyshell#40>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>> users = {
	'A':{
		'first':'yu',
		'last':'lei',
		'location':'hs',
		},
	'B':{
		'first':'liu',
		'last':'wei',
		'location':'hs',
		},
	}
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
>>> dict = {'Name':'gzs','Age': 20}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>>  for key in dict.keys():
	print key
	
  File "<pyshell#58>", line 2
    for key in dict.keys():
    ^
IndentationError: unexpected indent
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
20
gzs
>>> 
