
import pandas as pd
import os
from datetime import datetime

def ghi_log(ten_khach, email, sobg, ds):
    path = "bao_gia_log.xlsx"
    df = pd.DataFrame(ds)
    df.insert(0, "Số BG", sobg)
    df.insert(1, "Khách", ten_khach)
    df.insert(2, "Email", email)
    df.insert(3, "Ngày", datetime.now().strftime("%Y-%m-%d %H:%M"))
    try:
        old = pd.read_excel(path)
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass
    df.to_excel(path, index=False)
