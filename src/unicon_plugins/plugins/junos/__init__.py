"""
Module:
    unicon_plugins.plugins.junos

Authors:
    pyATS TEAM (pyats-support@cisco.com, pyats-support-ext@cisco.com)

Description:
    This subpackage implements Junos devices
"""
from unicon.bases.routers.connection import BaseSingleRpConnection
from unicon_plugins.plugins.junos.connection_provider import JunosSingleRpConnectionProvider
from .statemachine import JunosSingleRpStateMachine
from .setting import JunosSettings
from unicon_plugins.plugins.generic import ServiceList
from unicon_plugins.plugins.junos import service_implementation as svc


class JunosServiceList(object):
    def __init__(self):
        self.send = svc.Send
        self.sendline = svc.Sendline
        self.expect = svc.Expect
        self.execute = svc.Execute
        self.configure = svc.Configure
        self.enable = svc.Enable
        self.disable = svc.Disable
        self.expect_log = svc.ExpectLogging
        self.log_user = svc.LogUser
        self.bash_console = svc.BashService


class JunosSingleRpConnection(BaseSingleRpConnection):
    os = 'junos'
    series = None
    chassis_type = 'single_rp'
    state_machine_class = JunosSingleRpStateMachine
    connection_provider_class = JunosSingleRpConnectionProvider
    subcommand_list = JunosServiceList
    settings = JunosSettings()
