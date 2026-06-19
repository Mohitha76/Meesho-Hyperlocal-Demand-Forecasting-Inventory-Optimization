


import warnings
warnings.filterwarnings('ignore')

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=MOHITHA_REDDY;"
    "Trusted_Connection=yes;"
)
query = "SELECT * FROM DEMAND"
df = pd.read_sql(query, conn)

kurti = df[
    (df['City']=='Vijayawada') &
    (df['Category']=='Kurti')
]
print(kurti)
plt.figure(figsize=(8,3))
plt.plot(kurti['Date'],
         kurti['Orders'],
         marker='o')
plt.xlabel("dates")
plt.ylabel("no. of orders")
plt.xticks(rotation=90)
plt.title("sales of KURTI'S in vijayawada")
plt.show()
kurti = kurti.reset_index(drop=True)
kurti['Month_No'] = range(1, len(kurti)+1)

x=kurti[['Month_No']]
y=kurti['Orders']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)
next_month = [[25]]
prediction = model.predict(next_month)
print(prediction)
current_stock=300
pred = prediction[0]
if pred > current_stock:
    print(f"Restock {int(pred-current_stock)} units")
else:
    print("Current stock sufficient")

y_pred = model.predict(x)
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(kurti['Month_No'], y, marker='o', label='Actual Orders')
plt.plot(kurti['Month_No'], y_pred, marker='x', label='Predicted Trend')
plt.xlabel("Month")
plt.ylabel("Orders")
plt.title("Vijayawada Kurti Demand Forecast")
plt.legend()
plt.show()
from sklearn.metrics import r2_score
score = r2_score(y, y_pred)
print("R2 Score:", score)


OUTPUT :

         Date        City Category  Orders  Revenue  Stock_Available
0     2024-01  Vijayawada    Kurti     190   104500              250
100   2024-02  Vijayawada    Kurti     337   185350              402
200   2024-03  Vijayawada    Kurti     237   130350              260
300   2024-04  Vijayawada    Kurti     207   113850              260
400   2024-05  Vijayawada    Kurti     218   119900              253
500   2024-06  Vijayawada    Kurti     179    98450              209
600   2024-07  Vijayawada    Kurti     394   216700              420
700   2024-08  Vijayawada    Kurti     430   236500              549
800   2024-09  Vijayawada    Kurti     394   216700              465
900   2024-10  Vijayawada    Kurti     561   308550              604
1000  2024-11  Vijayawada    Kurti     523   287650              620
1100  2024-12  Vijayawada    Kurti     422   232100              551
1200  2025-01  Vijayawada    Kurti     281   154550              328
1300  2025-02  Vijayawada    Kurti     294   161700              322
1400  2025-03  Vijayawada    Kurti     248   136400              273
1500  2025-04  Vijayawada    Kurti     490   269500              532
1600  2025-05  Vijayawada    Kurti     241   132550              291
1700  2025-06  Vijayawada    Kurti     285   156750              352
1800  2025-07  Vijayawada    Kurti     210   115500              231
1900  2025-08  Vijayawada    Kurti     382   210100              502
2000  2025-09  Vijayawada    Kurti     261   143550              307
2100  2025-10  Vijayawada    Kurti     751   413050              867
2200  2025-11  Vijayawada    Kurti     702   386100              918
2300  2025-12  Vijayawada    Kurti     785   431750              963

[540.46014493]
Restock 240 units

