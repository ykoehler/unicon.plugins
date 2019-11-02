__author__ = "Syed Raza <syedraza@cisco.com>"

from unicon.bases.routers.connection import BaseSingleRpConnection, \
   BaseDualRpConnection
from unicon_plugins.plugins.iosxr.settings import IOSXRSettings
from unicon_plugins.plugins.iosxr.statemachine import IOSXRSingleRpStateMachine, \
   IOSXRDualRpStateMachine
from unicon_plugins.plugins.generic import ServiceList, HAServiceList
from unicon_plugins.plugins.iosxr import service_implementation as svc
from unicon_plugins.plugins.iosxr.connection_provider import \
    IOSXRSingleRpConnectionProvider, IOSXRDualRpConnectionProvider
from unicon_plugins.plugins.iosxe.service_implementation import Ping as IosXePing


class IOSXRServiceList(ServiceList):
    def __init__(self):
        super().__init__()
        self.execute = svc.Execute
        self.configure = svc.Configure
        self.admin_execute = svc.AdminExecute
        self.admin_configure = svc.AdminConfigure
        self.attach_console = svc.AttachModuleConsole
        self.bash_console = svc.BashService
        self.admin_console = svc.AdminService
        self.admin_attach_console = svc.AdminAttachModuleConsole
        self.admin_bash_console = svc.AdminBashService
        self.ping = IosXePing

class IOSXRHAServiceList(HAServiceList):
    """ Generic dual rp services. """
    def __init__(self):
        super().__init__()
        self.execute = svc.HAExecute
        self.configure= svc.HaConfigureService
        self.admin_execute = svc.HaAdminExecute
        self.admin_configure = svc.HaAdminConfigure
        self.switchover = svc.Switchover
        self.attach_console = svc.AttachModuleConsole
        self.bash_console = svc.BashService
        self.admin_console = svc.AdminService
        self.admin_attach_console = svc.AdminAttachModuleConsole
        self.admin_bash_console = svc.AdminBashService


class IOSXRSingleRpConnection(BaseSingleRpConnection):
    os = 'iosxr'
    series = None
    chassis_type = 'single_rp'
    state_machine_class = IOSXRSingleRpStateMachine
    connection_provider_class = IOSXRSingleRpConnectionProvider 
    subcommand_list = IOSXRServiceList
    settings = IOSXRSettings()


class IOSXRDualRpConnection(BaseDualRpConnection):
    os = 'iosxr'
    series = None
    chassis_type = 'dual_rp'
    state_machine_class = IOSXRDualRpStateMachine
    connection_provider_class = IOSXRDualRpConnectionProvider
    subcommand_list = IOSXRHAServiceList
    settings = IOSXRSettings()
