from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Customed_User,Upload,UploadPdf,UploadJson,GptUser,GptFormUser
from rest_framework import status
from .rest2 import *
from django.core.mail import send_mail
import requests

import json

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customed_User # 针对Basic_User表进行序列化
        fields="__all__"
        # exclude=["pub_date"]
    # def create(self,valid_data):
    #     return User.objects.create_user(**valid_data)

class CustomUserView(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Customed_User.objects.all()
    serializer_class=CustomUserSerializers

# 非正式用户表格
class GptUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=GptUser # 针对Basic_User表进行序列化
        fields="__all__"

class GptUserView(ModelViewSet):
    queryset=GptUser.objects.all()
    serializer_class=GptUserSerializers

# 正式用户表格
class GptFormUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = GptFormUser
        fields = '__all__'

class GptFormUserView(ModelViewSet):
    queryset = GptFormUser.objects.all()
    serializer_class = GptFormUserSerializers

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = GptFormUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 上传文件的api
class UploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class UploadView(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializers
    def post(self,request):
        file_serializer = UploadSerializers(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(file_serializer.data,status=status.HTTP_400_BAD_REQUEST)

# 上传pdf文件的api
class UploadPdfSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadPdf
        fields = '__all__'

class UploadPdfView(ModelViewSet):
    queryset = UploadPdf.objects.all()
    serializer_class = UploadPdfSerializers
    def post(self,request):
        file_serializer = UploadPdfSerializers(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(file_serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        UploadPdf.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 上传json文件的api（no use）
class UploadJsonSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadJson
        fields = '__all__'

class UploadJsonView(ModelViewSet):
    queryset = UploadJson.objects.all()
    serializer_class = UploadJsonSerializers

# 测试接口
@api_view(('GET','POST',))
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
# @renderer_classes((JSONRenderer))
def test(request):
    if request.method=='GET':
        print(request.method+' 请求发送成功')
        getData=dict(request.GET)
        print(getData)
        getStr=""
        for key,value in getData.items():
            getStr+=key+'='+str(value[0])+'&'
        getStr=getStr[0:-1]
        info='您使用'+request.method+'请求发送了'+getStr
        return Response(data=info)
    else :
        print(request.data)
        info='您使用'+request.method+'请求发送了'+json.dumps(request.data)
        return Response(data=info)
        # getData=dict(request.POST)
        # print(getData)
        # getStr=""
        # for key,value in getData.items():
        #     getStr+=key+'='+str(value[0])+'&'
        # getStr=getStr[0:-1]
        # info='您使用'+request.method+'请求发送了'+getStr
        # return Response(data=info)

# 得到分类的api
@api_view(('GET','POST',))
def gtc(request):
    oneQuestion = request.GET.get('question')
    return Response(data = gttt(oneQuestion))

# 得到对话内容的api
o1 = (i for i in range(0))
@api_view(('GET','POST',))
def chat(request):
    global o1
    question = request.GET.get('question')
    class_type = request.GET.get('class_type')
    print("===========________________=============")
    print(request.GET.get('isinit'))
    if request.GET.get('isinit') == 'true':
        o1,s1 = gtcc(question,class_type)
        return Response(data = s1)
    else :
        # try :
        #     nextcontent = o1.__next__()
        # except:
        #     nextcontent = "*****stop*****"
        # print("----||||-----")
        # print(nextcontent)
        return Response(data = o1.__next__())

# 发送邮件的api
@api_view(('GET','POST',))
def toemail(request):
    send_mail(
        'Subject here',  # 主题
        'Here is the message.',  # 消息内容
        'deepmiemie@gmail.com',  # 发件人
        ['3232372771@qq.com'],  # 收件人列表
        fail_silently=False,
    )
    return Response(data = "send sucessful!")

# 校验用户名和邮箱是否存在的api
@api_view(('GET','POST',))
def checkUE(request):
    field = request.GET.get("field")
    print(field)
    if GptUser.objects.filter(username=field).exists() or GptUser.objects.filter(email=field).exists() :
        return Response(data = 'true')
    else :
        return Response(data = 'false')

# 生成两个文件的api
@api_view(('GET','POST',))
def generate(request):
    res = requests.get("http://127.0.0.1:8000/test/uploadpdf/").json()
    # 从数据库中进行资料获取
    pdf_metadata = []
    filelist = res['data']

    for ifile in filelist :
        api = ifile['file']
        pdfdata = requests.get(api).content
        ipageText = ""
        pdfLearn = fitz.open(stream = pdfdata ,filetype = "pdf")
        for page in pdfLearn :
            ipageText += page.get_text("text")
        pdf_metadata.append({"metadata":pdfLearn.metadata,"pageText":ipageText})
        # print('.....')
    pdf_store = np.array(pdf_metadata)
    # 删除先前存在的文件
    # print(pdf_store)
    
    # 保存为json文件
    jsonDir = pd.DataFrame(pdf_store).to_json()
    jsonfiles = {'file': ('pdf_store.json', jsonDir, 'application/json')}
    print(jsonDir)

    # 存储到数据库中
    requests.post(url = "http://127.0.0.1:8000/test/upload/",files=jsonfiles)

    # 获得私有类知识库的encode
    pra_page_text = [i["pageText"] for i in pdf_metadata]
    pra_pdf_vec = model.encode("".join(pra_page_text))

    # 保存为csv暂存
    csvDir = pd.DataFrame(pra_pdf_vec).to_csv()
    csvfiles = {'file': ('csv_store.csv', csvDir)}
    # 存储到数据库中
    requests.post(url = "http://127.0.0.1:8000/test/upload/",files=csvfiles)

    return Response(data = "处理完毕")

# 判断是否能够登录
