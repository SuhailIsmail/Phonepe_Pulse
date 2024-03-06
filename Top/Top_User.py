#Top_User

from imports import *

path5 = "E:/Phone pe/pulse/data/top/user/country/india/state/"
Top_user_lst = os.listdir(path5)

column5 = {"States":[], "Years":[], "Quarter":[], "Districts":[],"registeredUsers":[]}

for state in Top_user_lst:
    cur_state = path5+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            G = json.load(data)

            for i in G["data"]["districts"]:
                name = i["name"]
                registeredUsers = i["registeredUsers"]

                column5["Districts"].append(name)
                column5["registeredUsers"].append(registeredUsers)
                column5["States"].append(state)
                column5["Years"].append(yr)
                column5["Quarter"].append(int(file.strip(".json")))

Top_user_lst =  pd.DataFrame(column5)


Top_user_lst["States"] = Top_user_lst["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_user_lst["States"] = Top_user_lst["States"].str.replace("-"," ")
Top_user_lst["States"] = Top_user_lst["States"].str.title()
Top_user_lst["States"] = Top_user_lst["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

# Top_User table insertion to sql

# posg = ps.connect(
#     host = "localhost",
#     user = "postgres",
#     password = "root3",
#     database = "Phonepe_Pulse",
#     port = "5432"
# )

# curs = posg.cursor()

# drop = '''drop table if exists Top_User'''
# curs.execute(drop)
# posg.commit()

# column5 = {"States":[], "Years":[], "Quarter":[], "Districts":[],"registeredUsers":[]}

# try:
#     query = '''Create table if not Exists Top_User(
#                                             States varchar(100),
#                                             Years varchar(10),
#                                             Quarter varchar(10),
#                                             Districts varchar(100),
#                                             registeredUsers bigint)'''
#     curs.execute(query)
#     posg.commit()
# except:
#     print("Top_User Table Already Created")

# for index,row in Top_user_lst.iterrows():
#     query = '''insert into Top_User(
#                                             States,
#                                             Years,
#                                             Quarter,
#                                             Districts,
#                                             registeredUsers)
                                                    
#                 values(%s,%s,%s,%s,%s)'''
    
#     values = (row['States'],
#                 row["Years"],
#                 row["Quarter"],
#                 row["Districts"],
#                 row["registeredUsers"])
        
#     try:
#         curs.execute(query,values)
#         posg.commit()
#     except:
#         print("Top_User Details Already Inserted")

