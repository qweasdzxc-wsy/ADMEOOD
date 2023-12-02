from mmcv import print_log
from ADMETood.curators import GenericCurator


def curate_data(cfg):
    print_log(f'Curator Config:\n{cfg.pretty_text}''\n' + '-' * 60)
    curator = GenericCurator(cfg)
    # Processing Flow
    data = curator.data_loading()
    data = curator.noise_filtering(data)
    data = curator.uncertainty_processing(data)
    data = curator.classification_label_generating(data)
    data = curator.data_splitting(data)
    curator.data_saving(data)
    curator.statistics_reporting()
