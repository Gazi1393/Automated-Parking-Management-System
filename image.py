import cv2
import matplotlib.pyplot as  plt
import sys
import mysql.connector as mc
def main():
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret = False


    img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    plt.imshow(img1)
    plt.title("Car Image")
    plt.xticks([])
    plt.yticks([])
    plt.show()


    try:
        conn = mc.connect(host='localhost', user='root', password='', db='car_park_master')

    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)



    sql_insert_query = """ INSERT INTO user
                              (picture) VALUES (%s)"""
    cursor = conn.cursor()


    result = cursor.execute(sql_insert_query, frame)
    conn.commit()
    cursor.close()
    conn.close()




    cap.release()



if _name_ == "_main_":
    main()