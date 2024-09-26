# Docs

~~(真的有必要吗)~~

class **HomoNumberExpr**(homoNumCursed: str = '114514', auto_calc: bool = True, table_load_fp: TextIOWrapper | None = None)

恶臭数字论证器主类

参数

+ homoNumCursed: str

    要论证的数字，默认为 `114514`

+ auto_calc: bool *(Optional)*

    自动生成缓存表，在对象构建的时候，以及更改要论证的数字的时候

    缓存表是一张包含该数字只用一个得到的所有可能组合出来的表达式（当然不全，测试过）

+ table_load_fp: TextIOWrapper *(Optional)*

    缓存表的文件对象，用于加载缓存表

    如果该参数不为 `None`，则不会构建新的缓存表

def **SaveHomoCalcTable**(table_save_fp: TextIOWrapper) -> None

保存缓存表到文件对象

+ table_save_fp: TextIOWrapper

    文件对象，用于保存缓存表

def **SetHomoNum**(homo_num: str = '114514') -> None

设置新的论证数字

如果 `auto_calc` 为 `True`，则会自动更新计算缓存表。

def **UpdateHomoCalcTable**() -> None

手动更新缓存表

def **Homo**(_num: str) -> str

论证（）


```
# 论证1145141919810

Homo > 1919810
1+1-4+5+1-4+1919810
Homo > 4294967295
11*4*5*141*9*19*810-114*514-1919*810+1+1+451+419+19-810
Homo > 5201314
11+45*1*4*19*19*8*10+1145-14+1*9*198-10
```
