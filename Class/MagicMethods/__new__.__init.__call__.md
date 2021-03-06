

### 文档

- [Python 之 \__new__() 方法与实例化](http://www.cnblogs.com/ifantastic/p/3175735.html)
- [详解Python中的__init__和__new__](http://python.jobbole.com/86506/)

- [python \__call__ 函数](http://www.cnblogs.com/lovemo1314/archive/2011/04/29/2032871.html)
- [Python \__new__ 、\__init__、 \__call__](http://2057.iteye.com/blog/1837026)



\__new__() 是在新式类中新出现的方法，它作用在构造方法建造实例之前，
可以这么理解，在 Python 中存在于类里面的构造方法 \__init__() 负责将类的实例化，
而在 \__init__() 启动之前，\__new__() 决定是否要使用该 \__init__() 方法，
因为__new__() 可以调用其他类的构造方法或者直接返回别的对象来作为本类的实例。

如果将类比喻为工厂，那么__init__()方法则是该工厂的生产工人，
\__init__()方法接受的初始化参数则是生产所需原料，
\__init__()方法会按照方法中的语句负责将原料加工成实例以供工厂出货。
而__new__()则是生产部经理，
\__new__()方法可以决定是否将原料提供给该生产部工人，
同时它还决定着出货产品是否为该生产部的产品，因为这名经理可以借该工厂的名义向客户出售完全不是该工厂的产品。


**\__new__() 方法的特性：**
> **\__new__() 方法是在类准备将自身实例化时调用。**
> **\__new__() 方法始终都是类的静态方法，即使没有被加上静态方法装饰器。**


**\__call__**
 
Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。