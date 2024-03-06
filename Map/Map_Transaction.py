# Map_Transaction

from imports import *

path2 = "E:/Phone pe/pulse/data/map/transaction/hover/country/india/state/"
map_tran_lst = os.listdir(path2)

column2 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Amount":[],"Transaction_count":[]}

for state in map_tran_lst:
    cur_state = path2+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            C = json.load(data)
            for i in C["data"]["hoverDataList"]:
                    name = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]

                    column2["Districts"].append(name)
                    column2["Transaction_count"].append(count)
                    column2["Amount"].append(amount)
                    column2["States"].append(state)
                    column2["Years"].append(yr)
                    column2["Quarter"].append(int(file.strip(".json")))
            
map_tran_lst = pd.DataFrame(column2)

map_tran_lst["States"] = map_tran_lst["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_tran_lst["States"] = map_tran_lst["States"].str.replace("-"," ")
map_tran_lst["States"] = map_tran_lst["States"].str.title()
map_tran_lst["States"] = map_tran_lst["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")
            
# Map_Transaction table insertion to sql

posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)

curs = posg.cursor()

drop = '''drop table if exists Map_Transaction'''
curs.execute(drop)
posg.commit()



try:
    query = '''Create table if not Exists Map_Transaction(
                                            States varchar(100),
                                            Years int,
                                            Quarter int,
                                            Districts varchar(100),
                                            Amount bigint,
                                            Transaction_count bigint)'''
    curs.execute(query)
    posg.commit()
except:
    print("Map_Transaction Table Already Created")

for index,row in map_tran_lst.iterrows():
    query = '''insert into Map_Transaction(
                                            States,
                                            Years,
                                            Quarter,
                                            Districts,
                                            Amount,
                                            Transaction_count )
                                                    
                values(%s,%s,%s,%s,%s,%s)'''
    
    values = (row['States'],
                row["Years"],
                row["Quarter"],
                row["Districts"],
                row["Amount"],
                row["Transaction_count"])
        
    try:
        curs.execute(query,values)
        posg.commit()
    except:
        print("Map_Transaction Details Already Inserted")


            