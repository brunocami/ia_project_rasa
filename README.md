# Pasos para levantar el chatbot con un bot de telegram
1. Crear un bot de telegram 
    - Open Telegram and search for "BotFather"
    - Click on the BotFather account and select "Start"
    - Type /newbot and send it
    - Choose a name and username for your bot
    - BotFather will send you a message with a link to your bot and an API token
    - Save your token and username

2. Cuando tengas el token vas a tener que setear un webhook donde telegram va a reenviar el mensaje (api de django), usa ngrok para exponer localhost:8000 (descargar ngrok y ejecutar en la terminal **ngrok http 8000**). 
    - Envia desde postman una solicitud POST a este endpoint:
        - https://api.telegram.org/botTokenDelBot/setWebhook body: type=x-www-form-urlencoded, key=url:dominio que te devuelve ngrok

3. crear en el proyecto de django un .env con estas keys:
    # Django Config
    DJANGO_SECRET_KEY='django-insecure-fw-i0j5dfn_1u0jy%$u)607e%@f&ao3_-g@p1*%ri4gbp101m4'

    # Telegram
    TELEGRAM_ACCESS_TOKEN=...
    TELEGRAM_URL=f"https://api.telegram.org/botTokenDelBot"

4. Levantar el servidor de desarrollo de Django

5. Conseguir una api key de gemini

6. Crear en el proyecto de rasa un .env con estas keys:
    # GEMINI
    GEMINI_API_KEY=AIzaSyB7iG1qAtV5_8TY2oBJCNlIoPDVQ-OBLvg

7. Levantar modelo de rasa:
    - Descargar todas las dependencias usando python 3.10 para no tener problema: py -3.10 -m venv venv
    
    - **Start model** rasa run --enable-api --cors "*" --debug

8. Levantar servidor de actions
    - **Start actions server** rasa run actions

# COMANDOS UTILES
- **Train new model** rasa train
- **Start model** rasa run --enable-api --cors "*" --debug
- **Start actions server** rasa run actions