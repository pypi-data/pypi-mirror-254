<a name="L5oVV"></a>
## 介绍

laorm尽可能自然语言写法操作数据库，让orm操作pythonic.

<a name="GLD90"></a>
### 方式1 动态查询
直接在模型对象类定义一个方法，上面标注了@sql 
```markdown
方式1 动态查询

@table("sys_user")
class User:
    name:str = FieldDescriptor(primary=True)
    id:str = FieldDescriptor()
    @sql
    def selectByAccountAndPassword(a: int, b: str) -> 'List[User]':pass

# 示例调用
user_count:List[User] = User.selectByAccountAndPassword(1,2)
print(user_count)
或者 User.dynamic('selectByAccountAndPassword',[a,b])
```
<a name="kiYkb"></a>
### 方式2 : api链式
```java
User.select("*").where(name="larry").orderby("id").where(id=18).get()
Use.select("*").where('name',1).match('age',18).get(1)
```
<a name="Op3Kq"></a>
### 方式3：直接执行sql
适合简单情况测试。不想定义模型，快速实现
```markdown
PPA.exec("SELECT * FROM config where id!=1")
```
<a name="SAU33"></a>
## 集成
先进行一定的配置然后调用初始化init_app
<a name="ocGWc"></a>
### 在fastapi中使用
```
from laorm.core.PPA import PPA
from fastapi import FastAPI

class PPAFastAPI(PPA):
    _instance = None

    # 集成主要就是注册对应框架的开启和结束的生命周期
    @classmethod
    def init_app(cls, app: FastAPI, *args):
        if cls._instance is None:
            default_values = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root",
                "db": "study",
                "charset": "utf8mb4",
                "autocommit": True,
            }
            args = {**default_values, **args[0]} if len(args) == 1 else default_values
            cls._instance = cls()
            # 将更新后的args传递给startup方法以便初始化数据库连接池
            cls.startup_params = args
            app.add_event_handler("startup", cls.startup)
            app.add_event_handler("shutdown", cls.shutdown)
```

```
app = FastAPI()
# 初始化 PPAFlask
PPAFlask.init_app(app)
```

<a name="S8mk9"></a>
### 在flask中使用

```
from flask import Flask
from laorm.core.PPA import PPA

class PPAFlask(PPA):
    _instance = None

    @classmethod
    def init_app(cls, app: Flask, *args):
        if cls._instance is None:
            default_values = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root",
                "db": "study",
                "charset": "utf8mb4",
                "autocommit": True,
            }
            args = {**default_values, **args[0]} if len(args) == 1 else default_values
            cls._instance = cls()
            # 将更新后的args传递给startup方法以便初始化数据库连接池
            cls.startup_params = args
            app.before_first_request(cls.startup)
            app.teardown_appcontext(cls.shutdown)
```

```
# 创建 Flask 应用实例
app = Flask()
# 初始化 PPAFlask
PPAFlask.init_app(app, {"host": "your_host", "password": "your_password"})  # 示例参数
```
<a name="JkMUp"></a>
### 在django中使用
Django框架确实内建了一个功能齐全的对象关系映射（ORM）系统。使用自带的orm就成。或者自己处理连接池关闭事件。django没有应用的关闭事件。

<a name="LcqQ3"></a>
## 更多示例
以下展示了在fastapi中crud的示例
```markdown
@table("config")
class Config1:
    id: str = FieldDescriptor(primary=True)
    name: str = FieldDescriptor()

    @sql
    def selectByName(name: str) -> list["Config1"]:
        pass

    # @sql
    # def selectByName(name:str)->'Config1':pass


@router.get("/config2/getdy")
async def getdy():
    res = await Config1.dynamic("selectByIdAndName", [2, 456])
    # res = await Config1.dynamic('selectById',3)
    return {"result": res}


@router.get("/config2/getdy2")
async def getdy2():
    res = await Config1.selectByName(22)
    return {"result": res}


@router.get("/config2/get")
async def get_config2():
    res = await Config1.where(name=22).get()
    return {"result": res}


@router.post("/config2/add")
async def addone():
    await Config1.delete(1)
    await Config1.delete(2)
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    config12 = Config1()
    config12.id = 2
    config12.name = 456
    configlist = [config12]
    await Config1.post(config1)
    await Config1.post(configlist)
    return {"result": "success"}


@router.delete("/config2/delete")
async def deleteone():
    await Config1.delete(1)
    # res = await Config1.where(name=22).delete()
    return {"result": "success"}


@router.delete("/config2/deletedy")
async def deletedy():
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    await Config1.post(config1)
    await Config1.dynamic("deleteById", 1)
    return {"result": "success"}


@router.put("/config2/update")
async def updateone():
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    res = await Config1.where(name=22).update(config1)
    return {"result": res}


@router.get("/config")
async def get_config():
    # 创建并发任务
    tasks = [
        PPA.exec("SELECT * FROM config where id=1"),
        # PPA.exec("SELECT * FROM config where id!={name}",{"name":1}),
        # PPA.exec("SELECT * FROM config where id!=?",[1]),
        # PPA.exec("SELECT * FROM config where id!=?", (1,)),
    ]

    # 并发执行并获取结果
    results = await asyncio.gather(*tasks)
    print(results)
    for i in results:
        print(i[0].get("id"))
```
