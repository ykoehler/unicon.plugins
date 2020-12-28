"""
Module:
    unicon.plugins.ironware.patterns

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    This subpackage defines services specific to the Ironware OS
"""

from unicon.bases.routers.services import BaseService
from unicon.plugins.generic.service_implementation import Execute as GenericExec
from unicon.plugins.generic.service_implementation import Ping as GenericPing
from unicon.eal.dialogs import Dialog
from unicon.core.errors import SubCommandFailure
from unicon.utils import AttributeDict

class Execute(GenericExec):
    """
        Overwrite execute to be IronWare specific if need be
    """

    def call_service(self, *args, **kwargs):
        # call parent
        super().call_service(*args, **kwargs)

class MPLSPing(BaseService):
    """ 
        Service to issue ping across MPLS RSVP LSP on the Brocade/Ironware Platform

        Returns:
            ping command response on Success (Not parsed)

        Raises:
            SubCommandFailure on failure

        Example:
            mpls_ping(lsp="mlx8.1_to_ces.2")
    """
    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.dialog = Dialog([])

        # MPLS Ping Error Pattern
        self.error_pattern = [
            'Ping fails: LSP is down'
        ]

        self.__dict__.update(kwargs)
    
    def call_service(self, lsp, timeout=20, **kwargs):
        # Stringify the command in case it is an object
        ping_str = str('ping mpls rsvp lsp {lsp}'.format(lsp=lsp))
        con = self.connection
        con.log.debug('+++ mpls ping +++')

        mpls_ping_context = AttributeDict({})
        for key in kwargs:
            mpls_ping_context[key] = str(kwargs[key])

        dialog = self.service_dialog(service_dialog=self.dialog)
        spawn = self.get_spawn()
        sm = self.get_sm()

        spawn.sendline(ping_str)
        try:
            self.result = dialog.process(
                spawn, context=mpls_ping_context,
                timeout=timeout)
        except TimeoutError:
            # Recover prompt and re-raise
            # Ctrl+shift+6
            spawn.send('\x1E')
            # Empty buffer
            spawn.expect(".+", trim_buffer=True)
            raise
        except Exception as err:
            raise SubCommandFailure("MPLS Ping failed", err) from err
        
        self.result = self.result.match_output
        if self.result.rfind(self.connection.hostname):
            self.result = self.result[
                :self.result.rfind(self.connection.hostname)]
        
        