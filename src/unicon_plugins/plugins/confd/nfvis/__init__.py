__author__ = "Dave Wapstra <dwapstra@cisco.com>"


from unicon_plugins.plugins.confd import ConfdServiceList, ConfdConnection, ConfdConnectionProvider
from .statemachine import NfvisStateMachine
from unicon_plugins.plugins.confd.settings import ConfdSettings


class NfvisServiceList(ConfdServiceList):
    def __init__(self):
        super().__init__()
        delattr(self, 'cli_style')


class NfvisSingleRPConnection(ConfdConnection):
    os = 'confd'
    series = 'nfvis'
    chassis_type = 'single_rp'
    state_machine_class = NfvisStateMachine
    connection_provider_class = ConfdConnectionProvider
    subcommand_list = NfvisServiceList
    settings = ConfdSettings()
