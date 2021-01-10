#列表和元组
#数据结构：以某种方式（如通过编号）组合起来的数据元素（如数、字符乃至其他数据结构）集合。
#最基本的数据结构为序列。序列中的每个元素都有编号，即其位置或索引，其中第一个元素的索引是0，从0开始指出相对于序列开头的偏移量。用负索引表示序列末尾元素的位置。
#常用的序列有两种：元组和列表。元组是一种特殊的序列，类似于列表，只是不能修改。
#另一种常用的序列是字符串。
#列表可以修改，元组不可以修改。这意味着列表可以中途修改，而元组禁止修改序列。有些内置函数出于此原因返回元组。
#在自己编写程序的时候，几乎在所有情况下都可以使用列表来替代元组。但是有一个例外，是将元组用作字典键。
#容器基本上就是可以包含其他对象的对象。两种主要的容器是序列（元组和列表）和映射（字典）。
#在序列中，每个元素都有编号，而在映射中，每个元素都有名称（也叫键）。有一种既不是序列也不是映射的容器是集合（set）。
#通用序列操作：索引、切片、相加、相乘和成员资格检查。
#字符串是由字符组成的序列。但是python没有专门用来表示字符的类型，因此一个字符就是只包含一个元素的字符串。
#索引：[编号]
#序列字面量索引和赋给变量后索引的效果是一样的。
#切片：[编号:编号:步长]
#切片的第一个索引是包含的第一个元素的编号，第二个索引是切片后余下的第一个元素的编号。
#如果切片的第一个索引位于第二个索引的后面，则结果为空序列。
#步长可以为负数，不过此时第一个索引是终点，第二个索引是起点。
#序列相加：可以用加法运算符来拼接序列。一般而言，不能拼接不同类型的序列。
#乘法：将序列和数x相乘，将重复这个序列x次来创建一个新序列。
#None表示什么都没有，空列表是使用不包含任何内容的两个方括号表示。
#成员资格：要检查特定的值是否包含在序列中，可使用运算符in。它检查是否满足指定的条件，并返回相应的值，满足时返回True,不满足时返回False。这样的运算符称为布尔运算符，真值称为布尔值。
#字符串包含的字符是其的成员或元素。
#内置函数len、min、max。len函数返回序列包含的元素的个数,min和max分别返回序列中最小和最大的元素。
#列表是可变的，即可修改其内容。另外列表有许多特有的方法。
#list类，可将任何序列作为list的实参，转换成列表。
#
