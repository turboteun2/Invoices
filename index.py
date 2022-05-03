from fpdf import FPDF 
import datetime
import csv

pdf = FPDF()    
pdf.add_page()

x = datetime.datetime.now()
date = str(x.day)+'/'+str(x.month)+'/'+str(x.year)
invoice = "123456789"

# Get customers
customer_number = []
customer_name = []
def select_company():
    with open("customer.csv", 'r') as chart: 
            # creating a csv reader object
            charts = csv.reader(chart)
            num = 0
            for row in charts:
                customer_number.append(row[0])
                customer_name.append(row[1])
                print(num, '-', customer_number[num], customer_name[num])
                num += 1

            company = int(input("Please select a company: "))
            return customer_name[company]

def create_pdf():
    pdf.image('./logo.png',w=15,h=15) # Company logo
    pdf.set_font('Arial', '', 38)
    pdf.text(txt="Invoice",x=158,y=23) # Invoice name
    pdf.set_font('Arial', '', 16)
    pdf.text(txt="Date: "+date,x=8,y=38)
    pdf.set_font('Arial', '', 22)
    pdf.text(txt="Bill to:",x=8,y=50)
    pdf.set_font('Arial', '', 18)
    pdf.text(txt="Invoice number: "+invoice,x=122,y=37)
    pdf.text(txt=select_company(),x=10,y=58)

# Get charts
chart_number = []
chart_name = []
with open("chart.csv", 'r') as chart:
        # creating a csv reader object
        charts = csv.reader(chart)
        for row in charts:
            chart_number.append(row[0])
            chart_name.append(row[1])

create_pdf()

pdf.output('invoices/tst.pdf')