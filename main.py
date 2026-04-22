import os
import re
import subprocess
import glob

def test_t1_uv():
    """T1 uv (4 pts): Verifica uso de uv buscando pyproject.toml o uv.lock"""
    if os.path.exists("uv.lock") or os.path.exists("pyproject.toml"):
        return 4, "[✓] T1 (4/4 pts): Entorno uv detectado (pyproject.toml / uv.lock existe)."
    return 0, "[X] T1 (0/4 pts): No se encontró evidencia de uv (falta uv.lock o pyproject.toml)."

def test_t2_ruta():
    """T2 index.qmd (8 pts): Existe dashboard/index.qmd"""
    if os.path.exists(os.path.join("dashboard", "index.qmd")):
        return 8, "[✓] T2 (8/8 pts): dashboard/index.qmd encontrado en la ruta correcta."
    return 0, "[X] T2 (0/8 pts): No se encontró dashboard/index.qmd."

def test_t3_render():
    """T3 Render (4 pts): Renderiza sin errores usando uv run"""
    print("      -> Ejecutando render (esto puede tardar unos segundos)...")
    try:
        resultado = subprocess.run(
            ["uv", "run", "quarto", "render", "dashboard/index.qmd"],
            capture_output=True, text=True
        )
        if resultado.returncode == 0:
            return 4, "[✓] T3 (4/4 pts): El tablero se renderizó sin errores."
        else:
            return 0, f"[X] T3 (0/4 pts): Error en el render.\nDetalle: {resultado.stderr[:200]}..."
    except FileNotFoundError:
        return 0, "[X] T3 (0/4 pts): No se pudo ejecutar 'uv' o 'quarto'. ¿Están instalados?"

def test_t4_salida():
    """T4 Salida en docs/ (4 pts): Existe docs/index.html"""
    if os.path.exists(os.path.join("docs", "index.html")):
        return 4, "[✓] T4 (4/4 pts): docs/index.html generado exitosamente."
    return 0, "[X] T4 (0/4 pts): No se encontró docs/index.html tras el render."

def test_t5_formato_dashboard():
    """T5 Formato dashboard (8 pts): El HTML tiene clases de Quarto Dashboard"""
    ruta_html = os.path.join("docs", "index.html")
    if not os.path.exists(ruta_html):
        return 0, "[X] T5 (0/8 pts): No se puede evaluar, falta docs/index.html."
    
    with open(ruta_html, 'r', encoding='utf-8') as f:
        contenido = f.read()
        # Quarto inyecta clases específicas o variables en los dashboards
        if "quarto-dashboard" in contenido or "layout: dashboard" in contenido.lower():
            return 8, "[✓] T5 (8/8 pts): El HTML confirma ser un tablero de Quarto."
    return 0, "[X] T5 (0/8 pts): El HTML no parece tener el formato de un Quarto dashboard."

def test_t6_md_only():
    """T6 md-only (8 pts): No hay HTML ni scripts en index.qmd"""
    ruta_qmd = os.path.join("dashboard", "index.qmd")
    if not os.path.exists(ruta_qmd):
        return 0, "[X] T6 (0/8 pts): No se puede evaluar, falta dashboard/index.qmd."
    
    with open(ruta_qmd, 'r', encoding='utf-8') as f:
        contenido = f.read()
        
    patron = re.compile(r'<\/?(?:div|span|script|style|iframe|html|body)[^>]*>', re.IGNORECASE)
    etiquetas = patron.findall(contenido)
    
    if etiquetas:
        return 0, f"[X] T6 (0/8 pts): Prosa sucia. Se encontró HTML: {set(etiquetas)}"
    return 8, "[✓] T6 (8/8 pts): dashboard/index.qmd es puro Markdown/Quarto."

def test_t7_licencia():
    """T7 Licencia CC (4 pts): Existe LICENSE o COPYING indicando Creative Commons"""
    archivos_licencia = glob.glob("LICENSE*") + glob.glob("COPYING*")
    
    if not archivos_licencia:
        return 0, "[X] T7 (0/4 pts): No se encontró archivo LICENSE o COPYING en la raíz."
        
    # Verificar que el contenido mencione Creative Commons o CC
    for archivo in archivos_licencia:
        with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read().lower()
            if "creative commons" in contenido or "cc by" in contenido or "cc0" in contenido:
                return 4, f"[✓] T7 (4/4 pts): Licencia Creative Commons detectada en '{archivo}'."
                
    return 0, "[X] T7 (0/4 pts): Archivo de licencia encontrado, pero no parece ser Creative Commons."

def main():
    print("="*60)
    print("SIMULADOR DE EVALUACIÓN AUTOMÁTICA - HACKODS UNAM 2026")
    print("="*60 + "\n")
    
    pruebas = [
        test_t1_uv,
        test_t2_ruta,
        test_t3_render,
        test_t4_salida,
        test_t5_formato_dashboard,
        test_t6_md_only,
        test_t7_licencia
    ]
    
    puntaje_total = 0
    for prueba in pruebas:
        puntos, mensaje = prueba()
        print(mensaje)
        puntaje_total += puntos
        
    print("\n" + "="*60)
    print(f"PUNTAJE FINAL OBTENIDO: {puntaje_total} / 40 PUNTOS")
    print("="*60)

if __name__ == "__main__":
    main()
    