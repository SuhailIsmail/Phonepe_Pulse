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