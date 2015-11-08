#!/usr/bin/python3
import cherrypy
import json
import youtube_dl

# Actual Webserver hosting the api calls
# URL: /


class DJServerRoot(object):
    # makes the server visible
    exposed = True

    # Necessary to allow phonegap to connect
    # Changes accepted web headers
    def enableCrossDomain(self):
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers[
            "Access-Control-Allow-Methods"] = "GET, POST, DELETE"
        cherrypy.response.headers[
            "Access-Control-Allow-Headers"] = \
            "Cache-Control, X-Proxy-Authorization, X-Requested-With"

    # Accept plain text
    @cherrypy.tools.accept(media='text/plain')
    # On Post Request
    # Determine the data
    # and cause an action based of it
    # TODO: needs to be under different URLs
    def POST(self, URL):
        import glob
        import shutil
        from mediaConverter import MediaConverter
        ydl_opts = {
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'format': 'bestaudio/best',

        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])
        filesToMove = glob.glob('./*.mp3')
        shutil.move(filesToMove[0], './Music/')
        x = MediaConverter()
        x.main()
        return 'Download Success'


class DJServerRequestSongs(object):
    # makes the server visible
    exposed = True

    # Necessary to allow phonegap to connect
    # Changes accepted web headers
    def enableCrossDomain(self):
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers[
            "Access-Control-Allow-Methods"] = "GET, POST, DELETE"
        cherrypy.response.headers[
            "Access-Control-Allow-Headers"] = \
            "Cache-Control, X-Proxy-Authorization, X-Requested-With"

    # Accept plain text
    @cherrypy.tools.accept(media='text/plain')
    # On Post Request
    # Determine the data
    # and cause an action based of it
    # TODO: needs to be under different URLs
    def POST(self):
        from os import walk
        fileList = walk('./Music')
        songList = []
        for root, b, song in fileList:
            songList.append(song)
        print songList
        return json.dumps(songList)
# Config for Cherrypy
if __name__ == '__main__':
    conf = {
        '/': {
            # Change it to API-style, method dispatcher
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            # Turn on Sessions
            'tools.sessions.on': True,
            # 360 seconds per session
            'tools.sessions.timeout': 360,
            # Headers are on
            'tools.response_headers.on': True,
            # allowed headers are text/plain
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        }
    }
    # update config with 0.0.0.0 (binds to all avaliable addresses)
    # update config to switch to port 12124
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0', 'server.socket_port': 12124})
    cherrypy.tree.mount(DJServerRoot(), '/', {
        '/':
        {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })
    cherrypy.tree.mount(DJServerRequestSongs(), '/songs', {
        '/':
        {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
