import mmcv
import os.path as osp
from mmcv import Config
from ADMETood.apis import set_random_seed,train_model
from ADMETood.datasets import build_dataset
from ADMETood.models import build_model

data_name=["label_EC50_core","label_KI_core","label_potency_core"]
ss=[2019,2020,2021,2022]
ood_val_auc=[]
iid_val_auc=[]

for seed in ss:
    for  nnname in data_name:
        l_name="/data_1/wsy22/ood/demo/data_new/"+nnname+'.json'
        data=mmcv.load(l_name)
        m_name='/data_1/wsy22/ood/configs/algorithms/irm/'+nnname+'_irm.py'
        cfg=Config.fromfile(m_name)

        ann_file=l_name
        cfg.data.train.ann_file=ann_file
        cfg.data.ood_val.ann_file=ann_file
        cfg.data.iid_val.ann_file=ann_file
        cfg.data.ood_test.ann_file=ann_file
        cfg.data.iid_test.ann_file=ann_file
        cfg.seed=seed
        cfg.gpu_ids=range(1)
        w_name='/data_1/wsy22/ood/demo/work_dirs_irm/work_dirs/'+nnname+'_'+str(seed)
        cfg.work_dir=w_name
        set_random_seed(cfg.seed,deterministic=False)

        datasets=[build_dataset(cfg.data.train)]
        model=build_model(cfg.model)
        mmcv.mkdir_or_exist(osp.abspath(cfg.work_dir))
        train_model(model,datasets,cfg,distributed=False,validate=True)



































