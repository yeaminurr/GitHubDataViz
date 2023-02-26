from django.shortcuts import render , redirect
from django.http import HttpResponse
import pandas as pd

import numpy as np

from firstapp import form
import sklearn
import pickle
import sys, os
from pathlib import Path
from .loancalculate import calculate
import pickle
#base = os.path.dirname(os.path.abspath())
from pathlib import Path
# from loancalculate import calculator
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#tempdir = BASE_DIR.joinpath()
staticdir = Path.joinpath(BASE_DIR,"static")
ran = Path.joinpath(staticdir, "../static/random")
from django.core.files.storage import FileSystemStorage



# Create your views here.
realdata = dict()
recommendation=dict()
actual = dict()

medianfill = {
 'Current Loan Amount': 11760447.389459714,
 'Term': 0.7220800000000349,
 'Credit Score': 1076.4560893556354,
 'Annual Income': 1378276.5598425677,
 'Years in current job': 5.892355238155139,
 'Home Ownership': 0.9421200000000357,
 'Purpose': 1.3534635340285428,
 'Monthly Debt': 18472.41233580006,
 'Years of Credit History': 18.19914099999905,
 'Number of Open Accounts': 11.12853000000053,
 'Number of Credit Problems': 0.16831000000000476,
 'Current Credit Balance': 294637.3823500047,
 'Maximum Open Credit': 760798.3817476183,
 'Bankruptcies': 0.11774018998757532,
 'Tax Liens': 0.029312931293129337}

def index(request):
    return render(request,'firstapp/bootstrap final.html')
def front(request):
    return HttpResponse("first page")
# def user(request):
#     return render(request,'firstapp/newfile.html')
flag = True
def userinput(request):
    global flag
    global medianfill
    global actual
    # print("pihan joss")
    #
    # frm = form.NameForm()
    # if request.method == 'POST':
    #     print("post hoise")
    #     frm = form.NameForm(request.POST)
    #     if frm.is_valid():
    #         #z=frm.cleaned_data['Annual_Income']
    #         #HttpResponse("first page",z)
    #         print("income", frm.cleaned_data['AnnualIncome'])
    #         print('job', frm.cleaned_data['Years_in_current_job'])
    #         print('ABCD')
    #     else:
    #         print("false")
    #
    #

    context = {'myflag':flag}
    if request.method == 'POST':
        flag = True
        count = 0
        #print('ashchi')
        actual['Credit Score'] = request.POST.get('Credit Score')
        actual["Annual Income"] = request.POST.get('Annual Income')
        actual["Years in current job"] = request.POST.get('Years in current job')
        actual["Home Ownership"] = request.POST.get('Home Ownership')
        actual["Monthly Debt"] = request.POST.get('Monthly Debt')
        actual["Purpose"] = request.POST.get('Purpose')
        actual["Term"] = request.POST.get('Term')
        actual["Years of Credit History"] = request.POST.get('Years of Credit History')
        actual["Number of Open Accounts"] = request.POST.get('Number of Open Accounts')
        actual["Current Credit Balance"] = request.POST.get('Current Credit Balance')
        actual["Maximum Open Credit"] = request.POST.get('Maximum Open Credit')
        actual["Current Loan Amount"] = request.POST.get('Current Loan Amount')

        #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #print(request.POST.get('Home Ownership'))
        #print(request.POST.get('Annual Income'))
        for key in actual.keys():
            if actual[key] == "" or actual[key] == 'Select' or actual[key] == None:
                count = count+1
                pass
            else:
                try:
                    medianfill[key] = float(actual[key])
                except:
                    flag=False
        if flag==True and count<10:
            return redirect('/firstapp/result/')
        else:
            flag = False
        context['myflag'] = flag




    return render(request, 'firstapp/bootsrapth.html',context)
nimprove = dict()

