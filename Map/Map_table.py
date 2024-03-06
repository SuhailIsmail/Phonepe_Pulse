from Conn_sql import *


#Map_transaction
curs.execute("select * from map_transaction")
posg.commit()
table3 = curs.fetchall()
Map_transaction = pd.DataFrame(table3,columns = ("States", "Years", "Quarter", 
                                                 "Districts", "Transaction_amount",
                                                 "Transaction_count"))

#Map_user
curs.execute("select * from map_user")
posg.commit()
table4 = curs.fetchall()
Map_user = pd.DataFrame(table4,columns = ("States", "Years", "Quarter",
                                          "Districts", "RegisteredUser", 
                                          "AppOpens"))

