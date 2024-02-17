"""
    QuaO Project quao_dwave_device.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

import time
import uuid

from ...data.device.circuit_running_option import CircuitRunningOption
from ...enum.status.job_status import JobStatus
from ...model.device.quao_device import QuaoDevice
from ...config.logging_config import logger


class QuaoDwaveDevice(QuaoDevice):
    def _create_job(self, circuit, options: CircuitRunningOption):
        logger.debug('[Quao Annealing] Create job with {0} shots'.format(options.shots))

        start_time = time.time()

        job = self.device.sample(circuit)

        self.execution_time = time.time() - start_time

        return job

    def _produce_histogram_data(self, job_result) -> dict | None:
        logger.debug('[Quao Annealing] Produce histogram')

        return None

    def _get_provider_job_id(self, job) -> str:
        logger.debug('[Quao Annealing] Get provider job id')

        return str(uuid.uuid4())

    def _get_job_status(self, job) -> str:
        logger.debug('[Quao Annealing] Get job status')

        return JobStatus.DONE.value

    def _get_job_result(self, job):
        logger.debug('[Quao Annealing] Get job result')

        return job
