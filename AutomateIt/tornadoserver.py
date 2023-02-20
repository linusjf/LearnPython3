#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TornadoServer."""
import tornado.ioloop
import tornado.web
import tornado.gen
import httplib2


# pylint: disable=abstract-method
class AsyncHandler(tornado.web.RequestHandler):
    """AsyncHandler class."""

    def __init__(self):
        """Construct."""
        super().__init__(self, None)
        self.response = None
        self.content = None

    @tornado.gen.coroutine
    def get(self):
        """Get."""
        http = httplib2.Http()
        self.response, self.content = http.request("http://ip.jsontest.com/", "GET")  # noqa
        self._async_callback(self.response, self.content)

    def _async_callback(self, response, content):
        """Call back asynchronously."""
        print("Content:", content)
        print(
            f"Response:\nStatusCode: {response['status']} Location:\
                    {response['content-location']}"
        )
        self.finish()
        tornado.ioloop.IOLoop.instance().stop()


application = tornado.web.Application([(r"/", AsyncHandler)], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
