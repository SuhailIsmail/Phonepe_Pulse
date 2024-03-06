#Top_Transaction 

from imports import *


path4 = "E:/Phone pe/pulse/data/top/transaction/country/india/state/"
Top_tran_lst = os.listdir(path4)

column4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Amount":[],"Transaction_count":[]}

for state in Top_tran_lst:
    cur_state = path4+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            E = json.load(data)

            for i in E["data"]["districts"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]

                column4["Districts"].append(name)
                column4["Transaction_count"].append(count)
                column4["Amount"].append(amount)
                column4["States"].append(state)
                column4["Years"].append(yr)
                column4["Quarter"].append(int(file.strip(".json")))

Top_tran_lst = pd.DataFrame(column4)

Top_tran_lst["States"] = Top_tran_lst["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Top_tran_lst["States"] = Top_tran_lst["States"].str.replace("-"," ")
Top_tran_lst["States"] = Top_tran_lst["States"].str.title()
Top_tran_lst["States"] = Top_tran_lst["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

# Top_Transaction table insertion to sql

posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)

curs = posg.cursor()

drop = '''drop table if exists Top_Transaction'''
curs.execute(drop)
posg.commit()



try:
    query = '''Create table if not Exists Top_Transaction(
                                            States varchar(100),
                                            Years varchar(10),
                                            Quarter varchar(10),
                                            Districts varchar(100),
                                            Amount bigint,
                                            Transaction_count bigint)'''
    curs.execute(query)
    posg.commit()
except:
    print("Top_Transaction Table Already Created")

for index,row in Top_tran_lst.iterrows():
    query = '''insert into Top_Transaction(
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
        print("Top_Transaction Details Already Inserted")


=======
#Top_Transaction 

from imports import *


path4 = "E:/Phone pe/pulse/data/top/transaction/country/india/state/"
Top_tran_lst = os.listdir(path4)

column4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Amount":[],"Transaction_count":[]}

for state in Top_tran_lst:
    cur_state = path4+state+"/"
    Agg_yr = os.listdir(cur_state)
    
    for yr in Agg_yr:
        cur_yr = cur_state+yr+"/"
        Agg_yr_lst = os.listdir(cur_yr)

        for file in Agg_yr_lst:
            cur_file = cur_yr+file
            data = open(cur_file, "r")
            
            E = json.load(data)

            for i in E["data"]["districts"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]

                column4["Districts"].append(name)
                column4["Transaction_count"].append(count)
                column4["Amount"].append(amount)
                column4["States"].append(state)
                column4["Years"].append(yr)
                column4["Quarter"].append(int(file.strip(".json")))

Top_tran_lst = pd.DataFrame(column4)

>>>>>>> 22caaa4fa472436115b5648e25f845b3ee187730
