import torch.nn as nn
from .esa import ESA
from .osa import OSA_Block


class OSAG(nn.Module):
    def __init__(self, channel_num=64, bias=True, block_num=4, window_size=0, pe=False):
        super(OSAG, self).__init__()

        group_list = []
        for _ in range(block_num):
            temp_res = OSA_Block(channel_num, bias, window_size=window_size, with_pe=pe)
            group_list.append(temp_res)
        group_list.append(nn.Conv2d(channel_num, channel_num, 1, 1, 0, bias=bias))
        self.residual_layer = nn.Sequential(*group_list)
        esa_channel = max(channel_num // 4, 16)
        self.esa = ESA(esa_channel, channel_num)

    def forward(self, x):
        out = self.residual_layer(x)
        out = out + x
        return self.esa(out)
