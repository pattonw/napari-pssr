import bioimageio.core
import os
import numpy as np
import torch


# first new model: add thresholding of outputs as post-processing
# the convenience function `build_model` creates a biomageio model spec compatible package (=zipped folder)
from bioimageio.core.build_spec import build_model

# create a subfolder to store the files for the new model
model_root = "./models"
os.makedirs(model_root, exist_ok=True)

# create the expected output tensor (= outputs thresholded at 0.5)
new_output = np.random.randn(1, 3, 10, 10)
new_output_path = f"{model_root}/new_test_output.npy"
np.save(new_output_path, new_output)
new_input = np.random.randn(1, 3, 10, 10)
new_input_path = f"{model_root}/new_test_input.npy"
np.save(new_input_path, new_input)

# add thresholding as post-processing procedure to our model
preprocessing = []
postprocessing = []

# get the model architecture
# note that this is only necessary for pytorch state dict models
model_source = "scripts/unet.py:Learner"


# the name of the new model and where to save the zipped model package
name = "baseline_pssr_1024"
zip_path = os.path.join(model_root, f"{name}.zip")

cite = [{"text": "Test", "doi": "NA"}]

# the axes descriptions for the inputs / outputs
input_axes = ["bcyx"]
output_axes = ["bcyx"]

# the pytorch_state_dict weight file
weight_file = "scripts/baseline_pssr_1024.pt"
model = torch.load(f"scripts/{name}.mdl")
torch.save({f"model.{k}": v for k, v in model.state_dict().items()}, weight_file)

# the path to save the new model with torchscript weights
zip_path = f"{model_root}/{name}.zip"

# build the model! it will be saved to 'zip_path'
new_model_raw = build_model(
    weight_uri=weight_file,
    test_inputs=[new_input_path],
    test_outputs=[new_output_path],
    input_axes=input_axes,
    input_names=["pssr"],
    input_min_shape=[[1, 1, 128, 128]],
    input_step=[[0, 0, 0, 0]],
    output_reference=["pssr"],
    output_axes=output_axes,
    output_scale=[[1, 1, 4, 4]],
    output_offset=[[0, 0, 0, 0]],
    halo=[[0, 0, 0, 0]],
    output_path=zip_path,
    name=name,
    description="pssr model",
    authors=[{"name": "Jane Doe"}],
    documentation="scripts/docs.md",
    tags=["pssr"],
    cite=cite,
    architecture=model_source,
    model_kwargs={"learner": "baseline_pssr_1024.mdl"},
    attachments={"files": ["scripts/baseline_pssr_1024.mdl"]},
)