def result(request):
    global recommendation
    global nimprove

    global medianfill
    #print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
    #print(medianfill)
    #print(medianfill)
    staticdir = Path.joinpath(BASE_DIR, "static")
    ran = Path.joinpath(staticdir, "../static/random")
    random = pickle.load(open(ran, 'rb'))


    mydata = pd.DataFrame(medianfill, index=[0])
    randomf_predictions = dict()
    randomf_predictions['pred'] = random.predict(mydata)
    new = dict()
    for keys in medianfill.keys():
        nkey =keys
        nkey = nkey.replace(" ","_")
        new[nkey]= medianfill[keys]

    #print(new["Annual_Income"])
    # a = dict()
    # b = dict()
    #
    # a['ajaira'] = "ami ajaira"
    # b['joss'] = 'ami joss'
    # z ={'one':a, 'two':b}
    improve = dict()

    for i in medianfill.keys():
        improve[i]=0
    #print(improve)
    if request.method == 'POST':
        # flag = True
        # count = 0
        #print('ekhaneo ashchi')
        improve['Credit Score'] = request.POST.get('Credit Score')
        improve["Annual Income"] = request.POST.get('Annual Income')
        improve["Home Ownership"] = request.POST.get('Home Ownership')
        improve["Monthly Debt"] = request.POST.get('Monthly Debt')
        improve["Number of Open Accounts"] = request.POST.get('Number of Open Accounts')
        improve["Current Credit Balance"] = request.POST.get('Current Credit Balance')
        improve["Maximum Open Credit"] = request.POST.get('Maximum Open Credit')
        improve["Current Loan Amount"] = request.POST.get('Current Loan Amount')

        for i in improve.keys():
            if improve[i] == None:
                improve[i] = 0
            else:
                improve[i] = int(improve[i])
        nimprove=improve
        #mycalculator = calculator()
        newdata=calculate(mydata,improve)
        #print(newdata)

        #print(improve)
        recommendation = newdata.to_dict('index')
        recommendation = recommendation[0]
        return redirect('/firstapp/recommendation/')

    return render(request, 'firstapp/result.html',randomf_predictions)



def after_result(request):
    #nimprove is the values of tick marks, that user wanted to Upgrade
    #recommendation is the uograded Result
    #medianFill is the userinput
    #final result is the suggestion
    finalresult = dict()
    global nimprove
    global recommendation
    global medianfill
    try:
        del recommendation['Bankruptcies']
        del recommendation['Number of Credit Problems']
        del recommendation['Tax Liens']
        del recommendation['Purpose']

    except:
        pass
    #print("recom", recommendation)
    for k,v in recommendation.items():
        if k=="Home Ownership" or k=="Number of Open Accounts" or k=='Credit Score':
            recommendation[k]=round(recommendation[k])

        else:
            recommendation[k] = round(recommendation[k],2)

    print("recommendations",recommendation)

    #print('keys',recommendation.keys())
    for k,v in recommendation.items():
        temp = v - medianfill[k]
        finalresult[k]= round(temp,2)
        print(k,v,medianfill[k])

    #print("final", finalresult)

    # print(medianfill)
    # #print(nimprove)
    # #print(recommendation)
    # print(finalresult)


    data= {'actual':medianfill,'recommendation':recommendation,'improve':nimprove,'finalresult':finalresult}

    z={"a":1}
    return render(request, 'firstapp/after result.html', data)

#Thesis done
def firebasetest(request):
    newdata = dict()

    return render(request, 'firstapp/Firebaset.html',newdata )
myfile = ""
def video(request):
    global myfile
    if request.method == 'POST'and request.FILES.get('myvideo'):
        for filename, file in request.FILES.items():
            newfilename = request.FILES[filename].name
            fs = FileSystemStorage()
            myfilename = fs.save(newfilename, file)
            myfile = myfilename
            print(myfile)
        return redirect('/firstapp/videoresult/')




    return render(request,'firstapp/video.html')
from .videoresultcalc import videores
def videoresult(request):
    global myfile
    ans = videores(myfile)
    mylist = {0: 'Archery',
              1: 'Basketball',
              2: 'Boxing',
              3: 'Cricket',
              4: 'Football',
              5: 'Ice Hockey',
              6: 'Swimming',
              7: 'Tennis'}
    myurl= fr"C:\Users\Pihan\PycharmProjects\GithubDataViz\static\video\{myfile}"
    print(myurl)
    videoname = {"name":mylist[ans],"videoName":myfile, "myurl":myfile}

    return render(request, 'firstapp/videoresult.html',videoname)


