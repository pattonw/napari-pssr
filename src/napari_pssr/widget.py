from magicgui import magic_factory
import napari


@magic_factory
def train_pssr_widget(
    model: str,
    high_res: napari.layers.Image,
    bluring: float,
    noise: float,
    downsampling: float,
):
    pass


@magic_factory
def predict_pssr_widget(
    model: str,
    raw: napari.layers.Image,
):
    pass
