import tornado.web
import json
import arabic_reshaper
from bidi.algorithm import get_display
import Bahr_template 

class PdfCreatorHandler(tornado.web.RequestHandler):

    def get(self):
        title = self.get_argument('title')
        author = self.get_argument('author')
        # result = self.books.add_book(title, author)
        # self.write(result)
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))

        x = Bahr_template.BahrTemplateGenerator()
        x.build_pdf(data)
        print(data)
        # self.write(result)