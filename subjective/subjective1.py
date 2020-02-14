# foo = 'foo'
# bar = 'bar'

# # foobar = '%s%s' % (foo, bar) # 可行
# # foobar = '{0}{1}'.format(foo, bar) # 更好
# # foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # 最好
# print('%s%s' % (foo, bar))
# print('{0}{1}'.format(foo, bar))
# print('{foo}{bar}'.format(foo=foo, bar=bar))


# 链接字符串的方法：从不好到好
""" 
字符串是不可变类型。这意味着当需要组合一个 字符串时，将每一部分放到一个可变列表里，使用字符串时再
组合 ('join') 起来的做法更高效
 """

# nums = ""
# for n in range(20):
#     nums += str(n)   # 慢且低效
# print (nums)

# nums = []
# for n in range(20):
#     nums.append(str(n))
# print "".join(nums)  # 更高效

nums = [str(n) for n in range(20)]
print(nums)
print("".join(nums))

# nums = map(str, range(20))
# print "".join(nums)