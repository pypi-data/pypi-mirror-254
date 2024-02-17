"""
    QuaO Project dwave_system_provider.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from dwave.system import DWaveSampler, EmbeddingComposite

from ...enum.provider_tag import ProviderTag
from ...model.provider.provider import Provider
from ...config.logging_config import *


class DwaveSystemProvider(Provider):

    def __init__(self, api_token):
        super().__init__(ProviderTag.IBM_QUANTUM)
        self.api_token = api_token

    def get_backend(self, device_specification: str):
        logger.debug("[IBM Quantum] Get backend")

        provider = self.collect_provider()

        return EmbeddingComposite(provider)

    def collect_provider(self):
        logger.debug("[IBM Quantum] Connect to provider")

        return DWaveSampler(token=self.api_token)
