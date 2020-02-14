import json
# # 将字典数据转换成JSON编码的字符串
data = {'phone':'187499039310','type':1}
json_str = json.dumps(data)
print(json_str)
print (type (json_str))

# # 将Json编码的字符串转换成字典数据
import json
data = '{"phone":"2930-0-8-28340","type":1}'
json_dict = json.loads(data)
print (json_dict)
print(type(json_dict))

data = {'phone':'187499039310','type':1}
# 判断字典中是否有key“in/not in dict”
print('phone' in data)
print('mobilephone'not in data)

# 字典键值迭代器：获取一个字典中所有的键值对数据
print(data.items()) #循环可遍历的（键，值）元组列表：dict_items([('phone', '187499039310'), ('type', 1)])
for tuple_data in data.items():
    print(tuple_data)# ('phone', '187499039310')  ('type', 1)
for key ,value in data.items():#获取key和value元组的值
    print (key,value) #phone 187499039310  type 1
