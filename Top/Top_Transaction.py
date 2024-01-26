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

