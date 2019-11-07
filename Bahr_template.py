from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle, ListFlowable, ListItem
  
import time
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import os
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT
from reportlab.graphics.shapes import Drawing, Line
import arabic_reshaper
from bidi.algorithm import get_display

PAGESIZE = (140 * mm, 216 * mm)
BASE_MARGIN = 2 * mm

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pdfmetrics.registerFont(TTFont('Arabic', 'arabic.ttf'))

# Some of the following statements are true and others are false. 

class BahrTemplateGenerator:

    def add_page_number(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 10)
        page_number_text = "%d" % (doc.page)
        canvas.drawCentredString(
            0.75 * inch,
            0.75 * inch,
            page_number_text
        )
        canvas.restoreState()
    def draw_line(self,x1,y1,x2,y2, line_color=colors.black):
        drawable_line = Drawing(x1,y1) 
        drawable_line.add(Line(0,0,x2,y2, fillColor=line_color))
        return drawable_line

    def get_body_style(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style=sample_style_sheet['BodyText']
        body_style.fontSize = 18
        return body_style
    def get_normal_style(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style=sample_style_sheet['Code']
        body_style.fontSize = 18
        return body_style
    def add_logos(self,link1,link2):
        im = [
            [Image(link1, 1.6*inch, .75*inch ),[],Image(link2, .70*inch, .5*inch)]
            ]
        return im

    def add_date_time(self):
        sample_style_sheet = getSampleStyleSheet()
        formatted_time = time.ctime()        
        body_style=sample_style_sheet['Definition']
        body_style.leftIndent = 200
        ptext = '<font size=8>Issued on %s</font>' % formatted_time
        ptext = Paragraph(ptext, body_style)
        return ptext

    def add_headings(self,client,freelancer):
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT, leftIndent =-50, fontSize=14))
        styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, rightIndent =-50, fontSize=14 ))

        header_title = [
            [Paragraph("Client #" + client, styles['Left']),Paragraph("Freelancer #" +freelancer, styles['Right'])]
        ]
        return header_title
    def add_project_header(self,project_no):
        sample_style_sheet = getSampleStyleSheet()
        body_style=sample_style_sheet['Heading5']
        return Paragraph("PROJECT #" + project_no, body_style)

    def add_project_table(self,project_details):
        sample_style_sheet = getSampleStyleSheet()
        body_style = sample_style_sheet['BodyText']
        projects_table = [
            [Paragraph("Title", body_style), Paragraph(project_details['Title'] , body_style)],
            [Paragraph("URL", body_style), Paragraph(project_details['URL'], body_style)],

            [Paragraph("Proposal Price", body_style), Paragraph(project_details['Proposal Price'], body_style)]
        ]
        return projects_table

    def add_payments_header(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style=sample_style_sheet['Heading5']
        return Paragraph("Payments(S)", body_style)

    def add_payments_table(self,payments):
        sample_style_sheet = getSampleStyleSheet()
        body_style = sample_style_sheet['BodyText']
        # normal_style = sample_style_sheet['Normal']
        payments_table = [[Paragraph("Milestone", body_style), Paragraph("Status" , body_style),Paragraph("Date" , body_style),Paragraph("Amount (SAR)" , body_style)],]
        for key, value in payments.items():
            # print(key,'-->', value['Status'])
            payments_table.append([Paragraph(key, body_style), Paragraph(value['Status'], body_style),Paragraph(value['Date'] , body_style),Paragraph(value['Amount (SAR)'] , body_style)])
        
        return payments_table

    def add_terms_header(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style=sample_style_sheet['Heading5']
        return Paragraph("TERMS", body_style)

    def add_terms(self,list):
        style = ParagraphStyle(
                name='Normal',
                fontName='Arabic',
                fontSize=8,
            )
        table=ListFlowable([ListItem(Paragraph(x, style), leftIndent=35, bulletColor='black') for x in list], bulletType='bullet')
        return table


    def build_pdf(self,data):
        
        payments = data['payments']
        project_details = data['project_details']
        terms = data['terms']

        if payments is None or project_details is None or terms is None :
            return False

        for i in range(len(terms)):
            terms[i] = arabic_reshaper.reshape(terms[i])
            terms[i] = get_display(terms[i])




        flowables =[]
        # d = shapes.Drawing(100, 1) #line 
        link2 = "bahr_logo.png"
        link1 = "invoice.png"

        timestr = time.strftime("%Y%m%d-%H%M%S")

        my_doc = SimpleDocTemplate(
            "/home/khaledawad/PdfCreator/" +timestr+".pdf",
            pagesize=PAGESIZE,
            topMargin=BASE_MARGIN,
            leftMargin=BASE_MARGIN,
            rightMargin=BASE_MARGIN,
            bottomMargin=BASE_MARGIN
        )

        
        #################### LOGO SECTION ####################
        chart_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                          ('VALIGN', (0, 0), (1, -1), 'RIGHT')])

        logo =Table(self.add_logos(link1,link2),colWidths=(15*mm,90*mm,15*mm),style=chart_style)

        flowables.append(logo)
           
        date_time = self.add_date_time()
        flowables.append(date_time)

        #################### client_freelancer SECTION ####################

        client_freelancer_header = Table(self.add_headings("client","free"),colWidths=(50*mm,50*mm))
        flowables.append(client_freelancer_header)


        flowables.append(self.draw_line(50,50,300,0))


        #################### PROJECT SECTION ####################
        projects_header = self.add_project_header("10")
        projects_table = Table(self.add_project_table(project_details),colWidths=(30*mm,100*mm))



        projects_table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,3),colors.khaki),
                   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                   ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                #    ("LINEBELOW", (0, 0), (-1, -2), 1, colors.black)

                   ]))


        flowables.append(projects_header)
        flowables.append(self.draw_line(50,5,300,0))
        flowables.append(Spacer(1, 10))
        flowables.append(projects_table)
        flowables.append(Spacer(1, 40))


        #################### PAYMENTS SECTION ####################
        payments_header = self.add_payments_header()
        payments_table = Table(self.add_payments_table(payments))
        payments_table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(4,0),colors.khaki),
                   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                   ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                   ]))

        flowables.append(payments_header)
        flowables.append(self.draw_line(50,5,300,0))
        flowables.append(Spacer(1, 10))
        flowables.append(payments_table)

        flowables.append(PageBreak())
        #################### END PAGE 1 ####################
        
        logo =Table(self.add_logos(link1,link2),colWidths=(30*mm,70*mm,30*mm))
        flowables.append(logo)
        
        #################### TERMS SECTION ####################
        terms_header = self.add_terms_header()
        flowables.append(terms_header)
        flowables.append(self.draw_line(50,5,300,0))
        flowables.append(Spacer(1, 10))
        flowables.append(self.add_terms(terms))


        my_doc.build(
            flowables,
            onFirstPage=self.add_page_number,
            onLaterPages=self.add_page_number,
        )

        return True

