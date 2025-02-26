def get_history(tracker):
    historial = []

    for event in tracker.events:
        if event.get("event") == "user":
            historial.append(f"Usuario: {event.get('text')}")
        elif event.get("event") == "bot":
            historial.append(f"Bot: {event.get('text')}")

    historial_str = "\n".join(historial[-10:])  # Guardar solo los últimos 10 mensajes
    return historial_str