import tifffile

from pathlib import Path

LR_8NM_EM = Path(__file__).parent / "sample_data/LR/8nm_em_sample/00.tif"


def sample_lr_em():
    image = tifffile.imread(LR_8NM_EM)
    return [
        (
            image[:],
            {
                "name": "Raw",
                "metadata": {"axes": ["y", "x"]},
            },
            "image",
        )
    ]
