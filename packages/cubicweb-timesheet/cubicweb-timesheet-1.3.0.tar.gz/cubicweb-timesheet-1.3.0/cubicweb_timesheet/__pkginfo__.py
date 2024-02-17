# pylint: disable-msg=W0622
"""cubicweb-timesheet application packaging information"""

modname = 'timesheet'
distname = 'cubicweb-%s' % modname

numversion = (1, 3, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
description = 'record who did what and when for the CubicWeb framework'
web = 'http://www.cubicweb.org/project/%s' % distname
author = 'Logilab'
author_email = 'contact@logilab.fr'
classifiers = [
           'Environment :: Web Environment',
           'Framework :: CubicWeb',
           'Programming Language :: Python',
           'Programming Language :: JavaScript',
           ]

__depends__ = {'cubicweb': '>= 4.0.0, < 5.0.0',
               'cubicweb-web': '>= 1.0.0, < 2.0.0',
               'cubicweb-calendar':  '>= 1.0.0, < 2.0.0',
               'cubicweb-workorder': '>= 1.0.0, < 2.0.0',
               'cubicweb-rqlcontroller': '>= 1.0.0, < 2.0.0',
               }
