from fastapi import FastAPI, Form
from fastapi.responses import Response
from fpdf import FPDF

app = FastAPI()

@app.post("/pdf")
def generar_pdf(
    nombre: str = Form(...),
    dni: str = Form(...),
    base_cotizacion: str = Form(...),
    grupo_cotizacion: str = Form(...),
    fecha_inicio: str = Form(...),
    fecha_fin: str = Form(...),
    dias_cotizados: str = Form(...)
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Construir el contenido del PDF
    contenido = (
        f"Nombre: {nombre}\n"
        f"DNI: {dni}\n"
        f"Base de cotización: {base_cotizacion}\n"
        f"Grupo de cotización: {grupo_cotizacion}\n"
        f"Fecha de inicio: {fecha_inicio}\n"
        f"Fecha de fin: {fecha_fin}\n"
        f"Días cotizados: {dias_cotizados}"
    )

    pdf.multi_cell(0, 10, contenido)

    # Generar PDF como bytes (evita errores de codificación)
    pdf_bytes = pdf.output(dest='S').encode('latin-1', 'replace')

    # Devolver el PDF como respuesta HTTP
    return Response(content=pdf_bytes, media_type="application/pdf")

