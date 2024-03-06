# Map_User 

from imports import *

path3 = "E:/Phone pe/pulse/data/map/user/hover/country/india/state/"
map_user_lst = os.listdir(path3)

column3 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "registeredUsers":[],"appOpens":[]}

for state in map_user_lst:
    cur_state = path3+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            D = json.load(data)

            for i in D["data"]["hoverData"].items():
                name = i[0]
                registeredUsers = i[1]["registeredUsers"]
                appOpens = i[1]["appOpens"]

                column3["Districts"].append(name)
                column3["registeredUsers"].append(registeredUsers)
                column3["appOpens"].append(appOpens)
                column3["States"].append(state)
                column3["Years"].append(yr)
                column3["Quarter"].append(int(file.strip(".json")))

map_user_lst = pd.DataFrame(column3)

map_user_lst["States"] = map_user_lst["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user_lst["States"] = map_user_lst["States"].str.replace("-"," ")
map_user_lst["States"] = map_user_lst["States"].str.title()
map_user_lst["States"] = map_user_lst["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

# Map_User table insertion to sql

posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)

curs = posg.cursor()

drop = '''drop table if exists Map_User'''
curs.execute(drop)
posg.commit()



try:
    query = '''Create table if not Exists Map_User(
                                            States varchar(100),
                                            Years varchar(10),
                                            Quarter varchar(10),
                                            Districts varchar(100),
                                            registeredUsers bigint,
                                            appOpens bigint)'''
    curs.execute(query)
    posg.commit()
except:
    print("Map_User Table Already Created")

for index,row in map_user_lst.iterrows():
    query = '''insert into Map_User(
                                            States,
                                            Years,
                                            Quarter,
                                            Districts,
                                            registeredUsers,
                                            appOpens )
                                                    
                values(%s,%s,%s,%s,%s,%s)'''
    
    values = (row['States'],
                row["Years"],
                row["Quarter"],
                row["Districts"],
                row["registeredUsers"],
                row["appOpens"])
        
    try:
        curs.execute(query,values)
        posg.commit()
    except:
        print("Map_User Details Already Inserted")
