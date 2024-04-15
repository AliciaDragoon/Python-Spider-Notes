-- sql语句单行注释
-- 创建表格
create table stu(
	stu_no int(10) primary key auto_increment,
	-- 第一列是主键，自动增加
	name varchar(30) not null,
	-- varchar 字符串
	gender varchar(10) not null,
	birthday date,
	address varchar(255) 
);
-- ;表示结束
-- 1,增加数据
-- insert into table_name(列1,列2,列3...) values(值1,值2,值3...);
-- 2,删除数据
-- delete from table_name;
-- 删除整个表
-- delete from table_name where 条件;
-- 按条件删除
-- 3,修改数据
-- update table_name set 列1=值1,列2=值2,列3=值3... where 条件;
-- 4,查询数据
-- select * from table_name;
-- 全表查询
-- select 列1,列2,列3... from table_name;
-- select 列1 as `别名1`,列2 as `别名2`,列3... from table_name;
-- 查询某个表的某几个列

-- where条件
-- where 列 = 值
-- select * from stu where name = '李华';
-- select * from stu where name = '李华' and gender = '男';
-- 与
-- select * from stu where name = '李华' or gender = '男';
-- 或
-- select * from stu where gender != '男';
-- 非
-- select * from stu where age >= 25;
-- >,>=,<,<=,=
-- select * from stu where age between 23 and 15;
-- 模糊搜索
-- select * from stu where name like '李%';
-- 查询所有name有'李'的数据
-- select * from stu where address like '%192%';

-- 分组查询
-- select 班级名称, avg(成绩) from 表 where 课 = '语文' group by 班;
-- select address, avg(age) from stu group by address;
-- sql脚本执行时，会根据by后面的列进行分组
-- avg()是个聚合函数。还有sum ，min，max，count。
-- select address, max(age), min(age), avg(age) from stu group by address;
-- having
-- 在分组，聚合之后再查询
-- select address, avg(age) from stu group by address having avg(age) > 18;

-- 排序
-- select * from stu order by age;
-- select * from stu order by age desc;

-- 分页查询
-- select * from stu limit 3;
-- 查询前三条数据
-- select * from stu limit 3, 8;
-- 从第三条开始，数8个