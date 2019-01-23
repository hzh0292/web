import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

define("port", type=int, default=8001)
base_dir = os.path.dirname(__file__)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class StreamHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pic_stream = os.listdir(os.path.join(base_dir, 'static/img/stream'))
        self.render("stream.html", pic_stream=pic_stream)


class ContactHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("contact.html")


urls = [
    (r"/", IndexHandler),
    (r"/stream", StreamHandler),
    (r"/contact", ContactHandler),
]

configs = dict(
    debug=True,
    template_path=os.path.join(base_dir, "templates"),
    static_path=os.path.join(base_dir, "static")
)


class CustomApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        handlers = urls
        settings = configs
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(CustomApplication(urls, configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


app = create_app()

if __name__ == "__main__":
    app()
