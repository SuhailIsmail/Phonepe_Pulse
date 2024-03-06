# Connection for Sql Tables

from imports import *


posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)