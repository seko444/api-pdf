from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fpdf import FPDF
import io

app = FastAPI()

class QuoteRequest(BaseModel):
    nombre: str
    email: str
    producto: str
    precio: float

@app.post("/pdf")
async def generar_pdf(data: QuoteRequest):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cotización", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Nombre: {data.nombre}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {data.email}", ln=True)
    pdf.cell(200, 10, txt=f"Producto: {data.producto}", ln=True)
    pdf.cell(200, 10, txt=f"Precio: €{data.precio}", ln=True)

    # Guardar el PDF en memoria (no en disco)
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=cotizacion.pdf"})
