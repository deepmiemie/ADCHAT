import json
import pandas as pd
import requests
import numpy as np
from io import BytesIO

d1 = {"name":"li"}

# pd.Series(json.loads(requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json/").content)).tolist()
# print(pd.read_json())

# np.array(pd.read_csv(BytesIO(requests.get("http://127.0.0.1:8000/media/uploads/csv_store.csv/").content)))[:,1::]
# pd.Series(json.loads(requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json/").content)).tolist()
# d = pd.read_json(r"F:\工作以及比赛\大一统框架\dd\try2\app\backproject\app01\all_function\2.准确定向文献\pdf_store\pdf_store1.json")
# print(d.reset_index(drop=True).iloc[:,0])
# print(pd.DataFrame(json.loads(requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json/").content)).iloc[:,0].tolist())

# pra_pdf_vec = pd.read_json(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\2.准确定向文献\\pdf_store\\pdf_store{1}.json").reset_index(drop=True).iloc[:,0]
pra_pdf_vec = pd.DataFrame(json.loads(requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json/").content)).iloc[:,0]
# pra_pdf_vec = pd.read_json(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\2.准确定向文献\\pdf_store\\pdf_store{1}.json").reset_index(drop=True).iloc[:,0]


print(pra_pdf_vec)

