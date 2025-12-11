from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch

def create_schedule_pdf():
    # Schedule data
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    shifts = [
        ['John 10am-8pm', 'Silvia 8pm-4am'],
        ['John 10am-5pm', 'Fares 5pm-4am'],
        ['Abdallah 10am-5pm', 'Fares 5pm-4am'],
        ['Abdallah 10am-5pm', 'Silvia 5pm-4am'],
        ['Abdallah 10am-5pm', 'Fares 5pm-4am'],
        ['Silvia 10am-5pm', 'Fares 5pm-4am'],
        ['Silvia 10am-5pm', 'Fares 5pm-4am']
    ]

    # Create the PDF document
    doc = SimpleDocTemplate("schedule.pdf", pagesize=letter)
    elements = []

    # Create the table data
    data = [['Day', 'Morning Shift', 'Evening Shift']]
    for day, shift in zip(days, shifts):
        data.append([day, shift[0], shift[1]])

    # Create the table
    table = Table(data, colWidths=[1.5*inch, 2*inch, 2*inch])
    
    # Add table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    table.setStyle(style)
    elements.append(table)
    
    # Build the PDF
    doc.build(elements)

if __name__ == '__main__':
    create_schedule_pdf() 