__author__ = "Giacomo Trifilo <gtrifilo@cisco.com>"


from unicon.bases.routers.connection import BaseSingleRpConnection
from unicon_plugins.plugins.generic.statemachine import GenericSingleRpStateMachine
from unicon_plugins.plugins.generic import ServiceList
from unicon_plugins.plugins.generic import GenericSingleRpConnectionProvider
from unicon_plugins.plugins.ios.ap.settings import ApSettings
from unicon_plugins.plugins.ios.ap import service_implementation as svc


class ApServiceList(ServiceList):
    def __init__(self):
        super().__init__()
        self.execute = svc.Execute


class ApSingleRpConnection(BaseSingleRpConnection):
    os = 'ios'
    series = 'ap'
    chassis_type = 'single_rp'
    state_machine_class = GenericSingleRpStateMachine
    connection_provider_class = GenericSingleRpConnectionProvider
    subcommand_list = ApServiceList
    settings = ApSettings()
