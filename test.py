import requests

# Ajusta la URL base si tu servidor corre en otro puerto o dominio
BASE_URL = "http://127.0.0.1:8000"

def test_health():
    """Prueba el endpoint /health para verificar el estado."""
    resp = requests.get(f"{BASE_URL}/health")
    assert resp.status_code == 200, f"Estado inesperado: {resp.status_code}"
    data = resp.json()
    assert data == {"status": "OK"}, f"Respuesta inesperada: {data}"
    print("✓ /health funciona correctamente.")

def test_chat():
    """Prueba el endpoint /chat enviando una pregunta de ejemplo."""
    payload = {"question": "Recetas con bajo índice glucémico"}
    resp = requests.post(f"{BASE_URL}/chat", json=payload)
    assert resp.status_code == 200, f"Estado inesperado: {resp.status_code}"
    data = resp.json()
    assert "recipes" in data, "No se encontró la clave 'recipes' en la respuesta."
    assert isinstance(data["recipes"], list), "Se esperaba que 'recipes' fuera una lista."
    print("✓ /chat funciona correctamente y devuelve 'recipes'.")

if __name__ == "__main__":
    # Ejecuta las pruebas de forma secuencial
    print("Iniciando pruebas...")
    test_health()
    test_chat()
    print("Todas las pruebas han finalizado con éxito.")
