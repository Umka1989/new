import psycopg2
from contextlib import closing

set_psswrd_query = """
update users set password_hash = '{0}' where rb = '{1}'
"""

select_psswrd_query = """select password_hash from users where rb = '{0}'"""

select_position_query = """select position from users where rb = '{0}'"""

user_exists_query = """select rb from users where rb = '{0}'"""

def get_connection (db_name, db_user_name, host_, password_):
    conn = psycopg2.connect(
        dbname = db_name,
        user = db_user_name,
        host = host_,
        password = password_
    )
    return conn

def select_query(query, rb):
    with closing(get_connection('postgres', 'postgres', 'localhost', '11235813')) as conn, closing(conn.cursor()) as cur:
        cur.execute(query.format(rb))
        res = cur.fetchone()[0]
        return res

def update_query(query, rb, psswrd):
    with closing(get_connection('postgres', 'postgres', 'localhost', '11235813')) as conn, closing(conn.cursor()) as cur:
        cur.execute(query.format(psswrd, rb))
        conn.commit()

if __name__ == '__main__':
    res = select_query(user_exists_query,'37')
    print (res)
