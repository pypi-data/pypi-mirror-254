import time
from typing import Union
from robertcommonio.system.io.sqlalche import SQLAlCheAccessor
from robertcommonbasic.basic.os.file import check_file_exist
from encodings.aliases import aliases as encodings_aliases
import sqlite3
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def test_sqlite():
    accessor = SQLAlCheAccessor()
    accessor.add_engine('sqlite0', 'sqlite+pysqlite:///:memory:')
    accessor.execute_sql('sqlite0', 'CREATE TABLE some_table (x int, y int)')
    accessor.execute_sql('sqlite0', 'INSERT INTO some_table (x,y) VALUES (:x, :y)', [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
    print(accessor.read_sql('sqlite0', 'SELECT * FROM some_table'))


def test_sqlite1():
    accessor = SQLAlCheAccessor()
    accessor.add_engine('sqlite0', 'sqlite:///config.db')
    accessor.execute_sql('sqlite0', 'CREATE TABLE some_table (x int, y int)')
    accessor.execute_sql('sqlite0', 'INSERT INTO some_table (x,y) VALUES (:x, :y)', [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
    print(accessor.read_sql('sqlite0', 'SELECT * FROM some_table'))


def test_sqlite2():
    db = '/data/config.db'
    print(check_file_exist(db))
    accessor = SQLAlCheAccessor()
    accessor.add_engine('sqlite0', f'sqlite:///{db}?check_same_thread=False')
    print(accessor.read_sql('sqlite0', 'SELECT * FROM task'))


def convert(content: Union[str, bytes]):
    print(f"{type(content)} {content}")
    if isinstance(content, str):
        return content
    try:
        return content.decode(encoding='gbk', errors='ignore')  # lambda x: unicode(x, 'utf-8', 'ignore')
    except:
        try:
            return content.decode(encoding='utf-8', errors='ignore')
        except:
            encodings = set(encodings_aliases.values())
            for encoding in encodings:
                if encoding not in ['gbk', 'utf-8']:
                    try:
                        return content.decode(encoding=encoding, errors='ignore')
                    except:
                        pass
    return str(content)


def test_sqlite3():
    db = 'E:/gzwjd.4db'
    print(check_file_exist(db))
    accessor = SQLAlCheAccessor()
    accessor.add_engine('sqlite0', f"sqlite:///{db}?check_same_thread=False", text_factory=lambda x: convert(x))
    rows = accessor.read_sql('sqlite0', 'SELECT distinct elementName FROM page_contain_elements')
    print(rows)


def test_mysql():
    accessor = SQLAlCheAccessor()
    accessor.add_engine('mysql0', 'mysql+pymysql://root:RNB.beop-2013@localhost/beopdata')

    print(accessor.read_sql('mysql0', 'SELECT * FROM some_table'))

    records = [{"A": 1, "B": 1, "C": 5.2, "D": "2021-07-23 00:00:00"}, {"A": 2, "B": 3, "C": 4.2, "D": "2021-07-25 00:00:00"}]
    cmds = accessor.generate_sql_cmds('some_table', records, 'replace', list(records[0].keys()))

    print(accessor.execute_multi_sql('mysql0', cmds))

    print(accessor.read_sql('mysql0', 'SELECT * FROM some_table'))

    record_update = [{"A": 1, "B": 1, "C": 5.2, "D": "2021-07-23 01:00:00"}, {"A": 2, "B": 3, "C": 4.2, "D": "2021-07-25 01:00:00"}]
    cmd_update = accessor.generate_sql_cmds('some_table', record_update, 'update', ["B", "C", "D"], ["A"])

    print(accessor.execute_multi_sql('mysql0', cmd_update))

    print(accessor.read_sql('mysql0', 'SELECT * FROM some_table'))

    print()


def test_oracle():
    accessor = SQLAlCheAccessor()
    accessor.add_engine('oracle0', 'oracle://cy2003:goen_cy2003@10.192.1.216:1521/gc', engine_pool_recycle=300)

    r = accessor.read_sql('oracle0', 'SELECT * FROM ACT')
    time.sleep(60)
    print(accessor.read_sql('oracle0', 'SELECT * FROM ACT'))

    records = [{"ID": '1512005962', "CNTR_NO": "123"}, {"ID": '1512005970', "CNTR_NO": "234"}]
    cmds = accessor.generate_sql_cmds('action_syn1', records, 'replace', list(records[0].keys()), ['ID'])

    # print(accessor.execute_multi_sql('oracle0', cmds))

    print()


def test_syn_oracle():
    accessor = SQLAlCheAccessor()
    accessor.add_engine('oracle0', 'oracle://XX:XX@10.192.1.250:1521/gc')
    accessor.add_engine('oracle1', 'oracle://XX:XX@10.192.1.216:1521/gc')

    r = accessor.read_sql('oracle0', 'SELECT * FROM action_syn1 where date_out is null')

    records = [{"ID": '1512005962', "CNTR_NO": "123"}, {"ID": '1512005970', "CNTR_NO": "234"}]
    cmds = accessor.generate_sql_cmds('action_syn1', records, 'replace', list(records[0].keys()), ['ID'])

    print(accessor.execute_multi_sql('oracle0', cmds))

    print(accessor.read_sql('mysql0', 'SELECT * FROM some_table'))


def test_sqlite4():
    db = 'C:/nginx/resource/1/best.4db'
    db = '1.4db'

    accessor = SQLAlCheAccessor()
    #accessor.add_engine('sqlite0', f"sqlite:///{db}?check_same_thread=False")
    #accessor.add_engine('sqlite0', f"sqlite:///{db}?check_same_thread=False", text_factory=lambda x: convert(x))
    accessor.add_engine('sqlite0', f"sqlite:///{db}?check_same_thread=False", text_factory= lambda x: str(x, 'gbk', 'ignore'))
    rows = accessor.read_sql('sqlite0', 'select * from template_files where id=7')
    rows = accessor.read_sql('sqlite0', 'select id, name, unitproperty01 as group_order from list_pagegroup  where id=19 order by cast(group_order as int)')
    print(rows)


test_sqlite4()