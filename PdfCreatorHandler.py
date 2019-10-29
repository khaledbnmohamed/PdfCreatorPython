import tornado.web
import json
import arabic_reshaper
from bidi.algorithm import get_display
import Bahr_template 

class PdfCreatorHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))

        Generator = (self.request.headers.get('Template-Name'))
        
        x = Bahr_template.BahrTemplateGenerator()
        x = x.build_pdf(data)
        print(data)
        if(x == False):
            self.set_status(201)
            self.write("Wrong parameter")

        else:
            self.write({'Response': "everything is good"})
            print(data)
 

