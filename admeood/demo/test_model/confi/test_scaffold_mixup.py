import mmcv
import os.path as osp
from mmcv import Config
from ADMETood.apis import set_random_seed,train_model
from ADMETood.datasets import build_dataset
from ADMETood.models import build_model

data_name=["confi_EC50_scaffold","confi_KI_scaffold","confi_potency_scaffold"]
ss=[2019,2020,2021,2022]
ood_val_auc=[]
iid_val_auc=[]

for seed in ss:
    for  nnname in data_name:
        l_name="/root/autodl-tmp/ADMETood/ood/demo/data_load/"+nnname+'.json'
        data=mmcv.load(l_name)
        m_name='/root/autodl-tmp/ADMETood/ood/configs/algorithms/mixup/'+nnname+'_mixup.py'
        cfg=Config.fromfile(m_name)
        ann_file=l_name
        cfg.data.train.ann_file=ann_file
        cfg.data.ood_val.ann_file=ann_file
        cfg.data.iid_val.ann_file=ann_file
        cfg.data.ood_test.ann_file=ann_file
        cfg.data.iid_test.ann_file=ann_file
    
        cfg.seed=seed
        cfg.gpu_ids=range(1)
        w_name='/root/autodl-tmp/ADMETood/ood/demo/work_MIXUP1/work_dirs1/'+nnname+'_'+str(seed)
        cfg.work_dir=w_name

        set_random_seed(cfg.seed,deterministic=False)
        datasets=[build_dataset(cfg.data.train)]
        model=build_model(cfg.model)
        mmcv.mkdir_or_exist(osp.abspath(cfg.work_dir))
        train_model(model,datasets,cfg,distributed=False,validate=True)


