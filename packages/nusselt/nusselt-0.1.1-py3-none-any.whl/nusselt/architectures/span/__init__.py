from .span import SPAN
from ...registry.model_descriptor import StateDict, ModelDescriptor
from ...utilities.state import get_scale_and_output_channels


def load(state_dict: StateDict) -> ModelDescriptor[SPAN]:
    img_range = 255.0
    rgb_mean = (0.4488, 0.4371, 0.4040)

    num_in_ch = state_dict["conv_1.sk.weight"].shape[1]
    feature_channels = state_dict["conv_1.sk.weight"].shape[0]

    upscale, num_out_ch = get_scale_and_output_channels(
        state_dict["upsampler.0.weight"].shape[0],
        num_in_ch,
    )
    bias = "block_1.c1_r.sk.bias" in state_dict

    model = SPAN(
        num_in_ch,
        num_out_ch,
        feature_channels,
        upscale,
        bias,
        img_range,
        rgb_mean,
    )

    return ModelDescriptor(
        model,
        state_dict,
        architecture="SPAN",
        scale=upscale,
        input_channels=num_in_ch,
        output_channels=num_out_ch
    )
