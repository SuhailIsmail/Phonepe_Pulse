# Aggregate_Transaction
#----------------------------------------------------------------------------------------------------

from imports import *
from Conn_sql import *

path = "E:/Phone pe/pulse/data/aggregated/transaction/country/india/state/"
Agg_tran_list = os.listdir(path)

column = {"States":[], "Years":[], "Quarters":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}
for state in Agg_tran_list:
    cur_state = path+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            A = json.load(data)

            for i in A["data"]["transactionData"]:
                name = i["name"]
                type = i["paymentInstruments"][0]["type"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                column["Transaction_type"].append(type)
                column["Transaction_count"].append(count)
                column["Transaction_amount"].append(amount)
                column["States"].append(state)
                column["Years"].append(yr)
                column["Quarters"].append(int(file.strip(".json")))

Aggregate_Transaction = pd.DataFrame(column)
     

     
# Aggregate_Transaction table insertion to sql
#--------------------------------------------------------------------------------

# drop = '''drop table if exists Aggregate_Transaction'''
# curs.execute(drop)
# posg.commit()

# try:
#     query = '''Create table if not Exists Aggregate_transaction(
#                                             States varchar(100),
#                                             Years int,
#                                             Quarters int,
#                                             Transaction_type varchar(30),
#                                             Transaction_count bigint,
#                                             Transaction_amount bigint)'''
#     curs.execute(query)
#     posg.commit()
# except:
#     print("Aggregate_Transaction Table Already Created")

# for index,row in Aggregate_Transaction.iterrows():
#     query = '''insert into Aggregate_Transaction(
#                                             States,
#                                             Years,
#                                             Quarters,
#                                             Transaction_type,
#                                             Transaction_count,
#                                             Transaction_amount )
                                                    
#                 values(%s,%s,%s,%s,%s,%s)'''
    
#     values = (row['States'],
#                 row["Years"],
#                 row["Quarters"],
#                 row["Transaction_type"],
#                 row["Transaction_count"],
#                 row["Transaction_amount"])
        
#     try:
#         curs.execute(query,values)
#         posg.commit()
#     except:
#         print("Aggregate_Transaction Details Already Inserted")


     
