"""
    QuaO Project dwave_system_device.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from ..device.device import Device
from ...data.device.circuit_running_option import CircuitRunningOption
from ...enum.status.job_status import JobStatus
from ...config.logging_config import *


class DwaveSystemDevice(Device):

    def _create_job(self, circuit, options: CircuitRunningOption):
        logger.debug("[Dwave System] Create job")

        return self.device.sample(circuit)

    def _is_simulator(self) -> bool:
        logger.debug("[Dwave System] Get device type")

        return True

    def _produce_histogram_data(self, job_result) -> dict | None:
        logger.debug("[Dwave System] Produce histogram")

        return None

    def _get_provider_job_id(self, job) -> str:
        logger.debug("[Dwave System] Get provider job id")

        return job.info.get("problem_id")

    def _get_job_status(self, job) -> str:
        logger.debug("[Dwave System] Get job status")

        return JobStatus.DONE.value

    def _calculate_execution_time(self, job_result) -> float:
        logger.debug("[Dwave System] Calculate execution time")

        self.execution_time = (
            job_result.get("_info").get("timing").get("qpu_access_time") / 1000
        )

        logger.debug(
            "[Dwave System] Execution time calculation was: {0} seconds".format(
                self.execution_time
            )
        )
