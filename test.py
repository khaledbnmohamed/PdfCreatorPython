from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
 
 #Create your first pdf using basic template library
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
 
#create array of flowables to append your elements in
Story=[]
 
full_name = "Mike Driscoll"
address_parts = "411 State St.Marshalltown, IA 50158"
 
#create your styling varaible as instance of template style sheet
 
styles=getSampleStyleSheet()
 
 
Story.append(Paragraph(full_name, styles["Normal"]))      
 
Story.append(Paragraph(address_parts, styles["Normal"]))      
 
#build your PDF from the array of the flowables you just filled
doc.build(Story)