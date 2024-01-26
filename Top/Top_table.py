from Conn_sql import *

#Top_transaction
curs.execute("select * from top_transaction")
posg.commit()
table5 = curs.fetchall()
Top_transaction = pd.DataFrame(table5,columns = ("States", "Years", "Quarter", 
                                                 "Districts", "Transaction_amount",
                                                 "Transaction_count"))

#Top_user
curs.execute("select * from top_user")
posg.commit()
table6 = curs.fetchall()
Top_user = pd.DataFrame(table6, columns = ("States", "Years", "Quarter", 
                                           "Districts", "RegisteredUser"))

