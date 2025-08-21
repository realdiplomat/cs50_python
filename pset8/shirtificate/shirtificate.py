from fpdf import FPDF

# Get name
name = input("Name: ")

# Create object
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=0)

# Header
pdf.set_font("helvetica", "B", 35)
pdf.cell(w=0, h=50, text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

# Add image
pdf.image("shirtificate.png", x="C", y=75, w=180)

# Add text on image
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", size=30)
pdf.cell(w=0, h=170, text=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
