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