# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import json
from pathlib import Path

from azureml.acft.common_components import get_logger_app
from azureml.acft.accelerator.finetune import AzuremlFinetuneArgs

from ....constants.constants import SaveFileConstants


logger = get_logger_app(__name__)


class FinetuneBase:
    def _save_mininum_finetune_args(self, finetune_args: AzuremlFinetuneArgs):
        """
        model_selector component reads model_name from finetune_args.json if resume_from_checkpoint=true.
        In case of pre-emption, finetune_args.json will not be found since it's saved after training is successful.
        Here we save a bare-minimum finetune_args.json before the training starts.
        """
        if finetune_args.trainer_args.should_save:
            finetune_args_path = Path(self.finetune_params["pytorch_model_folder"], SaveFileConstants.FINETUNE_ARGS_SAVE_PATH)
            params = {"model_name": self.finetune_params["model_name"]}
            with open(finetune_args_path, 'w') as rptr:
                json.dump(params, rptr, indent=2)
