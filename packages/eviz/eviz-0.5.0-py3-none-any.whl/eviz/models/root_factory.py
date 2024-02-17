from dataclasses import dataclass

from eviz.lib.eviz.config import Config
from eviz.models.esm.generic import Generic
from eviz.models.esm.geos import Geos
from eviz.models.esm.lis import Lis
from eviz.models.esm.wrf import Wrf
from eviz.models.obs.inventory.airnow import Airnow
from eviz.models.obs.inventory.fluxnet import Fluxnet
from eviz.models.obs.satellite.landsat import Landsat
from eviz.models.obs.satellite.mopitt import Mopitt
from eviz.models.obs.satellite.omi import Omi


class RootFactory:
    config: Config

    def create_root_instance(self, config):
        raise NotImplementedError("create_root_instance must be implemented in subclasses")


@dataclass
class GenericFactory(RootFactory):
    def create_root_instance(self, config):
        return Generic(config)


@dataclass
class GeosFactory(RootFactory):
    def create_root_instance(self, config):
        return Geos(config)

@dataclass
class WrfFactory(RootFactory):
    def create_root_instance(self, config):
        return Wrf(config)


@dataclass
class LisFactory(RootFactory):
    def create_root_instance(self, config):
        return Lis(config)

@dataclass
class AirnowFactory(RootFactory):
    def create_root_instance(self, config):
        return Airnow(config)


@dataclass
class OmiFactory(RootFactory):
    def create_root_instance(self, config):
        return Omi(config)


@dataclass
class MopittFactory(RootFactory):
    def create_root_instance(self, config):
        return Mopitt(config)


@dataclass
class LandsatFactory(RootFactory):
    def create_root_instance(self, config):
        return Landsat(config)


@dataclass
class FluxnetFactory(RootFactory):
    def create_root_instance(self, config):
        return Fluxnet(config)
