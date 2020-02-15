# import json
# # # 将字典数据转换成JSON编码的字符串
# data = {'phone':'187499039310','type':1}
# json_str = json.dumps(data)
# print(json_str)
# print (type (json_str))

# # 将Json编码的字符串转换成字典数据
# import json
# data = '{"phone":"2930-0-8-28340","type":1}'
# json_dict = json.loads(data)
# print (json_dict)
# print(type(json_dict))

# data = {'phone':'187499039310','type':1}
# # 判断字典中是否有key“in/not in dict”
# print('phone' in data)
# print('mobilephone'not in data)

# # 字典键值迭代器：获取一个字典中所有的键值对数据
# print(data.items()) #循环可遍历的（键，值）元组列表：dict_items([('phone', '187499039310'), ('type', 1)])
# for tuple_data in data.items():
#     print(tuple_data)# ('phone', '187499039310')  ('type', 1)
# for key ,value in data.items():#获取key和value元组的值
#     print (key,value) #phone 187499039310  type 1


# import json
# data1 = '{"phone":"2940","type":1}'
# json_dict = eval(data1)
# print (json_dict)
# print(type(json_dict))

# import json
# data2 = {"phone":"218293781870340","type":1}
# print(isinstance(data2,(dict,list))) 
# print(isinstance(data2,list)) #False
# print(isinstance(data2,dict))

# s1 = set([1, 1, 2, 2, 3, 3])
# print(s1) #{1, 2, 3}
# s2 = set([2, 3, 4])
# print(s1 & s2) #{2, 3}
# print(s1 | s2) # {1, 2, 3, 4}

# print (set ([1,2,3,4]).issubset(set([1,2]))) #False
# print (set ([3,4]).issubset(set([1,2,3,4]))) #True


# str.startswith(str,Beg = 0,end=len(string))
# str:要检测的字符串 Beg：可选参数，用于设置字符串检测的起始位置  end：可选参数，用于设置字符串的结束位置。
# str.endswith(suffix[,start[,end]])
# suffix：可以是一个字符串或者元素
# str = "this is string example....WOW!!!"
# print(str.startswith('this'))
# print(str.startswith('string',8))
# print(str.startswith('i',2,3))
# print(str.endswith('!!!'))
# print(str.endswith('h',0,1))


print('{} {}'.format('hello','world')) #不带数字  hello world
print('{0} {1}'.format('hello','world'))#带数字编号  hello world
print('{0} {1} {0}'.format('hello','world'))#打乱顺序 hello world hello
print('{a} {tom} {a}'.format(tom='hello',a='world'))#带关键字 world hello world




