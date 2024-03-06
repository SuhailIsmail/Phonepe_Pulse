from imports import *
from Conn_sql import *
from Query import *
from plots import *
from Map.Map_table import *
from Top.Top_table import *
from Aggregate.Agg_table import *


st.set_page_config(page_title= "Phonepe Pulse Data Visualization | By Samuel Solomon",
                   layout= "wide",

                   initial_sidebar_state= "expanded")
with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data"],
            icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
            menu_icon= "menu-button-wide",
            default_index=0,
            styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                    "nav-link-selected": {"background-color": "#6F36AD"}})

if selected == "Home":
    st.title(":blue[Phonepe Pulse Data Visualization and Exploration]")
    st.title(":blue[A User-Friendly Tool Using Streamlit and Plotly]")
    st.header(" ",divider='rainbow')
    
    st.subheader(":blue[This application provides visualisation and plots of phonpe data]")
    st.subheader(":blue[Migrates it to a SQL data warehouse.]")
    st.subheader(":blue[Allows querying]")


if selected == "Top Charts":

        ques= st.selectbox("**Select the Question**",('1. Top Brands Of Mobiles Used','2. States With Lowest Trasaction Amount',
                                  '3. Districts With Highest Transaction Amount','4. Top 10 Districts With Lowest Transaction Amount',
                                  '5. Top 10 States With AppOpens','6. Least 10 States With AppOpens','7. States With Lowest Trasaction Count',
                                 '8. States With Highest Trasaction Count','9. States With Highest Trasaction Amount',
                                 '10. Top 50 Districts With Lowest Transaction Amount'))

        if ques=="1. Top Brands Of Mobiles Used":
                ques1()

        elif ques=="2. States With Lowest Trasaction Amount":
                ques2()

        elif ques=="3. Districts With Highest Transaction Amount":
                ques3()

        elif ques=="4. Top 10 Districts With Lowest Transaction Amount":
                ques4()

        elif ques=="5. Top 10 States With AppOpens":
                ques5()

        elif ques=="6. Least 10 States With AppOpens":
                ques6()

        elif ques=="7. States With Lowest Trasaction Count":
                ques7()

        elif ques=="8. States With Highest Trasaction Count":
                ques8()

        elif ques=="9. States With Highest Trasaction Amount":
                ques9()

        elif ques=="10. Top 50 Districts With Lowest Transaction Amount":
                ques10()

    
# EXPLORE DATA - TRANSACTIONS
if selected == "Explore Data":
    tab1, tab2, tab3= st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:
        method = st.radio("**Select the Analysis Method**",["Transaction Analysis", "User Analysis"])

        if method == "Transaction Analysis":
            col1,col2= st.columns(2)
            with col1:
                years_at= st.slider("**Select the Year**", Aggre_transaction["Years"].min(), Aggre_transaction["Years"].max(),Aggre_transaction["Years"].min())

            df_agg_tran_Y= Y_year(Aggre_transaction,years_at)
            
            col1,col2= st.columns(2)
            with col1:
                quarters_at= st.slider("**Select the Quarter**", df_agg_tran_Y["Quarter"].min(), df_agg_tran_Y["Quarter"].max(),df_agg_tran_Y["Quarter"].min())

            df_agg_tran_Y_Q = Q_yearQ(df_agg_tran_Y, quarters_at)


        elif method == "User Analysis":
            year_au= st.selectbox("Select the Year_AU",Aggre_user["Years"].unique())
            agg_user_Y= Aggre_user_plot_1(Aggre_user,year_au)

            quarter_au= st.selectbox("Select the Quarter_AU",agg_user_Y["Quarter"].unique())
            agg_user_Y_Q= Aggre_user_plot_2(agg_user_Y,quarter_au)


    with tab2:
        method_map = st.radio("**Select the Analysis Method(MAP)**",["Map Transaction Analysis", "Map User Analysis"])

        if method_map == "Map Transaction Analysis":
            col1,col2= st.columns(2)
            with col1:
                years_m2= st.slider("**Select the Year_mi**", Map_transaction["Years"].min(), Map_transaction["Years"].max(),Map_transaction["Years"].min())

            df_map_tran_Y= Y_year(Map_transaction, years_m2)

            
            
            col1,col2= st.columns(2)
            with col1:
                quarters_m2= st.slider("**Select the Quarter_mi**", df_map_tran_Y["Quarter"].min(), df_map_tran_Y["Quarter"].max(),df_map_tran_Y["Quarter"].min())

            df_map_tran_Y_Q= Q_yearQ(df_map_tran_Y, quarters_m2)

        elif method_map == "Map User Analysis":
            col1,col2= st.columns(2)
            with col1:
                year_mu1= st.selectbox("**Select the Year_mu**",Map_user["Years"].unique())
            map_user_Y= map_user_plot_1(Map_user, year_mu1)

            col1,col2= st.columns(2)
            with col1:
                quarter_mu1= st.selectbox("**Select the Quarter_mu**",map_user_Y["Quarter"].unique())
            map_user_Y_Q= map_user_plot_2(map_user_Y,quarter_mu1)

           

    with tab3:
        method_top = st.radio("**Select the Analysis Method(TOP)**",["Top Transaction Analysis", "Top User Analysis"])

        if method_top == "Top Transaction Analysis":
            col1,col2= st.columns(2)
            with col1:
                years_t2= st.slider("**Select the Year_tt**", Top_transaction["Years"].min(), Top_transaction["Years"].max(),Top_transaction["Years"].min())
 
            df_top_tran_Y= Y_year(Top_transaction,years_t2)

            

        elif method_top == "Top User Analysis":
            col1,col2= st.columns(2)
            with col1:
                years_t3= st.selectbox("**Select the Year_tu**", Top_user["Years"].unique())

            df_top_user_Y= top_user_plot_1(Top_user,years_t3)

            


  
                

            