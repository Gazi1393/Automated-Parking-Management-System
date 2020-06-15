import mysql.connector
from mysql.connector import Error
import socket
def table():
    try:
        conn = mysql.connector.connect(host='localhost',
                                 database='car_park_master',
                                 user='root',
                                 password='')
        if conn.is_connected():
           db_Info = conn.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           cursor = conn.cursor()
           cursor.execute("select database();")
           record = cursor.fetchone()
           print ("Your connected to - ", record)
    except Error as e :
        print ("Error while connecting to MySQL", e)
    #finally:
        #closing database connection.
        #if(conn.is_connected()):
            #cursor.close()
            #conn.close()
            #print("MySQL connection is closed")

def main_screen():
    HOST = '127.0.0.1'              # Standard loopback interface address (localhost)
    PORT = 65432               # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            table()
            while True:

                data = conn.recv(1024)


                if not data:
                    break
                conn.sendall(data)



main_screen()