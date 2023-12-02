_base_ = ['../../_base_/schedules/classification.py', '../../_base_/default_runtime.py']

# transform
train_pipeline = [
    dict(
        type="SmileToGraph",
        keys=["input"]
    ),
    dict(
        type='Collect',
        keys=['input', 'gt_label', 'group']
    )
]
test_pipeline = [
    dict(
        type="SmileToGraph",
        keys=["input"]
    ),
    dict(
        type='Collect',
        keys=['input', 'gt_label', 'group']
    )]

# dataset
dataset_type = "LBAPDataset"
ann_file = 'data_new/confi_KI_scaffold.json'

data = dict(
    samples_per_gpu=128,
    workers_per_gpu=4,
    train=dict(
        split="train",
        type=dataset_type,
        ann_file=ann_file,
        pipeline=train_pipeline
    ),
    ood_val=dict(
        split="ood_val",
        type=dataset_type,
        ann_file=ann_file,
        pipeline=test_pipeline,
        rule="greater",
        save_best="accuracy"
    ),
    iid_val=dict(
        split="iid_val",
        type=dataset_type,
        ann_file=ann_file,
        pipeline=test_pipeline,
    ),
    ood_test=dict(
        split="ood_test",
        type=dataset_type,
        ann_file=ann_file,
        pipeline=test_pipeline,
    ),
    iid_test=dict(
        split="iid_test",
        type=dataset_type,
        ann_file=ann_file,
        pipeline=test_pipeline,
    ),
)
# model
model = dict(
    type="ERM",
    tasker=dict(
        type='Classifier',
        backbone=dict(
            type='GAT',
            in_feats=39,
        ),
        head=dict(
            type='LinearClsHead',
            num_classes=2,
            in_channels=64,
            loss=dict(
                type='CrossEntropyLoss',
            )
        )
    )
)
