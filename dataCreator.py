
import json

data = {}
payments ={ 'Milestone1' : {'Status':'Not Paid', 'Date':'06-03-2019', 'Amount (SAR)':'500.0'},
            'Milestone2' : {'Status':'Paid', 'Date':'16-03-2019', 'Amount (SAR)':'100.0'},
            'Milestone3' : {'Status':'Paid', 'Date':'16-03-2019', 'Amount (SAR)':'200.0'},
            'Milestone4' : {'Status':'Paid', 'Date':'16-03-2019', 'Amount (SAR)':'400.0'},
            'Milestone5' : {'Status':'Paid', 'Date':'16-03-2019', 'Amount (SAR)':'500.0'},
            'Milestone6' : {'Status':'Not Paid', 'Date':'16-03-2019', 'Amount (SAR)':'500.0'}

            }
project_details = {'Title':'Test payment gateway 9', 'URL':'http://uat-bahrsa.910ths.sa/projects/642', 'Publish Date':'Wed 06 Mar 2019 - 04:23 PM', 'Proposal Price':''}


terms = ["Khalod may receive his money to the Bank by submitting withdraw request at Bahr portal.","Client pay the millstones amount to the freelancer.","Project deliverables provided by the freelancer to the client.",'اللغة العربية هي اللغة الأولي في الحياة ولما نموت وكل حاجة','من أدمن قرع الباب يوشك ان يفتح له','في الليلة الظلماء يغتقد النور أكيد يعني']

data['payments'] = payments
data['project_details'] = project_details
data['terms'] = terms

with open('/home/khaledawad/PdfCreator/data.json', 'w') as json_file:
  json.dump(data, json_file,ensure_ascii=False)



