#!/usr/local/bin/python3.2
import cherrypy

#STATIC_FILES = os.path.join(os.path.abspath("."), u"static")

class Root(object):
    @cherrypy.expose
    def index(self):
        return 'Hello, this is your default site.'
    #@cherrypy.expose
    #def license(self):
    #    return os.path.join(STATIC_FILES, u'license.html')
    #    #return open(os.path.join(STATIC_FILES, u'network.html'))    

cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 28627,
})
cherrypy.quickstart(Root())
