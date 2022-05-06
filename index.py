from fpdf import FPDF 
import datetime
import csv
import os



pdf = FPDF()    
pdf.add_page()

x = datetime.datetime.now()
date = str(x.day)+'/'+str(x.month)+'/'+str(x.year)

def invoice_num():
    # TODO Specify your path to invoices
    _, _, files = next(os.walk(""))
    file_count = len(files) + 1

    return str(file_count)

invoice = invoice_num()

customer_number = []
customer_name = []
def select_company():
    with open("customer.csv", 'r') as chart:
            charts = csv.reader(chart)
            num = 0
            for row in charts:
                customer_number.append(row[0])
                customer_name.append(row[1])
                print(num, '-', customer_number[num], customer_name[num])
                num += 1

            company = int(input("Please select a company: "))
            return customer_name[company]

def prices():
    gross_price = 0
    vat_price = 0
    chart_num = []
    chart_name = []
    with open("chart.csv", 'r') as chart:
            # creating a csv reader object
            charts = csv.reader(chart)
            for row in charts:
                chart_num.append(row[0])
                chart_name.append(row[1])
    numb=0
    for name in chart_name:
        print(numb, name)
        numb += 1

    x = int(input("Select number: "))
    desc = input("Set description: ")
    qty = int(input("Set quantity: "))
    _price = int(input("Set price: "))

    if chart_num[x] == "8000":
        # VAT price is: 20%
        y = gross_price + (_price * qty)
        vat =  vat_price + ((_price * .2) * qty)
    elif chart_num[x] == "8010":
        # VAT price is: 0%
        y = gross_price + (_price * qty)
        vat = vat_price + ((_price * .05) * qty)
    else:
        y = gross_price + (_price * qty)
        vat =  0


    gross_price = y
    vat_price = vat

    cmd = []
    cmd.append(str(qty))
    cmd.append(desc)
    cmd.append(gross_price)
    cmd.append(vat_price)
    return cmd


def create_pdf():
    # HEADER #
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
    # BODY #
    pdf.text(txt='QTY',x=4,y=80)
    pdf.text(txt='Description',x=40,y=80)
    pdf.text(txt='Price',x=180,y=80)
    cmd = prices()
    total_price = cmd[2] + cmd[3]
    pdf.text(txt=cmd[0],x=7,y=90)  
    pdf.text(txt=cmd[1],x=41,y=90)  
    pdf.text(txt=str(cmd[2]),x=182,y=90)
    # FOOTER #
    pdf.text(txt='VAT: ',x=5,y=255)
    pdf.text(txt=str(cmd[3]),x=182,y=255)
    pdf.text(txt='Total price: ',x=5,y=262)
    pdf.text(txt=str(total_price),x=182,y=262)
    pdf.set_font('Arial', '', 12)
    pdf.text(txt='Please make sure to pay this invoice within 14 days.',x=5,y=290)

create_pdf()

pdf.output('invoices/invoice_'+invoice+'.pdf')