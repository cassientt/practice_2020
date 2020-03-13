## 0.数据库常识
### SQL 是用于访问和处理数据库的标准的计算机语言。(结构化查询语言,使我们有能力访问数据库)
## 重要事项
* SQL 对大小写不敏感
* 些数据库系统要求在每条 SQL 命令的末端使用分号。
分号是在数据库系统中分隔每条 SQL 语句的标准方法，这样就可以在对服务器的相同请求中执行一条以上的语句。

#### SQL 能做什么？
* SQL 面向数据库执行查询
* SQL 可从数据库取回数据
* SQL 可在数据库中插入新的记录
* SQL 可更新数据库中的数据
* SQL 可从数据库删除记录
* SQL 可创建新数据库
* SQL 可在数据库中创建新表
* SQL 可在数据库中创建存储过程
* SQL 可在数据库中创建视图
* SQL 可以设置表、存储过程和视图的权限

##### 存在着很多不同版本的 SQL 语言，但是为了与 ANSI(美国国家标准化组织) 标准相兼容，它们必须以相似的方式共同地来支持一些主要的关键词（比如 SELECT、UPDATE、DELETE、INSERT、WHERE 等等）。

## 0.0.1 数据操作语言 (DML) 和 数据定义语言 (DDL)。
SQL (结构化查询语言)是用于执行查询的语法。但是 SQL 语言也包含用于更新、插入和删除记录的语法。
### 查询和更新指令构成了SQL的DML 部分：
* SELECT - 从数据库表中获取数据
* UPDATE - 更新数据库表中的数据
* DELETE - 从数据库表中删除数据
* INSERT INTO - 向数据库表中插入数据
### SQL 最重要的DDL语句:
SQL 的数据定义语言 (DDL) 部分使我们有能力创建或删除表格。我们也可以定义索引（键），规定表之间的链接，以及施加表间的约束。
* CREATE DATABASE - 创建新数据库
* ALTER DATABASE - 修改数据库
* CREATE TABLE - 创建新表
* ALTER TABLE - 变更（改变）数据库表
* DROP TABLE - 删除表
* CREATE INDEX - 创建索引（搜索键）
* DROP INDEX - 删除索引
##  0.1.0 数据库基础
###  0.1.1 SQL SELECT 语句
SELECT 语句用于从表中选取数据。结果被存储在一个结果表中（称为结果集）。
```sql
SQL SELECT 语法:
SELECT 列名称 FROM 表名称   [选择指定列]
SELECT * FROM 表名称    [选择所有列]
备注：星号（*）是选取所有列的快捷方式。
```
#### 0.1.2 SELECT DISTINCT 语句
* 在表中，可能会包含重复值。这并不成问题，不过，有时您也许希望仅仅列出不（distinct）的值。
```sql
语法：
SELECT DISTINCT 列名称 FROM 表名称
```
#### 0.1.3 SQL WHERE 子句
* WHERE 子句用于规定选择的标准。
* 如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句。
```sql
语法:
SELECT 列名称 FROM 表名称 WHERE 列 运算符 值
```
##### 下面的运算符可在 WHERE 子句中使用：
操作符 | 描述
-------|-----
= | 等于
<>(操作符 <> 可以写为 !=) | 不等于
> | 大于
< | 小于
>= | 大于等于
<= | 小于等于
BETWEEN | 在某个范围内
LIKE | 搜索某种模式
#### 引号的使用:
* 请注意，我们在例子中的条件值周围使用的是单引号。
* SQL 使用单引号来环绕文本值（大部分数据库系统也接受双引号）。如果是数值，请不要使用引号。
```sql
example:
SELECT * FROM Persons WHERE FirstName='Bush'
SELECT * FROM Persons WHERE Year>1965
```
### 0.1.4 SQL AND & OR 运算符
* AND 和 OR 运算符用于基于一个以上的条件对记录进行过滤。
* 可在 WHERE 子语句中把两个或多个条件结合起来。
* 如果第一个条件和第二个条件都成立，则 AND 运算符显示一条记录。
* 如果第一个条件和第二个条件中只要有一个成立，则 OR 运算符显示一条记录。
```sql
SELECT * FROM Persons WHERE (FirstName='Thomas' OR FirstName='William')
AND LastName='Carter'
```
### 0.1.5 SQL ORDER BY 子句
* ORDER BY 语句用于对结果集进行排序。 根据指定的列对结果集进行排序。
* ORDER BY 语句默认按照升序对记录进行排序。如果您希望按照降序对记录进行排序，可以使用 DESC 关键字。
```sql
SELECT Company, OrderNumber FROM Orders ORDER BY Company, OrderNumber
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC
```

