import time
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_thread():
        """
        Crea un nuevo thread en OpenAI y devuelve su ID.
        """
        thread = client.beta.threads.create()
        return thread.id

def send_message(assistant_id, thread_id, user_message):
        """
        Envía un mensaje al thread existente en OpenAI y obtiene la respuesta del asistente.
        """
        # Agregar mensaje del usuario al thread
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_message
        )
        # Ejecutar el asistente para generar respuesta
        try:
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread_id,
                assistant_id=assistant_id
            )
        except Exception as e:
            print('Error creando la respuesta: ', e)

        # Esperar a que el run se complete
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            time.sleep(1)  # Espera 1 segundo antes de volver a comprobar
        # Obtener los mensajes generados
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        # Devolver el último mensaje del asistente
        if messages and messages.data:
            last_message = messages.data[0]  # OpenAI devuelve los mensajes en orden inverso (último primero)
            if last_message.role == "assistant":
                return last_message.content

        return "Lo siento, hubo un problema al generar la respuesta."