import tornado.ioloop
import tornado.web
# import JsonReader  
import PdfCreatorHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
       self.write("Book Microservice v1")
def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/createPDF", PdfCreatorHandler.PdfCreatorHandler),

        ])
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