### 0.2.0 SQL INSERT INTO 语句

```sql
INSERT INTO 语句用于向表格中插入新的行。
语法
INSERT INTO 表名称 VALUES (值1, 值2,....)
我们也可以指定所要插入数据的列：
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
```

### 0.3.0 SQL UPDATE 语句
```sql
Update 语句用于修改表中的数据。

语法：
UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值

example:
更新某一行中的一个列
UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson' 
更新某一行中的若干列
UPDATE Person SET Address = 'Zhongshan 23', City = 'Nanjing'
WHERE LastName = 'Wilson'
```
### SQL DELETE 语句
```sql
DELETE 语句用于删除表中的行。
语法:
DELETE FROM 表名称 WHERE 列名称 = 值

删除所有行
可以在不删除表的情况下删除所有的行。这意味着表的结构、属性和索引都是完整的：

DELETE FROM table_name
或者：

DELETE * FROM table_name
```


## 1. SQL函数
* SQL 拥有很多可用于计数和计算的内建函数。
```sql
内建函数的语法：

SELECT function(列) FROM 表
```
#### 在 SQL 中，基本的函数类型和种类有若干种。函数的基本类型是：
### 1.1  Aggregate
* Aggregate 函数(合计函数)：函数的操作面向一系列的值，并返回一个单一的值。

函数 | 描述
---------|-----------
AVG(column) | 	返回某列的平均值
COUNT(column) |	返回某列的行数（不包括 NULL 值）
COUNT(*) | 返回被选行数
FIRST(column) | 返回在指定的域中第一个记录的值
LAST(column) | 返回在指定的域中最后一个记录的值
MAX(column) | 返回某列的最高值
MIN(column) | 返回某列的最低值	 
SUM(column) | 返回某列的总和

####  1.1.1 SQL AVG 函数
####  AVG 函数返回数值列的平均值。NULL 值不包括在计算中。
```sql
语法：

SELECT AVG(column_name) FROM table_name

example：

SELECT AVG(OrderPrice) AS OrderAverage FROM Orders

SELECT Customer FROM Orders
WHERE OrderPrice>(SELECT AVG(OrderPrice) FROM Orders)
```

####  1.1.2 count（）函数
```sql
SELECT terminal FROM android.terminal_upgrade_group_device WHERE groupId = 352;   
统计获得设备列表

SELECT COUNT(terminal) FROM android.terminal_upgrade_group_device WHERE groupId = 352;  
统计出设备列表的总数量，并以COUNT(terminal)做为对应的列名

SELECT COUNT(*) FROM android.terminal_upgrade_group_device WHERE groupId = 352;
统计出设备列表的总数量，但无列名，以COUNT(*)做为对应的列名

SELECT COUNT(*) AS totaldevices FROM android.terminal_upgrade_group_device WHERE groupId = 352;
统计出设备列表的总数量，使用totaldevices做为“列别名”
```
#### 对应的参数区别
* COUNT(列名) 函数返回指定列的值的数目（NULL 值不计入），但COUNT(*)统计的是列数，不管是否为空都会加入。
*  COUNT(distinct 列名) 返回指定列的不同值的数目（NULL 值不计入） 。使用distinct有去重的作用。

