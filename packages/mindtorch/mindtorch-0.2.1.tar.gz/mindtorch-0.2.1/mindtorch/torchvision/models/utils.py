#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

ckpt_file_link = {
    'alexnet-owt-7be5be79.ckpt': 'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=alexnet',
    'resnet18-f37072fd.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnet18',
    'resnet34-b627a593.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnet34',
    'resnet50-0676ba61.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnet50',
    'resnet101-63fe2227.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnet101',
    'resnet152-394f9c45.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnet152',
    'resnext50_32x4d-7cdf4587.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnext50_32x4d',
    'resnext101_32x8d-8ba56ff5.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=resnext101_32x8d',
    'wide_resnet50_2-95faca4d.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=wide_resnet50_2',
    'wide_resnet101_2-32ee1156.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=wide_resnet101_2',
    'vgg11-8a719046.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg11',
    'vgg13-19584684.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg13',
    'vgg16-397923af.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg16',
    'vgg19-dcbb9e9d.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg19',
    'vgg11_bn-6002323d.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg11_bn',
    'vgg13_bn-abd245e5.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg13_bn',
    'vgg16_bn-6c64b313.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg16_bn',
    'vgg19_bn-c79401a0.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg19_bn',
    'squeezenet1_0-b66bff10.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=squeezenet1_0',
    'squeezenet1_1-b8a52dc0.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=squeezenet1_1',
    'inception_v3_google-0cc3c7bd.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=inception_v3_google',
    'densenet121-a639ec97.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=densenet121',
    'densenet169-b2777c0a.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=densenet169',
    'densenet201-c1103571.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=densenet201',
    'densenet161-8d451a50.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=densenet161',
    'mnasnet0.5_top1_67.823-3ffadce67e.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mnasnet0.5',
    'mnasnet1.0_top1_73.512-f206786ef8.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mnasnet1.0',
    'mobilenet_v2-b0353104.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mobilenetv2',
    'mobilenet_v3_large-8738ca79.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mobilenetv3_large',
    'mobilenet_v3_small-047dcff4.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mobilenetv3_small',
    'shufflenetv2_x0.5-f707e7126e.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=shufflenetv2_x0.5',
    'shufflenetv2_x1-5666bf0f80.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=shufflenetv2_x1',
    'fcn_resnet50_coco-1167a1af.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=fcn_resnet50_coco',
    'fcn_resnet101_coco-7ecb50ca.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=fcn_resnet101_coco',
    'deeplabv3_resnet50_coco-cd0a2569.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=deeplabv3_resnet50_coco',
    'deeplabv3_resnet101_coco-586e9e4e.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=deeplabv3_resnet101_coco',
    'deeplabv3_mobilenet_v3_large-fc3c493d.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=deeplabv3_mobilenet_v3_la',
    'lraspp_mobilenet_v3_large-d234d4ea.ckpt':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=lraspp_mobilenet_v3_large',
    'fasterrcnn_resnet50_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=fasterrcnn_resnet50_fpn_c',
    'fasterrcnn_mobilenet_v3_large_320_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=fasterrcnn_mobilenet_v3_l',
    'fasterrcnn_mobilenet_v3_large_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=fasterrcnn_mobilenet_coco',
    'keypointrcnn_resnet50_fpn_coco_legacy':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=keypointrcnn_resnet50_fpn',
    'keypointrcnn_resnet50_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=keypointrcnn_resnet50_coc',
    'maskrcnn_resnet50_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=maskrcnn_resnet50_fpn_coc',
    'retinanet_resnet50_fpn_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=retinanet_resnet50_fpn_co',
    'ssd300_vgg16_coco':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=ssd300_vgg16_coco',
    'vgg16_features':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=vgg16_features',
    'r3d_18':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=r3d_18',
    'mc3_18':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=mc3_18',
    'r2plus1d_18':'https://openi.pcl.ac.cn/OpenI/MSAdapter/modelmanage/show_model_info?name=r2plus1d_18',
}

model_path_name = "https://download.pytorch.org/models/"

def check_ckpt_file(ckpt_file_name):
    if not isinstance(ckpt_file_name, str):
        raise TypeError("For 'load', the argument 'ckpt_file_name' must be string, "
                        "but got {}.".format(type(ckpt_file_name)))

    if ckpt_file_name[-4:] != ".pth":
        raise ValueError("For 'load', the checkpoint file should end with '.pth', please "
                         "input the correct 'ckpt_file_name'.")
