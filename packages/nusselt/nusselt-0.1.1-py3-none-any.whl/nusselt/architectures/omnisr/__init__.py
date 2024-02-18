import math

from .omnisr import OmniSR
from ...registry.model_descriptor import StateDict, ModelDescriptor
from ...utilities.state import get_scale_and_output_channels, get_seq_len


def load(state_dict: StateDict) -> ModelDescriptor[OmniSR]:
    window_size = 8

    num_feat = state_dict["input.weight"].shape[0]
    num_in_ch = state_dict["input.weight"].shape[1]

    upscale, num_out_ch = get_scale_and_output_channels(
        state_dict["up.0.weight"].shape[0],
        num_in_ch,
    )

    bias = "input.bias" in state_dict
    res_num = get_seq_len(state_dict, "residual_layer")
    block_num = get_seq_len(state_dict, "residual_layer.0.residual_layer") - 1

    rel_pos_bias_key = "residual_layer.0.residual_layer.0.layer.2.fn.rel_pos_bias.weight"
    if rel_pos_bias_key in state_dict:
        pe = True
        rel_pos_bias_weight = state_dict[rel_pos_bias_key].shape[0]
        window_size = int((math.sqrt(rel_pos_bias_weight) + 1) / 2)
    else:
        pe = False

    model = OmniSR(
        num_in_ch=num_in_ch,
        num_out_ch=num_out_ch,
        num_feat=num_feat,
        up_scale=upscale,
        res_num=res_num,
        pe=pe,
        bias=bias,
        window_size=window_size,
        block_num=block_num,
    )

    return ModelDescriptor(
        model, state_dict, architecture="OmniSR", scale=upscale, input_channels=num_in_ch, output_channels=num_out_ch
    )
