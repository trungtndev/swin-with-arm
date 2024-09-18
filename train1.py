from pytorch_lightning.plugins.training_type.ddp import DDPPlugin
from pytorch_lightning.utilities.cli import LightningCLI

from comer.datamodule import CROHMEDatamodule
from comer.lit_swinArm import LitSwinARM

cli = LightningCLI(
    LitSwinARM,
    CROHMEDatamodule,
    save_config_overwrite=True,
    trainer_defaults={"plugins": DDPPlugin(find_unused_parameters=False)},
)
