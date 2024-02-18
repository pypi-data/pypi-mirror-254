# clickzetta-sqlalchemy


`clickzetta-sqlalchemy` 提供为 SQLAlchemy 提供 ClickZetta Lakehouse 的 dialect 适配，使得以 SQLAlchemy 接口编写的代码或上层应用可以对接到 ClickZetta Lakehouse 上。


本文主要介绍使用 `clickzetta-sqlalchemy` 进行编程的注意事项。


安装
```shell
pip install clickzetta-sqlalchemy
```


## 执行 SQL


```python
from sqlalchemy import create_engine
from sqlalchemy import text


# 建立连接，使用 clickzetta:// 前缀
engine = create_engine("clickzetta://username:password@instance.api.clickzetta.com/workspace?schema=schema&vcluster=default")


sql = text('select * from clickzetta_sample_data.ecommerce_events_history.ecommerce_events_multicategorystore_live;')


# 执行并获取结果
with engine.connect() as conn:
    results = conn.execute(sql)
    for r in results:
        print(r)
```
## 示例一：通过pygwalker对Lakehouse的数据进行可视化分析
[**PyGWalker**](https://github.com/Kanaries/pygwalker)可以将您的 pandas dataframe（和 polars dataframe）转变为 Tableau 风格的用户界面以进行视觉探索，从而简化您的 Jupyter Notebook 数据分析和数据可视化工作流程，而仅需多添加一行代码！




```python
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import pygwalker as pyg


# 建立连接，使用 clickzetta:// 前缀
engine = create_engine("clickzetta://username:password@instance.api.clickzetta.com/workspace?schema=schema&vcluster=default")


# SQLAlchemy 2.0 的 sql 必须使用 sqlalchemy.text 对象构造
sql = text('select * from clickzetta_sample_data.ecommerce_events_history.ecommerce_events_multicategorystore_live;')


# 执行并获取结果
with engine.connect() as conn:
    results = conn.execute(sql)
# 将结果转换为 DataFrame
df = pd.DataFrame(results.fetchall(), columns=results.keys())
df.head(n=5)  # 显示头部前 5 行
df.tail(n=5)  # 显示尾部后5 行
walker = pyg.walk(df)
```



