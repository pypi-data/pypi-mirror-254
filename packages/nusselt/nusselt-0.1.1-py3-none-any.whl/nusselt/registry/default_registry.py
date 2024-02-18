from .architecture_registry import ArchRegistry, ArchSupport
from ..architectures import span, ditn, omnisr

MAIN_REGISTRY = ArchRegistry()

MAIN_REGISTRY.add(
    ArchSupport(
        id="SPAN",
        keys=["block_1.c1_r.sk.weight", "block_1.c2_r.sk.weight", "conv_cat.weight"],
        load=span.load,
    ),
    ArchSupport(
        id="DITN",
        keys=[
            "sft.weight",
            "UFONE.0.ITLs.0.attn.temperature",
            "UFONE.0.ITLs.0.ffn.project_in.weight",
            "UFONE.0.ITLs.0.ffn.dwconv.weight",
            "UFONE.0.ITLs.0.ffn.project_out.weight",
            "conv_after_body.weight",
            "upsample.0.weight",
        ],
        load=ditn.load,
    ),
    ArchSupport(
        id="OmniSR",
        keys=["residual_layer.0.residual_layer.0.layer.0.fn.0.weight"],
        load=omnisr.load,
    ),
)
