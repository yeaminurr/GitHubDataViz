from django.shortcuts import render , redirect
from django.http import HttpResponse
import pandas as pd

import numpy as np



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



def index(request):
    return render(request,'firstapp/bootstrap final.html')
def front(request):
    return HttpResponse("first page")
# def user(request):
#     return render(request,'firstapp/newfile.html')
flag = True



from sklearn.preprocessing import MinMaxScaler
dataseti = pd.read_csv(Path.joinpath(staticdir, "../static/git/deepset-ai-haystack-issues.csv"))
dataseti["Created At"]= pd.to_datetime(dataseti["Created At"])
dataseti["just_month"]=dataseti["Created At"].dt.strftime('%Y-%m')
dataseti["just_month"]= pd.to_datetime(dataseti["just_month"])
dataseti["Labels"]=dataseti["Labels"].fillna("Others")
datasetissue = dataseti[dataseti["Type"]=="issue"]
datasetissue = datasetissue.reset_index()
datasetissue = datasetissue.drop("index",axis=1)
datasetissueshort = datasetissue[["id","Created At","Closed At","Labels","just_month"]]
# datasetissueshort["Created At"]= pd.to_datetime(datasetissueshort["Created At"])
# datasetissueshort["just_month"]=datasetissueshort["Created At"].dt.strftime('%Y-%m')
# datasetissueshort["just_month"]= pd.to_datetime(datasetissueshort["just_month"])
# datasetissueshort["Labels"]=datasetissueshort["Labels"].fillna("Others")
pullset = pd.read_csv(Path.joinpath(staticdir, "../static/git/deepset-ai-haystack-pulls_updated.csv"))
pullset = pullset[pullset['merged'].notna()]
pullset["merged"] = pd.to_datetime(pullset["merged"],format="%Y-%m-%d")
pullbytime = pullset[["issue_id","merged","changed_files","pull_id"]]
#pullbytime['just_date'] =

pullbytime["just_month"] = pd.to_datetime(pullbytime["merged"].dt.strftime('%Y-%m'))
user_cat = pd.read_csv(Path.joinpath(staticdir, "../static/git/user_catelog.csv"))
datasetcomment = dataseti[dataseti["Type"]=="comment"]
t10colab = datasetcomment[["id","just_month","Title"]]
t10colab.rename(columns={"id": "issue_id","Title":"username","just_month":"only_month"	},inplace = True)
t10colab["username"]=t10colab["username"].str.replace("b'","")
t10colab["username"]=t10colab["username"].str.replace("'","")
t10colab = pd.merge(t10colab, user_cat[["username","category"]].drop_duplicates(), on='username', how='left')
t10colab = pd.merge(t10colab, datasetissueshort[["id","Labels"]].drop_duplicates(),left_on="issue_id", right_on="id", how='left')
t10colab.rename(columns={"id": "issue_id"},inplace = True)
from functools import reduce


location = Path.joinpath(staticdir, "../static/git/datasetissueshortnot_othersc.csv")
dataset = pd.read_csv(location)
labelarraynew = []
labellist = pd.read_csv(Path.joinpath(staticdir, "../static/git/labellist.csv"))
# for i in dataset.iloc:
#     if i["types"] not in labelarraynew:
#         labelarraynew.append(i["types"])
# print("label",len(labelarraynew))

labelarray = list(labellist["name"])
labelarray.append("Others")

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

        temp = datasetissueshort.copy()
        temp = temp[temp["just_month"] == data]
        #temp = temp[temp['Closed At'].notna()]
        temp = temp.groupby(["id", "Labels"])["id",].count().rename(columns={'id': 'unused'})
        temp = pd.merge(temp.reset_index(),datasetissueshort[["id","Closed At"]],on="id",how="left")
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




def labelsort(request):
    global t10colab
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

        #NOW DOING THE BARCHART

        t10copy = t10colab[t10colab["Labels"].str.contains('|'.join(data))]
        #print(t10colab.head(25))



        high = t10copy[t10copy["category"] == "high"][["only_month", "category"]].groupby(["only_month"]).count()
        high.rename(columns={'category': 'high'}, inplace=True)
        mid = t10copy[t10copy["category"] == "mid"][["only_month", "category"]].groupby(["only_month"]).count()
        mid.rename(columns={'category': 'mid'}, inplace=True)
        low = t10copy[t10copy["category"] == "low"][["only_month", "category"]].groupby(["only_month"]).count()
        low.rename(columns={'category': 'low'}, inplace=True)


        allcommenthis = reduce(lambda x, y: pd.merge(x, y, on='only_month', how='outer'), [high, mid, low])
        allcommenthis = allcommenthis.replace([np.nan], 0)
        allcommenthis.reset_index(inplace = True)
        allcommenthis.rename(columns={"only_month":"time"},inplace = True)
        allcommenthis.info()
        allcommenthis.sort_values(by='time')
        allcommenthis["time"] = allcommenthis["time"].dt.strftime('%m/%d/%Y')
        allcommenthis.to_csv(Path.joinpath(ran3, "commentboard_copy.csv"),index = None)







        print(data)
        #return redirect('/firstapp/github/')


        #temp.to_csv("temp.csv")
    return HttpResponse(status=204)


user_cat = pd.read_csv(Path.joinpath(staticdir, "../static/git/user_catelog.csv"))
def commentcat(request):
    #This function is only for fetching the user list who commented on a perticular time(after clicking on barchart)
    global user_cat
    if request.method == 'POST':
        data = request.POST.get("date", None)
        print(data)
        user_catcopy  =  user_cat[user_cat["only_month"]==data]
        ran3 = Path.joinpath(staticdir, "../"
                                        "/git")
        user_catcopy[["username","category"]].sort_values(by='category').to_csv(Path.joinpath(ran3, "user_catcopy.csv"),index=False)


    return HttpResponse(status=204)

