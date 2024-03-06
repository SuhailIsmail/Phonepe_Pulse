# Aggregate_User
#--------------------------------------------------------------------------------------------------

from Conn_sql import *
from imports import *

path1 = "E:/Phone pe/pulse/data/aggregated/user/country/india/state/"
Agg_user_list = os.listdir(path1)

column1 = {"States":[], "Years":[], "Quarter":[], "Brands":[], "Transaction_count":[], "Percentage":[]}

for state in Agg_user_list:
    cur_state = path1+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            B = json.load(data)

            try:
                for i in B["data"]["usersByDevice"]:
                    brand = i["brand"]
                    count = i["count"]
                    percentage = i["percentage"]

                    column1["Brands"].append(brand)
                    column1["Transaction_count"].append(count)
                    column1["Percentage"].append(percentage)
                    column1["States"].append(state)
                    column1["Years"].append(yr)
                    column1["Quarter"].append(int(file.strip(".json")))

            except:
                pass

Aggregate_User =  pd.DataFrame(column1)


# Aggregate_User table insertion to sql
#-----------------------------------------------------------------------------------

# drop = '''drop table if exists Aggregate_User'''
# curs.execute(drop)
# posg.commit()


# try:
#     query = '''Create table if not Exists Aggregate_User(
#                                             States varchar(100),
#                                             Years int,
#                                             Quarter int,
#                                             Brands varchar(50),
#                                             Transaction_count bigint,
#                                             Percentage bigint)'''
#     curs.execute(query)
#     posg.commit()
# except:
#     print("Aggregate_User Table Already Created")

# for index,row in Aggregate_User.iterrows():
#     query = '''insert into Aggregate_User(
#                                             States,
#                                             Years,
#                                             Quarter,
#                                             Brands,
#                                             Transaction_count,
#                                             Percentage )
                                                    
#                 values(%s,%s,%s,%s,%s,%s)'''
    
#     values = (row['States'],
#                 row["Years"],
#                 row["Quarter"],
#                 row["Brands"],
#                 row["Transaction_count"],
#                 row["Percentage"])
        
#     try:
#         curs.execute(query,values)
#         posg.commit()
#     except:
#         print("Aggregate_User Details Already Inserted")


