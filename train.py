from pytorch_lightning.plugins.training_type.ddp import DDPPlugin
from pytorch_lightning.utilities.cli import LightningCLI

from swinArm.datamodule import CROHMEDatamodule
from swinArm.lit_comer import LitCoMER

cli = LightningCLI(
    LitCoMER,
    CROHMEDatamodule,
    save_config_overwrite=True,
    trainer_defaults={"plugins": DDPPlugin(find_unused_parameters=False)},
)
