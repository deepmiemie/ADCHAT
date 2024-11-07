import pandas as pd
import numpy as np
from InstructorEmbedding import INSTRUCTOR
from sklearn.metrics.pairwise import cosine_similarity
import replicate
import json
import torch
import torch.nn as nn
import fitz
import requests
from io import BytesIO
import re

# 读取本地模型文件
model = INSTRUCTOR("F:\\工作以及比赛\\大一统框架\\dd\\try2\\t1\\model")
print("read successful!")

# 加载网络结构参数
with open("F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\1.准确定向问题\\model_struct.json","r") as f :
    content = f.read()
model_struct = json.loads(content)

# 定义网络结构
class network(nn.Module) :
    def __init__(self,input_size,hidden_size,drop_prod,num_layers,activate_func) :
        super().__init__()
        # 激活函数可供选择
        if activate_func == 'relu' :
            acf = nn.ReLU()
        elif activate_func == 'sigmoid' :
            acf = nn.Sigmoid()
        elif activate_func == 'tanh' :
            acf = nn.Tanh()
        
        layer_list = [
            nn.Linear(in_features = input_size,out_features = hidden_size,bias = True),
            acf,
            nn.Dropout(p=drop_prod),
        ]

        for i in range(num_layers-1) :
            layer_list.append(nn.Linear(in_features = hidden_size,out_features = hidden_size,bias = True))
            layer_list.append(acf)
            layer_list.append(nn.Dropout(p=drop_prod))
        
        layer_list.append(nn.Linear(in_features = hidden_size,out_features = 4 ,bias = True))
        self.model = nn.Sequential(*layer_list)

    def forward(self,x) :
        return self.model(x)

# 定义网络结构参数
hidden_size = model_struct["hidden_size"]
drop_prod = model_struct["drop_prod"]
num_layers = model_struct["num_layers"]
activate_func = model_struct["activate_func"]

# 定义模型
model_custom = network(input_size=768,hidden_size=int(hidden_size),drop_prod=drop_prod,num_layers=int(num_layers),activate_func=["relu","sigmoid","tanh"][int(activate_func)])

# 加载模型参数
model_custom.load_state_dict(torch.load("F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\1.准确定向问题\\model_params.pth"))
model_custom.eval()

def gttt(question) :
    global model,model_custom
    # 给定一个问题
    # question = "Why are nitrogen source materials like ammonia and urea added to the process?"

    # 对问题进行编码
    question_vec = model.encode(question)

    # 求解问题分类
    class_type = model_custom(torch.Tensor(question_vec)).argmax() + 1
    return class_type




def gtcc(question,class_type) :
    global template,model,pra_pdf_vec,pra_store
    if class_type == "5": # 基于读入的数据库进行读取
        template = """
        Please answer the questions based on the information given to you.
        {context}

        {chat_history}
        The question you are about to answer is:
        {question}
        """
        
        # 读取私有类知识库
        # pra_store = pd.read_json(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\2.准确定向文献\\pdf_store\\pdf_store{class_type}.json").reset_index(drop=True).iloc[:,0].tolist()
        pra_store = pd.DataFrame(json.loads(requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json/").content)).iloc[:,0].tolist()
        
        # 读取编码向量
        print("encoding...")
        pra_pdf_vec = np.array(pd.read_csv(BytesIO(requests.get("http://127.0.0.1:8000/media/uploads/csv_store.csv/").content)))[:,1::]
        
        print("encoding successful !")

    else : # 基于基础数据库进行读取
        with open(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\3更加准确的gpt\\classcontent\\t{class_type}.txt","r",encoding="utf8") as f :
            add_prompt = f.read()
        print(len(add_prompt))
        template="""
        You are an AI assistant designed to provide guidance tailored to in the field of anaerobic digestion. 
        Context:\n{context}
        Question:{question}
        Please answer in the following format.
        first, absorb as much of the Context as you can and give answers to the corresponding questions based on your understanding..
        second, Answer the question in more detail and logically, explaining every detail of the question in more detail. The format is
            (1) Sub-explanation
            (2) Sub-explanation
        etc...
        Sub-explanation should not be limited to two, usually three or more;
        finally, Summarize all the above conclusions and further explain the problem. And finally give your in-depth insights on this issue.Don't give a summary or anything like that in your answer, just give the corresponding conclusion.
        {chat_history}
        The Question you are about to answer is:
        Answer:
        """

        # 读取私有类知识库
        pra_store = pd.read_json(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\2.准确定向文献\\pdf_store\\pdf_store{class_type}.json").reset_index(drop=True).iloc[:,0].tolist()

        # 读取编码向量
        print("encoding...")
        pra_pdf_vec = np.array(pd.read_csv(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\3更加准确的gpt\\pra_pdf\\pra_pdf_vec{class_type}.csv"))[:,1::]
        print("encoding successful !")
    

    if class_type != "5":
        dp = {
            "question" : question,
            "k" : 4,
            }
        p = requests.post("https://u246156-8c85-142afdcc.westb.seetacloud.com:8443/test/pdfjson/", data=dp)
        pj = json.loads(p.text)
        prompt = template.format(question = question , context = pj , chat_history = [] , base_know = add_prompt)
        with open(f"F:\\工作以及比赛\\大一统框架\\dd\\try2\\app\\backproject\\app01\\all_function\\3更加准确的gpt\\sys\\{class_type}.txt") as f:
            sys = f.read()
    else :
        a = requests.get("http://127.0.0.1:8000/media/uploads/pdf_store.json")
        a1 = json.loads(a.text)["0"]
        info = ""
        for i in range(len(list(a1.values()))):
            d = a1[str(i)]["pageText"]
            info += f"PDF1:\n\n{d}"
        pj = info
        prompt = template.format(question = question , context = pj , chat_history = [])
        sys = ""
    
    data = {
        "question" : prompt,
        "sys" : sys,
        }
    r = requests.post("https://u246156-8c85-142afdcc.westb.seetacloud.com:8443/test/chat/", data=data)
    def f(x):
        extracted_content = x.split("<start_of_turn>model")[1].split("<eos>")[0]
        final_content = extracted_content.strip()
        # Removing Markdown formatting
        clean_content = re.sub(r'\*\*|\*\*', '', final_content)  # Remove bold formatting
        clean_content = re.sub(r'\n+', '\n', clean_content)  # Remove extra new lines
        ct = clean_content.strip()
        return ct
    rtext = f(r.text).replace("\n", "")
    o = (i for i in rtext)
    print(o)

    return o, pj
    


