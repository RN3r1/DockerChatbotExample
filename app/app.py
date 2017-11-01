from flask import Flask, request
from fbmq import fbmq

PAGE_ACCESS_TOKEN = "TU TOKEN AQUI"
VERIFY_TOKEN = "ChatbotWithDocker"

app = Flask(__name__)

page = fbmq.Page(PAGE_ACCESS_TOKEN)

@app.route('/')
def main_route():
    return 'Servidor corriendo exitosamente :)'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        page.handle_webhook(request.get_data(as_text=True))
        return 'OK'
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Error con el Token de Verificación'

@page.handle_message
def message_handler(event):
    sender_id = event.sender_id # Se obtiene el id de quien envia el mensaje
    if event.is_text_message or event.is_quick_reply: # Se verifica si el mensaje es texto
        page.send(sender_id, "Genial! Tu mensaje fue -> {}".format(event.message_text))
    elif event.is_attachment_message: # Se verifica si el mensaje no es texto
        page.send(sender_id, "Lo siento, aún no sé que hacer con archivos :(")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
