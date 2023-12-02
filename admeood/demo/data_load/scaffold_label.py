# -*- coding: utf-8 -*-
import pandas as pd
import json
import random
import csv
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold
df=pd.read_excel('/data_1/wsy22/ood/demo/data_load/confi_9.xlsx')
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


#去重&&筛选出标签冲突数据
ec={}
smiles={}
ec_iid=[]
ec_ood=[]
for case in ecc:
    domain_value=case['standard_inchi_key']
    if domain_value not in ec:
        ec[domain_value]=[]
    ec[domain_value].append(case)
for k,l in ec.items():

    a=[]
    b=[]
    for i in l:
        if i['cls_label']==0:
            a.append(i)
        elif i['cls_label']==1:
            b.append(i)

    if  len(a)!=0 and len(b)!=0:
        if len(a)>=len(b):
            for i in a:
                ec_ood.append(i)
        else:
            for i in b:
                ec_ood.append(i)
    else:
        for i in l:
            ec_iid.append(i)

ic={}
smiles={}
ic_iid=[]
ic_ood=[]
for case in icc:
    domain_value=case['standard_inchi_key']
    if domain_value not in ic:
        ic[domain_value]=[]
    ic[domain_value].append(case)
for k,l in ic.items():
    a=[]
    b=[]
    for i in l:
        if i['cls_label']==0:
            a.append(i)
        elif i['cls_label']==1:
            b.append(i)

    if  len(a)!=0 and len(b)!=0:
        if len(a)>=len(b):
            for i in a:
                ic_ood.append(i)
        else:
            for i in b:
                ic_ood.append(i)
    else:
        for i in l:
            ic_iid.append(i)


ki={}
smiles={}
ki_iid=[]
ki_ood=[]
for case in kii:
    domain_value=case['standard_inchi_key']
    if domain_value not in ki:
        ki[domain_value]=[]
    ki[domain_value].append(case)
for k,l in ki.items():
    a=[]
    b=[]
    for i in l:
        if i['cls_label']==0:
            a.append(i)
        elif i['cls_label']==1:
            b.append(i)

    if  len(a)!=0 and len(b)!=0:
        if len(a)>=len(b):
            for i in a:
                ki_ood.append(i)
        else:
            for i in b:
                ki_ood.append(i)
    else:
        for i in l:
            ki_iid.append(i)

po={}
smiles={}
po_iid=[]
po_ood=[]
for case in poo:
    domain_value=case['standard_inchi_key']
    if domain_value not in po:
        po[domain_value]=[]
    po[domain_value].append(case)
for k,l in po.items():
    a=[]
    b=[]
    for i in l:
        if i['cls_label']==0:
            a.append(i)
        elif i['cls_label']==1:
            b.append(i)

    if  len(a)!=0 and len(b)!=0:
        if len(a)>=len(b):
            for i in a:
                po_ood.append(i)
        else:
            for i in b:
                po_ood.append(i)
    else:
        for i in l:
            po_iid.append(i)

def sort(smile):
    mol = Chem.MolFromSmiles(smile)
    if (mol is None):
        print('GetNumAtoms error, smiles:{}'.format(smile))
        return  len(smile)
    number_atom = mol.GetNumAtoms()
    return number_atom

def  dataload(name,name1,nnn):
    #加载train iid 数据
    data_each_domain1={}
    assay_id1=[]
    data_each_domain={}
    assay_id=[]
    for case in name:
        domain_value=case['smiles']
        if domain_value not in data_each_domain:
            data_each_domain[domain_value]=[]
        data_each_domain[domain_value].append(case)
    
    list_domain_data=list(data_each_domain.items())
   
    list_domain_data=sorted(list_domain_data,key=lambda x:sort(x[0]),reverse=True)
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
    for domain_id,lines_one_domain in list_domain_data:
        if count<l_tr:
           count+=len(lines_one_domain)
           n_tr+=1
        elif count<l_tr+l_va:
           count+=len(lines_one_domain)
           n_va+=1

    domain_train=list_domain_data[:n_tr]
    domain_val=list_domain_data[n_tr:n_tr+n_va]
    domain_test=list_domain_data[n_tr+n_va:]
    train=[]
    val=[]
    test=[]
    for domain_id,lines_one_domain in domain_train:
        for line in lines_one_domain:
         train.append(line)
    for domain_id,lines_one_domain in domain_val:
        for line in lines_one_domain:

            val.append(line)
    for domain_id,lines_one_domain in domain_test:
        for line in lines_one_domain:

            test.append(line)
    #加载新的OOD数据
    for case in name1:
        domain_value=case['smiles']
        if domain_value not in data_each_domain1:
            data_each_domain1[domain_value]=[]
        data_each_domain1[domain_value].append(case)
    list_domain_data1=list(data_each_domain1.items())
    list_domain_data=sorted(list_domain_data,key=lambda x:sort(x[0]),reverse=True)
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
    json_file_name='/data_1/wsy22/ood/demo/data_new/label_'+nnn+'_scaffold.json'
    dic1={"cfg":{"path":{"task":{"type":"lbap","subset":"lbap_core_ec50_assay_custom"},
                         "source_root":"/data_1/wsy22/ood/CHEMBL_SQLLITE/chembl_29_sqlite/chembl_29.db",
                         "target_root":"data/"},"uncertainty":{"delta":{"<":-1,"<=":-1,">":1,">=":1}},
                 "classification_threshold":{"lower_bound":4,"upper_bound":6,"fix_value":5},
                 "fractions":{"train_fraction_ood":0.6,"val_fraction_ood":0.2,"iid_train_sample_fractions":0.6,
                              "iid_val_sample_fractions":0.2},"noise_filter":{
            "assay":{"measurement_type":["EC50"],"assay_value_units":["nM","uM"],"molecules_number":[50,100],
                     "confidence_score":9},
            "sample":{"filter_none":[],"smile_exist":[],"smile_legal":[],"value_relation":["=","~"]}},
                 "domain":{"domain_generate_field":"assay_id","domain_name":"assay","sort_func":"domain_capacity",
                           "sort_order":"descend","protein_family_level":1}},
          'split':{}}
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
dataload(po_iid,po_ood,'potency')