def tyre(request):
    global myfile
    if request.method == 'POST'and request.FILES.get('myvideo'):
        for filename, file in request.FILES.items():
            newfilename = request.FILES[filename].name
            fs = FileSystemStorage()

            myfilename = fs.save('image.jpg', file)
            myfile = myfilename
            print(myfile)
        return redirect('/firstapp/tyreresult/')
    return render(request, 'firstapp/tyre.html')
from .tyrecalc import tyreresultcalc
import matlab.engine

def tyreresult(request):
    url = fr"C:\Users\Pihan\PycharmProjects\GithubDataViz\static\video\matlab"
    eng = matlab.engine.start_matlab()
    try:

        eng.finalfuzzy_2(nargout=0)
    except:
        pass



    ans = tyreresultcalc(url)
    print(ans)
    try:
        os.remove(fr'C:\Users\Pihan\PycharmProjects\GithubDataViz\static\video\image.jpg')
    except:
        pass
    ans[0][0] = "{:.2f}".format(ans[0][0])
    if ans[0][0]<0.5:
        ans[0][0] = 1-ans[0][0]
        value =1  #'Worn out'
        ans[0][0]= ans[0][0]*100
    else:
        value =0 #'Good Tyre'
        ans[0][0] = ans[0][0] * 100

    info = {"name": ans[0][0], 'conition': value}



    return render(request, 'firstapp/tyreresult.html',info)

location = Path.joinpath(staticdir, "../static/git/datasetissueshortnot_othersc.csv")
dataset = pd.read_csv(location)
labelarray = []
for i in dataset.iloc:
    if i["types"] not in labelarray:
        labelarray.append(i["types"])

date = {}
def githubproject(request):
    global labelarray
    send_data={}
    send_data["Labels"]=labelarray
    ran2 = Path.joinpath(staticdir, "../static/git/datasetissueshortnot_othersc.csv")
    datasetissueshortnot_othersc = pd.read_csv(ran2)

    icat = Path.joinpath(staticdir, "../static/git/issue_catelog.csv")
    icatdata = pd.read_csv(icat)

    #doing the popup task for issue table
    if request.method == 'POST':
        data = request.POST.get("date",None)
        #print("asi")
        print(data)
        # ran2 = Path.joinpath(staticdir, "../static/git/datasetissueshortnot_othersc.csv")
        # datasetissueshortnot_othersc = pd.read_csv(ran2)
        print("Iam okay")
        # temp = datasetissueshortnot_othersc.copy()
        # temp = temp[temp["just_month"] == data]
        # temp = temp[temp['Closed At'].notna()]
        # temp = temp.groupby(["types"])["types",].count()
        # temp = temp.rename(columns={'types': 'Count of Type'})

        temp = datasetissueshortnot_othersc.copy()
        temp = temp[temp["just_month"] == data]
        #temp = temp[temp['Closed At'].notna()]
        temp = temp.groupby(["id", "Labels"])["id",].count().rename(columns={'id': 'unused'})
        temp = pd.merge(temp.reset_index(),datasetissueshortnot_othersc[["id","Closed At"]],on="id",how="left")
        temp.drop_duplicates(inplace = True)

        temp['Closed At'][temp['Closed At'].notnull()] = "Completed"
        temp = temp.fillna({'Closed At':"Incomplete"})
        temp =pd.merge(temp, icatdata[["issue_id","Importance Type"]], left_on='id',right_on="issue_id", how='left')



        # temp.to_frame().rename(columns={'types': 'Count of Type'})
        #temp.to_csv("temp.csv")
        #print(temp.to_string)
        ran3 = Path.joinpath(staticdir, "../static/git")

        temp.to_csv(Path.joinpath(ran3, "temp.csv"))



    return render(request, 'firstapp/Newtest.html',send_data)


def pull_table(request):
    if request.method == 'POST':
        data = request.POST.get("date", None)
        print("asi")
        print(data)
        ran2 = Path.joinpath(staticdir, "../static/git/pull_table.csv")
        pulltable = pd.read_csv(ran2)
        pulltable = pulltable[pulltable["just_month"] == data]
        ran3 = Path.joinpath(staticdir, "../static/git")
        pulltable.to_csv(Path.joinpath(ran3, "pulltable.csv"))

        #temp.to_csv("temp.csv")
    return HttpResponse(status=204)

