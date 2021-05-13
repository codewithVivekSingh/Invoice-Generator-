from tkinter import *
from tkinter import filedialog as fd

from PIL import ImageTk, Image

mainWindow = Tk()
mainWindow.title("Logical Lab Quotation Generator")
mainWindow.configure(bg='white')



def generateInvoice():
    # Importing Required Module
    from reportlab.pdfgen import canvas

    # Creating Canvas
    c = canvas.Canvas(fil.get() + ".pdf", pagesize=(200, 250), bottomup=0)

    # Logo Section
    # Setting th origin to (10,40)
    c.translate(10, 40)
    # Inverting the scale for getting mirror Image of logo
    c.scale(1, -1)
    # Inserting Logo into the Canvas at required position
    #c.drawImage("LLLogo.jpg", 0, 0, width=50, height=30)

    # Title Section
    # Again Inverting Scale For strings insertion
    c.scale(1, -1)
    # Again Setting the origin back to (0,0) of top-left
    c.translate(-10, -40)
    # Setting the font for Name title of company
    c.setFont("Helvetica-Bold", 6)
    # Inserting the name of the company
    c.drawCentredString(105, 20, "LOGICAL LAB PRIVATE LIMITED")
    # For under lining the title
   # c.line(70, 22, 180, 22)
    # Changing the font size for Specifying Address
    c.setFont("Helvetica-Bold", 5)
    c.drawCentredString(105, 30, "195, Indira Nagar")
    c.drawCentredString(105, 35, "Jabalpur, 482009, India")
    # Changing the font size for Specifying GST Number of firm
    c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(105, 42, "GSTIN : 23AAECL1522F1Z4")

    # Line Seprating the page header from the body
    c.line(5, 45, 195, 45)

    # Document Information
    # Changing the font for Document title
    c.setFont("Courier-Bold", 8)
    c.drawCentredString(100, 55, "INVOICE")

    # This Block Consist of Costumer Details
    c.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)
    c.setFont("Times-Bold", 5)
    c.drawRightString(70, 70, "Quotation No. :")
    c.drawCentredString(100, 70,invoice.get())
    c.drawRightString(70, 80, "DATE : ")
    c.drawCentredString(100, 80, date.get())


    c.drawRightString(70, 90, "CUSTOMER NAME :")
    c.drawRightString(100, 90, To.get())
    c.drawRightString(70, 100, "ADDRESS :")
    c.drawCentredString(100, 100, address_line_1.get())

    # This Block Consist of Item Description
    c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
    c.line(15, 120, 185, 120)
    c.drawCentredString(25, 118, "SR No.")
    c.drawCentredString(25, 125, "01.")
    c.drawCentredString(25, 135, "02.")
    c.drawCentredString(25, 145, "03.")
    c.drawCentredString(25, 155, "04.")

    c.drawCentredString(25, 165, "05.")
    c.drawCentredString(25, 175, "06.")
    c.drawCentredString(25, 185, "07.")
    c.drawCentredString(25, 195, "IGST.")
    c.drawCentredString(25, 205,"CGST")

    c.drawCentredString(70, 215, "Total (including 18% GST)")

    c.drawCentredString(60, 118, "Name of Item")
    c.setFont("Times-Bold", 4)

    c.drawCentredString(125, 118, "Unit Price" )
    c.setFont("Times-Bold", 5)

    c.drawCentredString(147, 118, "Quantity")
    c.setFont("Times-Bold", 5)

    c.drawCentredString(175, 118, "Total")
    c.setFont("Times-Bold", 4)

    # Adding item 1 information
    if len(serialNumber1.get()) != 0:
        c.drawCentredString(60, 125, nameOfItem1.get())
        c.drawCentredString(125, 125, quantity1.get())
        c.drawCentredString(147, 125, unitPrice1.get())
        total1 = int(quantity1.get()) * int(unitPrice1.get())
        c.drawCentredString(175, 125, str(total1))
        Total1=total1
        Total=0.18*Total1

    # Adding item 2 information
    if len(serialNumber2.get()) != 0:
        c.drawCentredString(60, 135, nameOfItem2.get())
        c.drawCentredString(125, 135, quantity2.get())
        c.drawCentredString(147, 135, unitPrice2.get())
        total2 = int(quantity2.get()) * int(unitPrice2.get())
        c.drawCentredString(175, 135, str(total2))
        Total1=total1+total2
        Total=Total1+(0.18*Total1)


    # Adding item 3 information
    if len(serialNumber3.get()) != 0:
        c.drawCentredString(60, 145, nameOfItem3.get())
        c.drawCentredString(125, 145, quantity3.get())
        c.drawCentredString(147, 145, unitPrice3.get())
        total3 = int(quantity3.get()) * int(unitPrice3.get())
        c.drawCentredString(175, 145, str(total3))
        Total1=total1+total2+total3
        Total=Total1+(0.18*Total1)


    # Adding item 4 information
    if len(serialNumber4.get()) != 0:
        c.drawCentredString(60, 155, nameOfItem4.get())
        c.drawCentredString(125, 155, quantity4.get())
        c.drawCentredString(147, 155, unitPrice4.get())
        total4 = int(quantity4.get()) * int(unitPrice4.get())
        c.drawCentredString(175, 155, str(total4))
        Total1=total1+total2+total3+total4
        Total=Total1+(0.18*Total1)


    # Adding item5 information
    if len(serialNumber5.get()) != 0:
        c.drawCentredString(60, 165, nameOfItem5.get())
        c.drawCentredString(125, 165, quantity5.get())
        c.drawCentredString(147, 165, unitPrice5.get())
        total5 = int(quantity5.get()) * int(unitPrice5.get())
        c.drawCentredString(175, 165, str(total5))
        Total1=total1+total2+total3+total4+total5
        Total=Total1+(0.18*Total)





    c.drawCentredString(175, 195, str(0.09*Total1)+"/-")
    c.drawCentredString(175, 205, str(0.09*Total1)+"/-")
    c.drawCentredString(175, 215, str(Total))

    # Drawing table for Item Description
    c.line(15, 210, 185, 210)
    c.line(35, 108, 35, 220)
    c.line(115, 108, 115, 220)
    c.line(135, 108, 135, 220)
    c.line(160, 108, 160, 220)

    # Declaration and Signature
    c.line(15, 220, 185, 220)
    c.line(100, 220, 100, 238)
    c.drawString(20, 225, "We declare that above mentioned")
    c.drawString(20, 230, "information is true.")
    c.drawString(20, 235, "(This is system generated invoice)")
    c.drawRightString(180, 235, "Authorised Signatory")

    # End the Page and Start with new
    c.showPage()
    # Saving the PDF
    c.save()

    # saving the file at desired location
    import shutil

