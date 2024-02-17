"""
    QuaO Project quao_dwave_provider.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from neal import SimulatedAnnealingSampler

from ...config.logging_config import logger
from ...model.provider.quao_provider import QuaoProvider


class QuaoDwaveProvider(QuaoProvider):

    def get_backend(self, device_specification):
        logger.debug('[Quao Dwave] Get backend')

        return SimulatedAnnealingSampler()

    def collect_provider(self):
        return None
