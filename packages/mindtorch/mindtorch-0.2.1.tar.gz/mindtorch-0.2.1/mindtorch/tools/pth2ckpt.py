#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from mindtorch.tools.utils import try_import
from mindspore import Tensor, save_checkpoint

def pth2ckpt(path):
    torch = try_import('torch')
    torch_dict = torch.load(path, map_location='cpu')
    ms_params = []
    for name, value in torch_dict.items():
        if isinstance(value, dict):
            for k, v in value.items():
                param_dict = {}
                param_dict['name'] = k
                if isinstance(v, torch.Tensor):
                    param_dict['data'] = Tensor(v.detach().cpu().numpy())
                else:
                    param_dict['data'] = Tensor(v)
                ms_params.append(param_dict)
            continue
        else:
            param_dict = {}
            param_dict['name'] = name
            if isinstance(value, torch.Tensor):
                param_dict['data'] = Tensor(value.detach().cpu().numpy())
            else:
                param_dict['data'] = Tensor(value)
            ms_params.append(param_dict)

    save_checkpoint(ms_params, path[:-3] + "ckpt")
    print("convert ckpt finish.")

if __name__=="__main__":
    pth_file = sys.argc[1]
    pth2ckpt(pth_file)