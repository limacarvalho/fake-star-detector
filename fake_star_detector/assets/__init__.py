from dagster import load_assets_from_modules

from . import simpler_model

simpler_model_assets = load_assets_from_modules([simpler_model], key_prefix="simpler_model", group_name="simpler_model")
