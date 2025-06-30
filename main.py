from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
from fpdf import FPDF
import io

app = FastAPI()

@app.post("/pdf")
async def generar_pdf(
    cliente: str = Form(...),
    producto: str = Form(...),
    precio: float = Form(...),
    descripcion: str = Form(...),
    correo: str = Form(...)
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cotización", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Correo: {correo}", ln=True)
    pdf.cell(200, 10, txt=f"Producto: {producto}", ln=True)
    pdf.cell(200, 10, txt=f"Precio: €{precio}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Descripción:\n{descripcion}")

    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=cotizacion.pdf"
    })
