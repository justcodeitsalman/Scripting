#!/usr/bin/python3

import cx_Oracle

template={"TEST1":18949,"TEST2":252}

try:
    def get_connection():
        connection = cx_Oracle.connect(user="", password='',dsn="",encoding="UTF-8")
        return connection
except :
    print("Connection unsuccessfull")
else:
    print("connection Successfull")


def output_type_handler(cursor, name, default_type, size, precision, scale):
    if default_type == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if default_type == cx_Oracle.DB_TYPE_BLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)

def  get_xml(template_id):
      con = get_connection()
      cursor=con.cursor()
      con.outputtypehandler = output_type_handler
      #cursor.execute("select KCI_EVENT_MESSAGE_XML from ksu_message where ksu_message_id=4649430519")
      for name,temp_id in template.items():
          sql="""select sysdate from dual"""
 
           cursor.execute(sql, [temp_id,1])
           clob_data = cursor.fetchone()
           try:
                filename=name+".xml"
                with open(filename,'w') as f:
                f.write(clob_data[1])
            except:
                print("file exception")
            
      cursor.close()
      con.close()

def main():
    get_xml(18949)

if __name__=='__main__':
    main()


