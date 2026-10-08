def run_custom_tool(query: str) -> str:
    if not query.strip():
        raise ValueError("La consulta no puede estar vacía")
    return f"Resultado simulado para: {query}"