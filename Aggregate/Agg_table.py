from Conn_sql import *


#Aggregated_transsaction
curs.execute("select * from aggregate_transaction;")
posg.commit()
table1 = curs.fetchall()
Aggre_transaction = pd.DataFrame(table1,columns = ("States", "Years", "Quarter", 
                                                   "Transaction_type", "Transaction_count", 
                                                   "Transaction_amount"))

#Aggregated_user
curs.execute("select * from aggregate_user")
posg.commit()
table2 = curs.fetchall()
Aggre_user = pd.DataFrame(table2,columns = ("States", "Years", "Quarter", 
                                            "Brands", "Transaction_count", 
                                            "Percentage"))