####  1.1.3 FIRST() 函数
FIRST() 函数返回指定的字段中第一个记录的值。
* 提示：可使用 ORDER BY 语句对记录进行排序。
```sql
SQL FIRST() 语法:
SELECT FIRST(column_name) FROM table_name
```
####  1.1.4 LAST() 函数
LAST() 函数返回指定的字段中最后一个记录的值。
* 提示：可使用 ORDER BY 语句对记录进行排序。
```sql
SQL LAST() 语法
SELECT LAST(column_name) FROM table_name
``` 
####  1.1.5 MAX() 函数/MIN() 函数
MAX 函数返回一列中的最大值。NULL 值不包括在计算中。
```sql
SQL MAX() 语法
SELECT MAX(column_name) FROM table_name
注释：MIN 和 MAX 也可用于文本列，以获得按字母顺序排列的最高或最低值。
```
####  1.1.6 SUM() 函数
SUM 函数返回数值列的总数（总额）。
```sql
SQL SUM() 语法
SELECT SUM(column_name) FROM table_name
```
####  1.1.7 GROUP BY 语句
* GROUP BY 语句用于结合合计函数，根据一个或多个列对结果集进行分组。
```sql
SQL GROUP BY 语法:
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
```
####  1.1.8 HAVING 子句
在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。
```sql
SQL HAVING 语法
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_function(column_name) operator value
```
### 1.2 Scalar
* Scalar 函数：函数的操作面向某个单一的值，并返回基于输入值的一个单一的值

函数 | 描述
----------|--------
UCASE(c) | 将某个域转换为大写
LCASE(c) | 将某个域转换为小写
MID(c,start[,end]) | 从某个文本域提取字符
LEN(c) | 返回某个文本域的长度
INSTR(c,char) | 返回在某个文本域中指定字符的数值位置
LEFT(c,number_of_char) | 返回某个被请求的文本域的左侧部分
RIGHT(c,number_of_char) | 返回某个被请求的文本域的右侧部分
ROUND(c,decimals) | 对某个数值域进行指定小数位数的四舍五入
MOD(x,y) | 返回除法操作的余数
NOW() | 返回当前的系统日期
FORMAT(c,format) | 改变某个域的显示方式
DATEDIFF(d,date1,date2) | 用于执行日期计算

#### 1.2.1 UCASE() 函数
UCASE 函数把字段的值转换为大写。
```sql
SQL UCASE() 语法
SELECT UCASE(column_name) FROM table_name
```
#### 1.2.2 LCASE() 函数
LCASE 函数把字段的值转换为小写。
```sql
SQL LCASE() 语法
SELECT LCASE(column_name) FROM table_name
```
#### 1.2.3 MID() 函数
MID 函数用于从文本字段中提取字符。
```sql
SQL MID() 语法
SELECT MID(column_name,start[,length]) FROM table_name
```
参数 | 描述
----------|--------
column_name	| 必需。要提取字符的字段。
start | 必需。规定开始位置（起始值是 1）。
length | 可选。要返回的字符数。如果省略，则 MID() 函数返回剩余文本。

#### 1.2.4 LEN() 函数
LEN 函数返回文本字段中值的长度。
```sql
SQL LEN() 语法
SELECT LEN(column_name) FROM table_name
```
#### 1.2.5 ROUND() 函数
ROUND 函数用于把数值字段舍入为指定的小数位数。
```sql
SQL ROUND() 语法
SELECT ROUND(column_name,decimals) FROM table_name
```
参数 | 描述
----------|--------
column_name | 必需。要舍入的字段。
decimals | 必需。规定要返回的小数位数。
#### 1.2.5 NOW() 函数
NOW 函数返回当前的日期和时间。
提示：如果您在使用 Sql Server 数据库，请使用 getdate() 函数来获得当前的日期时间。
```sql
SQL NOW() 语法:

SELECT NOW() FROM table_name

SELECT ProductName, UnitPrice, Now() as PerDate FROM Products

```
#### 1.2.6 FORMAT() 函数
FORMAT 函数用于对字段的显示进行格式化。
```sql
SQL FORMAT() 语法: 

SELECT FORMAT(column_name,format) FROM table_name

SELECT ProductName, UnitPrice, FORMAT(Now(),'YYYY-MM-DD') as PerDate
FROM Products
```
参数 | 描述
----------|--------
column_name | 必需。要格式化的字段。
format | 必需。规定格式




