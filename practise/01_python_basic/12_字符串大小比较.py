"""
字符串进行比较就是基于数字的码值(ASCII码)大小进行比较的。
字符串是按位比较，也就是一位位进行对比，只要有一位大，那么整体就大。
"""

# abc 比较 abd
print(f"abd > abc = {'abd' > 'abc'}")

# a 比较 ab
print(f"ab > a = {'ab' > 'a'}")

# a 比较 A
print(f"a < A = {'a' < 'A'}")