L1 = Label(mainWindow, text="To", font=("Calibri 18")).grid(column=0, row=0)
To = Entry(mainWindow, bd=7, font=("Calibri 18"))
To.grid(column=1, row=0)

L2 = Label(mainWindow, text="Address line ", font=("Calibri 18")).grid(column=0, row=2)
address_line_1 = Entry(mainWindow, bd=7, font=("Calibri 18"))
address_line_1.grid(column=1, row=2)



# Adding Item 1
L4 = Label(mainWindow, text="S. No.", font=("Calibri 12"), bg="yellow" ).grid(column=0, row=3)
L5 = Label(mainWindow, text="Name of item", font=("Calibri 12"),bg="yellow" ).grid(column=1, row=3)
L6 = Label(mainWindow, text="Quantity", font=("Calibri 12"),bg="yellow").grid(column=2, row=3)
L7 = Label(mainWindow, text="Unit Price", font=("Calibri 12"),bg="yellow").grid(column=3, row=3)

serialNumber1 = Entry(mainWindow, bd=7, font=("Calibri 12"))
serialNumber1.grid(column=0, row=4)

nameOfItem1 = Entry(mainWindow, bd=7, font=("Calibri 12"))
nameOfItem1.grid(column=1, row=4)

unitPrice1 = Entry(mainWindow, bd=7, font=("Calibri 12"))
unitPrice1.grid(column=2, row=4)

quantity1 = Entry(mainWindow, bd=7, font=("Calibri 12"))
quantity1.grid(column=3, row=4)

# Adding Item 2

serialNumber2 = Entry(mainWindow, bd=7, font=("Calibri 12"))
serialNumber2.grid(column=0, row=5)

nameOfItem2 = Entry(mainWindow, bd=7, font=("Calibri 12"))
nameOfItem2.grid(column=1, row=5)

unitPrice2 = Entry(mainWindow, bd=7, font=("Calibri 12"))
unitPrice2.grid(column=2, row=5)

quantity2 = Entry(mainWindow, bd=7, font=("Calibri 12"))
quantity2.grid(column=3, row=5)
# Adding Item 3

serialNumber3 = Entry(mainWindow, bd=7, font=("Calibri 12"))
serialNumber3.grid(column=0, row=6)

nameOfItem3 = Entry(mainWindow, bd=7, font=("Calibri 12"))
nameOfItem3.grid(column=1, row=6)

unitPrice3 = Entry(mainWindow, bd=7, font=("Calibri 12"))
unitPrice3.grid(column=2, row=6)

quantity3 = Entry(mainWindow, bd=7, font=("Calibri 12"))
quantity3.grid(column=3, row=6)

# Adding Item 4
serialNumber4 = Entry(mainWindow, bd=7, font=("Calibri 12"))
serialNumber4.grid(column=0, row=7)

nameOfItem4 = Entry(mainWindow, bd=7, font=("Calibri 12"))
nameOfItem4.grid(column=1, row=7)

unitPrice4 = Entry(mainWindow, bd=7, font=("Calibri 12"))
unitPrice4.grid(column=2, row=7)

quantity4 = Entry(mainWindow, bd=7, font=("Calibri 12"))
quantity4.grid(column=3, row=7)

# Adding Item 5
serialNumber5 = Entry(mainWindow, bd=7, font=("Calibri 12"))
serialNumber5.grid(column=0, row=8)

nameOfItem5 = Entry(mainWindow, bd=7, font=("Calibri 12"))
nameOfItem5.grid(column=1, row=8)

unitPrice5 = Entry(mainWindow, bd=7, font=("Calibri 12"))
unitPrice5.grid(column=2, row=8)

quantity5 = Entry(mainWindow, bd=8, font=("Calibri 12"))
quantity5.grid(column=3, row=8)

# Giving File name

L20 = Label(mainWindow, text="File name", font=("Calibri 18")).grid(column=0, row=11)
fil = Entry(mainWindow, bd=7, font=("Calibri 18"))
fil.grid(column=1, row=11)

button1 = Button(mainWindow, text="Generate Invoice",font=("Calibri 18"), command=generateInvoice, padx=50, pady=10, bd=5, bg="blue",
                 fg="white").grid(row=12, column=1)

L8 = Label(mainWindow, text="Invoice Number", font=("Calibri 18")).grid(column=0, row=9)
invoice = Entry(mainWindow, bd=7, font=("Calibri 18"))
invoice.grid(column=1, row=9)

L9 = Label(mainWindow, text="Date", font=("Calibri 18")).grid(column=0, row=10)
date = Entry(mainWindow, bd=7, font=("Calibri 18"))
date.grid(column=1, row=10)



mainWindow.mainloop()
