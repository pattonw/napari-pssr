import tifffile

from pathlib import Path

LR_LARGE= Path(__file__).parent / "LR/large.tif"
LR_8NM_EM = Path(__file__).parent / "LR/small.tif"
HR_2NM_EM = Path(__file__).parent / "HR/small.tif"


def lr_em_small():
    lr = tifffile.imread(LR_8NM_EM)
    return [
        (
            lr[:, :],
            {
                "name": "Low Res",
                "metadata": {"axes": ["y", "x"]},
                "scale": [8, 8],
            },
            "image",
        )
    ]


def hr_em_small():
    hr = tifffile.imread(HR_2NM_EM)
    return [
        (
            hr[:, :],
            {
                "name": "High Res",
                "metadata": {"axes": ["y", "x"]},
                "scale": [2, 2],
            },
            "image",
        ),
    ]

def lr_em_large():
    hr = tifffile.imread(LR_LARGE)
    return [
        (
            hr[:, :],
            {
                "name": "Low Res Large",
                "metadata": {"axes": ["y", "x"]},
                "scale": [8, 8],
            },
            "image",
        ),
    ]