<<<<<<< HEAD
# Connection for Sql Tables

from imports import *


posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)

=======
# Connection for Sql Tables

from imports import *


posg = ps.connect(
    host = "localhost",
    user = "postgres",
    password = "root3",
    database = "Phonepe_Pulse",
    port = "5432"
)

>>>>>>> 22caaa4fa472436115b5648e25f845b3ee187730
curs = posg.cursor()