from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fpdf import FPDF
import os

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
    pdf.cell(200, 10, txt=f"Precio: ${data.precio}", ln=True)

    output_path = "cotizacion.pdf"
    pdf.output(output_path)

    return FileResponse(output_path, media_type='application/pdf', filename="cotizacion.pdf")
