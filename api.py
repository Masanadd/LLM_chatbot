from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import cohere
import os
from dotenv import load_dotenv

# Importa la función para conectarte a la BD
from db import get_connection

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise RuntimeError("COHERE_API_KEY environment variable is not set.")

cohere_client = cohere.Client(COHERE_API_KEY)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    """
    Devuelve el template 'index.html' ubicado en /templates
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "OK"}

def parse_recipes(raw_text: ChatRequest):
    """
    Función que parsea el texto devuelto por Cohere.
    Reemplaza '**Recipes**:' por '**Receta**:' para uniformizar
    y luego divide en bloques por '**Receta**:'.
    """
    # Normaliza el texto para que use siempre '**Receta**:'
    raw_text = raw_text.replace("**Recipes**:", "**Receta**:")

    # Ahora partimos en bloques
    blocks = raw_text.split("**Receta**:")
    recipes = []
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        
        lines = block.split("\n", 1)
        recipe_name = lines[0].strip()
        details = lines[1].strip() if len(lines) > 1 else ""
        
        recipes.append({
            "name": recipe_name,
            "details": details
        })
    
    return recipes



@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Prompt especializado en nutrición y gastronomía
        system_prompt = """La receta solicitada es: [NOMBRE DEL PLATO].

Actúa como un chef profesional y experto en nutrición. Responde completamente en español, sin mezclar con inglés. Incluye:

1. **Nombre de la receta** – Título claro.
2. **Ingredientes** – Lista con cantidades específicas.
3. **Preparación** – Explica cada paso en detalle, con tiempos de cocción aproximados y consejos de preparación.
4. **Sustituciones** – Sugiere ingredientes alternativos.
5. **Información calórica** – Calorías aproximadas por porción.
6. **Índice glucémico** – Indica si es bajo y ofrece formas de reducir la carga glucémica si procede.
7. **Consejos nutricionales** – Observaciones finales para una dieta saludable.

Usa un estilo claro y directo, sin exceder 500-800 tokens. 


"""

        full_prompt = f"{system_prompt}\n\nConsulta del usuario: {request.question}\n\nRecomendaciones:"

        # Llamada a Cohere
        response = cohere_client.generate(
            model="command-r-plus",
            prompt=full_prompt,
            max_tokens=800,
            temperature=0.5,
            #stop_sequences=["\n\n"]
        )

        raw_answer = response.generations[0].text.strip()
        print("Respuesta de Cohere:", raw_answer)  # Para depurar

        # Parsear el texto para obtener una lista de "recipes"
        recipes = parse_recipes(raw_answer)

        # Guardar en BD (almacenamos la respuesta sin parsear, si lo deseas)
        conn = get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO interactions 
                 (question, answer) 
                 VALUES (%s, %s)"""
        val = (request.question, raw_answer)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

        # Devuelve la respuesta en JSON con clave "recipes"
        return {"recipes": recipes}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
