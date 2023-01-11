''' ___0. Variable Scale Test

'''

class Test:
    def function(self):
        foo = -float('inf')
        lis = []

        def loop(n, foo):
            for i in range(4):
                if i > foo:
                    # print("$$$ foo =", foo)
                    foo = i
                    # print("@@@ foo =", foo)
                    lis.append(i)

        print("Before loop() ->: ", foo, lis)    # Output: -inf []
        loop(3, foo)
        print("after loop() ->: ", foo, lis)     # 我以为的: 3    [0, 1, 2, 3]
                                                 # 实际输出：-inf [0, 1, 2, 3]
        return

class Test_v2:
    def function(self):
        self.foo = -float('inf')
        lis = []

        def loop(n):
            for i in range(4):
                if i > self.foo:
                    # print("$$$ foo =", foo)
                    self.foo = i
                    # print("@@@ foo =", foo)
                    lis.append(i)

        print("Before loop() ->: ", self.foo, lis)    # Output: -inf []
        loop(3)
        print("after loop() ->: ", self.foo, lis)     # 我以为的: 3    [0, 1, 2, 3]
                                                 # 实际输出：-inf [0, 1, 2, 3]
        return

import collections
from collections import deque

def main():
    t = Test()
    t.function()

    t2 = Test_v2()
    t2.function()

    # print(dir(collections))
    # print(len(dir(collections)))
    # # Follows are output
    # lis = ['ChainMap', 'Counter', 'Mapping', 'MutableMapping', 'OrderedDict', 'UserDict', 'UserList', 'UserString', '_Link', '_OrderedDictItemsView', '_OrderedDictKeysView', '_OrderedDictValuesView', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_chain', '_collections_abc', '_count_elements', '_eq', '_heapq', '_iskeyword', '_itemgetter', '_nt_itemgetters', '_proxy', '_recursive_repr', '_repeat', '_starmap', '_sys', 'abc', 'defaultdict', 'deque', 'namedtuple']
    # print(len(lis))
    # q = collections.deque()
    
    # point = collections.namedtuple('Points', ['x', 'y'])
    # p1 = point(2, 3)
    # p2 = point(4, 2)

    # print(p1) # Points(x=2, y=3)
    # print(p2) # Points(x=4, y=2)

    # # 使用 _make 赋值

    # a= [11, 3]
    # p1._make(a)
    # print(p1) # Points(x=11, y=3)
    # # 使用 _replace 更改值

    # p1._replace(x=5)
    # print(p1) # Points(x=5, y=3)

    # print(isinstance(p1, point)) # True
    # print(isinstance(p2, tuple)) # True

    # q = deque(['a', 'b', 'c'], maxlen=10)
    # q.append('d')			                    #### 从右边添加一个元素
    # print(q) 		                    # deque(['a', 'b', 'c', 'd'], maxlen=10)

    # print(q.popleft()) 	                # a	    ### 从左边删除一个元素
    # print(q) 		                    # deque(['b', 'c', 'd'], maxlen=10)

    # q.extend(['i', 'j', 'c', 'd'])      # 从右边扩展队列
    # print(q)			                # deque(['b', 'c', 'd', 'i', 'j', 'c', 'd'], maxlen=10)

    # print(q.index('c'))	                # 1	    #### 查找该元素首次出现的下标 NOT 5 or [1, 5]

    # q.remove('d')                               #### 移除第一个'd' (从左到右遍历查询)
    # print(q)                            # deque(['b', 'c', 'i', 'j', 'c', 'd'], maxlen=10)

    # q.reverse()                                 #### 逆序
    # print(q) 		                    # deque(['d', 'c', 'j', 'i', 'c', 'b'], maxlen=10)

    # print(q.maxlen) 		            # 10	### 最大长度



main()