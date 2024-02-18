import json
import logging
import os
from logging import Logger
from typing import Any

import matplotlib.pyplot as plt
import mlflow
from pydantic import BaseModel

from experiment_goodies.logger.rainbow_logger import RainbowLoggingHandler


class ExperimentLoggerConfig(BaseModel):
    log_level: str = "INFO"
    log_freq_steps: int = 100
    log_mlflow: bool = False
    mlflow_experiment_id: int = None
    mlflow_run_name: str = None
    mlflow_run_description: str = None
    mlflow_nested_run: bool = False


class ExperimentLogger(Logger):
    """Extends Logger from logging library to incorporate functionalities useful during model training.

    Attributes:
        name (str): owner of this logger (will be printed to console)
        experiment_config (ExperimentConfig): specifies experiment configuration such as network values and dataset structure
        exp_folder (str, optional): folder in which to store logging artifacts generated in this experiment. Defaults to "".

    For mlflow logging purposes, it is assumed that there is a .env file in working directory containing tracking variables:
        MLFLOW_TRACKING_URI (e.g. http://localhost:5000)
        MLFLOW_TRACKING_USERNAME (e.g. admin)
        MLFLOW_TRACKING_PASSWORD (e.g. password)
    """

    def __init__(
        self,
        name: str,
        logger_config: ExperimentLoggerConfig,
        exp_folder: str = "",
    ):
        super().__init__(name, logger_config.log_level)
        self.logger_config = logger_config
        handler = RainbowLoggingHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.addHandler(handler)
        self.exp_folder = exp_folder
        if self.logger_config.log_mlflow:
            assert (
                self.logger_config.mlflow_experiment_id is not None
            ), "Must provide a mlflow experiment id"
            self.__start_mlflow_run()

    def __save_exp_config(self, config: dict[str, Any]):
        """Saves the configuration of this experiment"""
        with open(os.path.join(self.exp_folder, "experiment_config.json"), "w") as f:
            json.dump(config, f, indent=4)

    def __start_mlflow_run(self):
        from dotenv import load_dotenv

        load_dotenv(".env")
        mlflow.start_run(
            experiment_id=self.logger_config.mlflow_experiment_id,
            run_name=self.logger_config.mlflow_run_name,
            nested=self.logger_config.mlflow_nested_run,
            description=self.logger_config.mlflow_run_description,
        )

    def log_config_to_mlflow(
        self, experiment_config: dict[str, Any], dvc_file_path: str
    ) -> mlflow.ActiveRun:
        """Creates a new mlflow run, logging .dvc config file and experiment parameters"""
        mlflow.log_params(experiment_config)
        mlflow.log_artifact(dvc_file_path)

    def log_metrics(self, metrics: dict, epoch: int, step: int, total_step: int):
        """Logs training metrics

        Args:
            metrics (dict): dictionary containing metrics. (eg. {"val_loss":0.509})
            epoch (int): training epoch
            step (int): training step at which metrics were computed
            total_step (int): total training steps in this experiment
        """
        step_info = f"{step}/{total_step}"
        log_msg = f"Epoch: {epoch} | step: {step_info} | "
        for k, v in metrics.items():
            log_msg += f"{k}: {v:.4f} | "
        self.info(log_msg)
        if self.logger_config.log_mlflow:
            mlflow.log_metrics(metrics, step=step)

    def log_epoch_info(self, epoch: int, step: int):
        if self.logger_config.log_mlflow:
            mlflow.log_metric("epoch", epoch, step=step)

    def log_prediction_figure(self, figure: plt.Figure, epoch: int, fig_id: int):
        """Saves a sample prediction figure to disk and logs it to mlflow

        Args:
            figure (plt.Figure): figure containing sample prediction
            epoch (int): epoch of training
            fig_id (int): figure identifier
        """
        fig_path = os.path.join(
            self.exp_folder,
            "figures",
            f"epoch{epoch}_pred_{fig_id}.png",
        )
        figure.savefig(fig_path)
        if self.logger_config.log_mlflow:
            mlflow.log_figure(
                figure, f"predictions_by_epoch/{epoch}/prediction_{fig_id}.png"
            )
        plt.close()

    def log_experiment_config(self, exp_config: dict[str, Any], dvc_file_path: str):
        """Saves configuration, or parameters, of this experiment

        Args:
            exp_config (dict[str, Any]): experiment configuration to be logged
            dvc_file_path (str): path to dvc file of experiment dataset
        """
        self.__save_exp_config(exp_config)
        if self.logger_config.log_mlflow:
            self.log_config_to_mlflow(exp_config, dvc_file_path)

    def end_run(self):
        """Any clean up operations to be performed after experiment ends"""
        self.info("Experiment ended ...")
        if self.logger_config.log_mlflow:
            mlflow.end_run()
