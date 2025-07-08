from config import connection_pool

def fetch_x():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT x_value FROM datapoint;")
        xValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("fetch x Error")
    return xValue

def fetch_y():
    try:
        conn = connection_pool.getconn()
        if conn:
            print("connected")
        cur = conn.cursor()
        cur.execute("SELECT y_value FROM datapoint;")
        yValue = cur.fetchall()
        cur.close()
        connection_pool.putconn(conn)
    except:
        print("fetch y Error")
    return yValue