from sklearn.preprocessing import MinMaxScaler
dataseti = pd.read_csv(Path.joinpath(staticdir, "../static/git/deepset-ai-haystack-issues.csv"))
datasetissue = dataseti[dataseti["Type"]=="issue"]
datasetissue = datasetissue.reset_index()
datasetissue = datasetissue.drop("index",axis=1)
datasetissueshort = datasetissue[["id","Created At","Closed At","Labels"]]
datasetissueshort["Created At"]= pd.to_datetime(datasetissueshort["Created At"])
datasetissueshort["just_month"]=datasetissueshort["Created At"].dt.strftime('%Y-%m')
datasetissueshort["just_month"]= pd.to_datetime(datasetissueshort["just_month"])
datasetissueshort["Labels"]=datasetissueshort["Labels"].fillna("Others")
pullset = pd.read_csv(Path.joinpath(staticdir, "../static/git/deepset-ai-haystack-pulls_updated.csv"))
pullset = pullset[pullset['merged'].notna()]
pullset["merged"] = pd.to_datetime(pullset["merged"],format="%Y-%m-%d")
pullbytime = pullset[["issue_id","merged","changed_files","pull_id"]]
#pullbytime['just_date'] =

pullbytime["just_month"] = pd.to_datetime(pullbytime["merged"].dt.strftime('%Y-%m'))

def labelsort(request):
    global labelarray
    send_data = {}
    send_data["Labels"] = labelarray
    if request.method == 'POST':
        data = request.POST.get("labels", None)
        print(data)


        data = data.split(",")
        temp_datasetissueshort=datasetissueshort.copy()
        temp_datasetissueshort = temp_datasetissueshort[temp_datasetissueshort["Labels"].str.contains('|'.join(data))]
        newforviz = temp_datasetissueshort.groupby(["just_month"])["just_month"].count()

        issuewith_time = newforviz.copy()
        issuewith_time = issuewith_time.to_frame()
        issuewith_time = issuewith_time.rename(columns={'just_month': 'Total_issue'})
        onlyclosedissue = datasetissueshort[datasetissueshort['Closed At'].notna()].groupby(["just_month"])["just_month"].count()
        issuewith_time["closed_issue"] = onlyclosedissue
        issuewith_time["ratio"] = issuewith_time["closed_issue"] / issuewith_time["Total_issue"]

        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(issuewith_time[["ratio"]])
        issuewith_time["scaled"] = scaled
        temp_pullbytime = pullbytime[pullbytime['issue_id'].isin(temp_datasetissueshort['id'])]
        g = temp_pullbytime.groupby(["just_month"])["just_month"].count().to_frame()
        g = g.rename(columns={'just_month': 'Total_pull'})
        j = temp_pullbytime.groupby(["just_month"])["changed_files"].sum().to_frame()
        mypullnew_forviz = pd.merge(g, j, left_index=True, right_index=True).reset_index()
        Pull_Issue = pd.merge(issuewith_time.reset_index(), mypullnew_forviz, on='just_month', how='outer')
        s = pd.date_range(Pull_Issue.iloc[0]["just_month"], Pull_Issue.iloc[-1]["just_month"], freq='M').to_frame()
        s["just_month"] = pd.to_datetime(s[0].dt.strftime('%Y-%m')).to_frame()
        allissue = pd.merge(Pull_Issue, s["just_month"], on='just_month', how='outer')
        allissue = allissue.fillna(0)
        allissue = allissue.sort_values(by='just_month').rename(columns={'just_month': 'date'})
        allissue["date"]= pd.to_datetime(allissue["date"])

        ran3 = Path.joinpath(staticdir, "../static/git")
        allissue.to_csv(Path.joinpath(ran3, "issue_pull_temp.csv"),index=False)







        print(data)
        #return redirect('/firstapp/github/')


        #temp.to_csv("temp.csv")
    return HttpResponse(status=204)


user_cat = pd.read_csv(Path.joinpath(staticdir, "../static/git/user_catelog.csv"))
def commentcat(request):
    global user_cat
    if request.method == 'POST':
        data = request.POST.get("date", None)
        print(data)
        user_catcopy  =  user_cat[user_cat["only_month"]==data]
        ran3 = Path.joinpath(staticdir, "../static/git")
        user_catcopy[["username","category"]].sort_values(by='category').to_csv(Path.joinpath(ran3, "user_catcopy.csv"),index=False)


    return HttpResponse(status=204)

