# -*- coding: utf-8 -*-
import pandas as pd
import json
import random
import csv
#加载ood数据
df=pd.read_excel('F:\论文相关代码\ood\demo\data_load\confi_03.xlsx')
json_data=df.to_json(orient='records')
list_data=json.loads(json_data)
ecc=[]
icc=[]
kii=[]
poo=[]
kdd=[]
for line in list_data:
    s=line['standard_type']
    if s=='EC50':
        ecc.append(line)
    elif s=='IC50':
        icc.append(line)
    elif s=='Ki':
        kii.append(line)
    elif s=='Potency':
        poo.append(line)
    elif s=='Kd':
        kdd.append(line)
#加载iid数据
df=pd.read_excel('F:\论文相关代码\ood\demo\data_load\confi_9.xlsx')
json_data=df.to_json(orient='records')
list_data=json.loads(json_data)
ecc1=[]
icc1=[]
kii1=[]
poo1=[]
kdd1=[]
for line in list_data:
    s=line['standard_type']
    if s=='EC50':
        ecc1.append(line)
    elif s=='IC50':
        icc1.append(line)
    elif s=='Ki':
        kii1.append(line)
    elif s=='Potency':
        poo1.append(line)
    elif s=='Kd':
        kdd1.append(line)


#去重
def preprocessing(name):    
    list={}
    nn=[]
    for case in name:
        domain_value=case['standard_inchi_key']
        if domain_value not in list:
            list[domain_value]=[]

        list[domain_value].append(case)
    for k,l in list.items():        
            nn.append(l[0])
    return nn

ec_ood=preprocessing(ecc)
ic_ood=preprocessing(icc)
ki_ood=preprocessing(kii)
po_ood=preprocessing(poo)
ec_iid=preprocessing(ecc1)
ic_iid=preprocessing(icc1)
ki_iid=preprocessing(kii1)
po_iid=preprocessing(poo1)


def  dataload(name,name1,nnn):
    #加载train iid 数据
    data_each_domain1={}
    assay_id1=[]
    data_each_domain={}
    assay_id=[]
    for case in name:
        domain_value=case['assay_id']
        if domain_value not in data_each_domain:
            data_each_domain[domain_value]=[]
        data_each_domain[domain_value].append(case)
    list_domain_data=list(data_each_domain.items())
    list_domain_data=sorted(list_domain_data,key=lambda x:len(x[1]),reverse=True)
    for domain_id,(domain_value,lines_cur_domain) in enumerate(list_domain_data):
        for one_line in lines_cur_domain:
            one_line['domain_id']=domain_id

    l_ec=len(name)
    l_tr=int(l_ec*0.6)
    l_te=int(l_ec*0.2)
    l_va=int(l_ec*0.2)
    count=0
    n_tr=0
    n_va=0
    train=[]
    val=[]
    test=[]
    for domain_id,data_cur_domain in list_domain_data:
        random.shuffle(data_cur_domain)
        len_train=int(len(data_cur_domain)*0.6)
        len_val=int(len(data_cur_domain)*0.2)
        train_cur_domain=data_cur_domain[:len_train]
        iid_val_cur_domain=data_cur_domain[len_train:len_train+len_val]
        iid_test_cur_domain=data_cur_domain[len_train+len_val:]
        train+=train_cur_domain
        val+=iid_val_cur_domain
        test+=iid_test_cur_domain

    #加载新的OOD数据
    for case in name1:
        domain_value=case['assay_id']
        if domain_value not in data_each_domain1:
            data_each_domain1[domain_value]=[]
        data_each_domain1[domain_value].append(case)
    list_domain_data1=list(data_each_domain1.items())
    for domain_id,(domain_value,lines_cur_domain) in enumerate(list_domain_data1):
        for one_line in lines_cur_domain:
            one_line['domain_id']=domain_id+len(list_domain_data)

    l_ec1=len(name1)
    l_te1=l_ec1/2
    l_va1=l_te1
    count1=0
    n_tr1=0
    n_va1=0
    for domain_id,lines_one_domain in list_domain_data1:
        if count1<l_te1:
            count1+=len(lines_one_domain)
            n_tr1+=1
        elif count1<l_te1+l_va1:
            count1+=len(lines_one_domain)
            n_va1+=1

    domain_val1=list_domain_data1[:n_tr1]
    domain_test1=list_domain_data1[n_tr1:n_tr1+n_va1]
    val1=[]
    test1=[]
    for domain_id,lines_one_domain in domain_val1:
        for line in lines_one_domain:
            val1.append(line)
    for domain_id,lines_one_domain in domain_test1:
        for line in lines_one_domain:
            test1.append(line)
    import json
    import os
    json_file_name='F:/论文相关代码/ood/demo/data_new/confi_'+nnn+'_assay.json'
    dic1={"cfg":{"path":{"task":{"type":"","subset":""},
                         "source_root":"",
                         "target_root":""},"uncertainty":{"delta":{}},
                 "classification_threshold":{},
                 "fractions":{},"noise_filter":{"assay":{},"sample":{}},"domain":{}},'split':{}}
    dic1['split']['train']=train
    dic1['split']['iid_val']=val
    dic1['split']['iid_test']=test
    dic1['split']['ood_val']=val1
    dic1['split']['ood_test']=test1


    with open(json_file_name,'w') as f:
        json.dump(dic1,f)

dataload(ec_iid,ec_ood,'EC50')
dataload(ic_iid,ic_ood,'IC50')
dataload(ki_iid,ki_ood,'KI')
dataload(po_iid,po_ood,'Potency')
