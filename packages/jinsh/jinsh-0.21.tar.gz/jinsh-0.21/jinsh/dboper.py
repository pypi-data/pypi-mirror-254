import oracledb
import json
from jinsh import tool

def getPool(user,password,ip,port,name,min,max,increment):
    try:
        pool = oracledb.create_pool(
            user=user,
            password=password,
            dsn="%s:%s/%s" % (ip,port,name),
            min=min,
            max=max,
            increment=increment,
        )
        return pool
    except Exception as e:
        print(e)

def insert(pool,sql,data):
    try:
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.executemany(sql, data, )
            connection.commit()
        return tool.jsonMsg("success",data="",error="")
    except Exception as e:
        print(e)
        return tool.jsonMsg("fail",data="",error=str(e))

def query(pool,sql,data):
    try:
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, data)
                columns = [column[0] for column in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                json_data = json.dumps(data)
                return tool.jsonMsg("success",data=data,error="")
    except Exception as e:
        print(e)
        return tool.jsonMsg("fail", data="", error=str(e))

