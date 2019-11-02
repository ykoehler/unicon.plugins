""" Defines the settings for aci based unicon connections """

__author__ = "dwapstra"

from unicon_plugins.plugins.generic.settings import GenericSettings


class AciSettings(GenericSettings):
    """" Generic platform settings """
    def __init__(self):
        """ initialize
        """
        super().__init__()
        self.TERM = 'vt100'
        self.HA_INIT_EXEC_COMMANDS = []
        self.HA_INIT_CONFIG_COMMANDS = []

        self.POST_RELOAD_WAIT = 30
