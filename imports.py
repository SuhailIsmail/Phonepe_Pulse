import  os
import json
import pandas as pd
import psycopg2 as ps
import requests
from pprint import pprint
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from Conn_sql import *