## 数据库连接
* 数据库中的表可通过键将彼此联系起来。主键（Primary Key）是一个列，在这个列中的每一行的值都是唯一的。在表中，每个主键的值都是唯一的。这样做的目的是在不重复每个表中的所有数据的情况下，把表间的数据交叉捆绑在一起。



## SQL 约束 (Constraints)
* 约束用于限制加入表的数据的类型。
* 可以在创建表时规定约束（通过 CREATE TABLE 语句），或者在表创建之后也可以（通过 ALTER TABLE 语句）。
#### 我们将主要探讨以下几种约束：
* NOT NULL：如果不向字段添加值，就无法插入新记录或者更新记录。
* UNIQUE：唯一标识数据库表中的每条记录。UNIQUE 和 PRIMARY KEY 约束均为列或列集合提供了唯一性的保证。PRIMARY KEY 拥有自动定义的 UNIQUE 约束。

请注意，每个表可以有多个 UNIQUE 约束，但是每个表只能有一个 PRIMARY KEY 约束。
* PRIMARY KEY：约束唯一标识数据库表中的每条记录。
主键必须包含唯一的值。主键列不能包含 NULL 值。

每个表都应该有一个主键，并且每个表只能有一个主键。
* FOREIGN KEY：一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY。用于预防破坏表之间连接的动作。也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。
* CHECK：用于限制列中的值的范围。
* DEFAULT：用于向列中插入默认值
## 索引
* CREATE INDEX 语句用于在表中创建索引。
* 在不读取整个表的情况下，索引使数据库应用程序可以更快地查找数据。
索引
* 您可以在表中创建索引，以便更加快速高效地查询数据。用户无法看到索引，它们只能被用来加速搜索/查询。
* 注释：更新一个包含索引的表需要比更新一个没有索引的表更多的时间，这是由于索引本身也需要更新。因此，理想的做法是仅仅在常常被搜索的列（以及表）上面创建索引。
```sql
语法如下：
CREATE INDEX index_name
ON table_name (column_name)
可以为两列创建索引或者以降序索引某个列中的值，您可以在列名称之后添加保留字 DESC
CREATE INDEX PersonIndex
ON Person (LastName, FirstName)
```
## SQL 撤销索引、表以及数据库
* 通过使用 DROP 语句，可以轻松地删除索引、表和数据库（表的结构、属性以及索引也会被删除）
* 请使用 TRUNCATE TABLE 命令（仅仅删除表格中的数据，并不删除表本身）：
## SQL ALTER TABLE 语句
ALTER TABLE 语句用于在已有的表中添加、修改或删除列。
```sql
添加列的语法：

ALTER TABLE table_name
ADD column_name datatype

删除对应列的语法：（某些数据库系统不允许这种在数据库表中删除列的方式 (DROP COLUMN column_name)）

ALTER TABLE table_name 
DROP COLUMN column_name

改变表中列的数据类型：

ALTER TABLE table_name
ALTER COLUMN column_name datatype

```
## SQL AUTO INCREMENT 字段
* Auto-increment 会在新记录插入表中时生成一个唯一的数字。
* 默认地，AUTO_INCREMENT 的开始值是 1，每条新记录递增 1。

## SQL VIEW（视图）
在 SQL 中，视图是基于 SQL 语句的结果集的可视化的表。

## SQL 服务器 - RDBMS
* 现代的 SQL 服务器构建在 RDBMS（Relational Database Management System） 之上。
* DBMS - 数据库管理系统（Database Management System）
数据库管理系统是一种可以访问数据库中数据的计算机程序。
* DBMS 使我们有能力在数据库中提取、修改或者存贮信息。不同的 DBMS 提供不同的函数供查询、提交以及修改数据。
