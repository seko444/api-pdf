from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fpdf import FPDF
import io

app = FastAPI()

class QuoteRequest(BaseModel):
    cliente: str
    producto: str
    precio: float
    descripcion: str
    correo: str

@app.post("/pdf")
async def generar_pdf(data: QuoteRequest):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.set_text_color(40, 40, 40)

    pdf.cell(200, 10, txt="I LOVE COTIZAR - Cotización", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Cliente: {data.cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Correo: {data.correo}", ln=True)
    pdf.cell(200, 10, txt=f"Producto: {data.producto}", ln=True)
    pdf.cell(200, 10, txt=f"Precio: €{data.precio}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Descripción:\n{data.descripcion}")

    # Guardar en memoria
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=cotizacion.pdf"
    })

