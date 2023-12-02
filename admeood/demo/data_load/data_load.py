# -*- coding: utf-8 -*-
'''
file=open('/data_1/wsy22/ood/demo/11.txt')
dataMat=[]
for line in file.readlines():
#     print(line)
    curLine=line.strip().split("\t")
#     floatLine=list(map(float,curLine))#这里使用的是map函数直接把数据转化成为float类型
    dataMat.append(curLine[:])
#print('dataMat:',dataMat)

id=[]
smiles=[]
for line in dataMat:
    id.append(line[0])
    smiles.append(line[1].strip('"'))

print(id)
print(smiles)


for i,j in zip(id,smiles):
    with open("/data_1/wsy22/ood/demo/aaa.txt",'a') as f:
        f.write((i+"\t"+j+'\n').encode('utf-8').decode('utf-8'))

for i in id:
    with open("/data_1/wsy22/ood/demo/aa.txt",'a') as f:
        f.write((i+'\n').encode('utf-8').decode('utf-8'))

import csv

f=open("/data_1/wsy22/ood/demo/CID.csv",'r')
csvreader=csv.reader(f)
final_list=list(csvreader)
#print(final_list)
id=[]
for i in final_list:
    id.append(i[1])
print(id)

for i in id:
    with open("/data_1/wsy22/ood/demo/cid.txt",'a') as f:
        f.write((i+'\n').encode('utf-8').decode('utf-8'))
#*****************************************
file=open('/data_1/wsy22/ood/demo/data_tox4/herg.txt')
dataMat=[]
for line in file.readlines():
#     print(line)
    curLine=line.strip().split("\t")
#     floatLine=list(map(float,curLine))#这里使用的是map函数直接把数据转化成为float类型
    dataMat.append(curLine[:])
#print('dataMat:',dataMat)


name=[]
smiles=[]
for line in dataMat:
    name.append(line[0].strip('"'))
    smiles.append(line[1].strip('"'))

#print(name)
#print(smiles)
#************************************


file=open('/data_1/wsy22/ood/demo/data_tox4/herg.txt')
dataMat=[]
for line in file.readlines():
#     print(line)
    curLine=line.strip().split("\t")
#     floatLine=list(map(float,curLine))#这里使用的是map函数直接把数据转化成为float类型
    dataMat.append(curLine[:])
#print('dataMat:',dataMat)
name=[]

for line in dataMat:
    name.append(line[0].strip('"'))

ff=0
for s in pref_name:
    if s in name:
        ff=ff+1
print(ff)




from mmcv import Config
ll=0
l=[]
data_name=["lbap_core_ec50_assay","lbap_core_ic50_assay","lbap_core_ki_assay","lbap_core_potency_assay"]
for  nnname in data_name:
    import mmcv

    l_name="data/"+nnname+'_custom.json'
    data=mmcv.load(l_name)
    train=data["split"]["train"]
    ood_test=data["split"]["ood_test"]
    iid_test=data["split"]["iid_test"]
    ood_val=data["split"]["ood_val"]
    iid_val=data["split"]["iid_val"]
    wa=train+ood_val+ood_test+iid_val+iid_test
    for line in wa:
        p=line["assay_id"]
        if p not in l:
            l.append(p)
    print(len(l))

import csv



f=open("/data_1/wsy22/ood/demo/data_tox4/herg_central.csv",'r')
csvreader=csv.reader(f)
final_list=list(csvreader)
#print(final_list)
id=[]
for i in final_list:
    id.append(i[15])
#print(id)


ff=0
for s in pref_name:
    if s in id:
        ff=ff+1
#print(ff)

'''




import pandas as pd
import json
import csv
df = pd.read_excel('F:\论文相关代码\ood\demo\data_load\Result_0-3.xlsx')
json_data = df.to_json(orient='records')
list_data = json.loads(json_data)
#print(list_data)

assay_id=[]
activity_id=[]
molregno=[]
canonical_smiles=[]
standard_inchi_key=[]
alogp=[]
hba=[]
hbd=[]
psa=[]
num_lipinski_ro5_violations=[]   #值为0   正样本    其他为负样本
cx_logd=[]
cx_most_apka=[]
cx_most_bpka=[]
full_mwt=[]
mw_freebase=[]
mw_monoisotopic=[]
standard_relation=[]
standard_value=[]
standard_type=[]
standard_units=[]
standard_flag=[]
pchembl_value=[]
pref_name=[]
assay_type=[]
ro3_pass=[]
structure_type=[]
molecule_type=[]
confidence_score=[]

p=0
f=0

lisst=['assay_id','activity_id','record_id','molregno',
       'pchembl_value','canonical_smiles','standard_inchi_key','alogp','hba','hbd','psa',
       'ro3_pass','num_lipinski_ro5_violations','cx_logd','cx_most_apka','cx_most_bpka',
       'full_mwt','mw_freebase','mw_monoisotopic','standard_relation','standard_value','standard_type',
       'standard_units','standard_flag','molecule_type','pref_name','confidence_score','assay_type']
flag=0
cls_label=[]
for line in list_data:
    assay_id=line['assay_id']
    activity_id=line['activity_id']
    molregno=line['molregno']
    pchembl_value=line['pchembl_value']
    canonical_smiles=line['canonical_smiles']
    standard_inchi_key=line['standard_inchi_key']
    alogp=line['alogp']
    hba=line['hba']
    hbd=line['hbd']
    psa=line['psa']
    ro3_pass=line['ro3_pass']
    num_lipinski_ro5_violations=line['num_lipinski_ro5_violations']
    cx_logd=line['cx_logd']
    cx_most_apka=line['cx_most_apka']
    cx_most_bpka=line['cx_most_bpka']
    full_mwt=line['full_mwt']
    mw_freebase=line['mw_freebase']
    mw_monoisotopic=line['mw_monoisotopic']
    standard_relation=line['standard_relation']
    standard_value=line['standard_value']
    structure_type=line['structure_type']
    standard_units=line['standard_units']
    standard_flag=line['standard_flag']

    molecule_type=line['molecule_type']
    pref_name=line['pref_name']
    confidence_score=['confidence_score']
    assay_type=line['assay_type']
    if pchembl_value<=5.6 and alogp>=3.55 and hba<=5 or hbd<=2 and psa<=84.94 and cx_logd>=2.82 and full_mwt<=407.46\
            and mw_freebase<=405.5 and num_lipinski_ro5_violations==0 and cx_most_apka>=6.5 and cx_most_bpka<=8.5:
        c=1
        p=p+1
    else:
        c=0
        f=f+1
    cls_label.append(c)

print(p)
print(f)



import pandas as pd

filename = 'F:\论文相关代码\ood\demo\data_load\Result_0-3.xlsx'
df = pd.read_excel(filename)

# 将数据框的列名全部提取出来存放在列表里
col_name=df.columns.tolist()

# 一、将u_list插入到指定位置。
# 在列索引为2的位置插入一列。刚插入时不会有值，整列都是NaN
# 比如说原来是a,b,c,d;我把新的一列插入到索引2，则变成a,b,新的一列,c,d
col_name.insert(0, 'cls_label')


# DataFrame.reindex() 对原行/列索引重新构建索引值
df=df.reindex(columns=col_name)

# 把新的数据，放到指定的列名下
# 新插入的数据u_list是从14&16列的数据计算得来
df['cls_label'] = cls_label

# 将整个df写入excel（不分sheets）
df.to_excel('F:\论文相关代码\ood\demo\data_load\confi_03.xlsx')








