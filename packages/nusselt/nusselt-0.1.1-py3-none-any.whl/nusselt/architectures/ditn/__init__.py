from .ditn_real import DITN_Real
from ...registry.model_descriptor import ModelDescriptor, StateDict
from ...utilities.state import get_seq_len, get_scale_and_output_channels


def load(state_dict: StateDict) -> ModelDescriptor[DITN_Real]:
    LayerNorm_type = "WithBias"  # unused internally
    patch_size = 8  # cannot be deduced from state_dict

    inp_channels = state_dict["sft.weight"].shape[1]
    dim = state_dict["sft.weight"].shape[0]

    UFONE_blocks = get_seq_len(state_dict, "UFONE")
    ITL_blocks = get_seq_len(state_dict, "UFONE.0.ITLs")
    SAL_blocks = get_seq_len(state_dict, "UFONE.0.SALs")

    ffn_expansion_factor = state_dict["UFONE.0.ITLs.0.ffn.project_in.weight"].shape[0] / 2 / dim

    bias = "UFONE.0.ITLs.0.attn.project_out.bias" in state_dict

    upscale, _ = get_scale_and_output_channels(state_dict["upsample.0.weight"].shape[0], inp_channels)

    model = DITN_Real(
        inp_channels=inp_channels,
        dim=dim,
        ITL_blocks=ITL_blocks,
        SAL_blocks=SAL_blocks,
        UFONE_blocks=UFONE_blocks,
        ffn_expansion_factor=ffn_expansion_factor,
        bias=bias,
        LayerNorm_type=LayerNorm_type,
        patch_size=patch_size,
        upscale=upscale,
    )

    return ModelDescriptor(
        model=model,
        state_dict=state_dict,
        architecture="DITN",
        scale=upscale,
        input_channels=inp_channels,
        output_channels=3,
    )
