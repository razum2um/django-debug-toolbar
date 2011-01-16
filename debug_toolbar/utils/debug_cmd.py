from django.core.exceptions import ImproperlyConfigured

class DebugCmd(object):
    def __init__(self, name, verbose_name, fn, params=None):
        self.name = name
        self.verbose_name = verbose_name
        if hasattr(fn, '__call__'): 
            self.fn = fn 
            self.doc = fn.__doc__
        else:
            raise ImproperlyConfigured('Debug cmd must have a callable intead of %s' % str(fn))
        self.params = params

    def __repr__(self):
        return '#'.join(['DebugCmd', self.name, str(self.params)])
