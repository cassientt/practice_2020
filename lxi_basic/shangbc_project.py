# 导入renamer模块
import renamer
# 赋值变量path
path = 'C:\photo'

# 赋值变量table
table ='C:\拍照顺序.csv'

# 使用set_name()方法，将变量作为参数使图片名匹配表格拍照顺序重命名为相应信息
renamer.set_name(path , table)

# 使用set_files()方法让所有图片文件自动分类
renamer.set_files(path)