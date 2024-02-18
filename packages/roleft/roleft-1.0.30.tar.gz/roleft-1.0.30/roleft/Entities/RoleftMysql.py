# from typing import TypeVar
import pymysql
from roleft.Entities.RoleftMpn import EatDictable

from roleft.Enumerable.RoleftList import xList
# from roleft import xList
# from Module1.RoleftMpn import EatDictable

# T = TypeVar("T")

class DbConfig4Mysql(EatDictable):
    def __init__(self, host: str='', port: int=0, db: str='', user: str='', pwd: str='') -> None:
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.pwd = pwd

class QueryObject4Mysql:
    def __init__(self, cfg: DbConfig4Mysql) -> None:
        self._cfg = cfg

    def _get_conn(self):
        cfg = self._cfg
        return pymysql.connect(
            host=cfg.host,
            port=cfg.port,
            db=cfg.db,
            user=cfg.user,
            password=cfg.pwd,
        )

    def execute_query(self, sql: str, params: dict={}):
        conn = self._get_conn()
        cursor = conn.cursor()

        affected = cursor.execute(sql, params)
        conn.commit()
        conn.close()
        return affected

    def query_mpns(self, sql: str, params: dict = {}) -> xList[dict]:
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute(sql, params)
        cols = cur.description
        records = cur.fetchall()
        mpns = xList[dict]()

        for item in records:
            mpn = {}
            for i in range(len(cols) - 1):
                mpn[cols[i][0]] = item[i]
            mpns.Add(mpn)

        conn.close()
        return mpns

    # def query_mpns_new[T: EatDictable](self, sql: str, params: dict = {}):
    #     items = self.query_mpns(sql, params)
    #     mpns = list[T]()
        
    #     for x in items.ToList():
    #         item: T = T()
    #         mpns.append(item.EatDict(x))

    #     return mpns

