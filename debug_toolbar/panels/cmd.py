from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import DebugPanel

class CmdDebugPanel(DebugPanel):
    """
    settings.py:
    
    from debug_toolbar.utils.debug_cmd import DebugCmd
    ... import some callable actions ...
    
    DEBUG_CMD_FUNCTIONS = (
        DebugCmd('name/id', 'verbose_name', callable[, params]) # params not implemented right
    )
    # left it for easier function search
    DEBUG_CMD_FUNCTIONS = dict(((debug_cmd.name, debug_cmd) for debug_cmd in DEBUG_CMD_FUNCTIONS))

    initially written to login-logout as different user-types *faster*
    """
    name = 'Cmd'
    has_content = True
    cmds = hasattr(settings, 'DEBUG_CMD_FUNCTIONS') and \
            settings.DEBUG_CMD_FUNCTIONS.values() or \
            None

    def title(self):
        return _('Cmd Debug')

    def nav_title(self):
        return _('Cmd Debug')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update({
            'cmds': self.cmds
        })

        return render_to_string('debug_toolbar/panels/cmd.html', context)

