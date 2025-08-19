from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Flask + HTML</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: system-ui, Arial; margin: 0; background: #0f172a; color: #e5e7eb; }
    header { padding: 14px 18px; background: #111827; border-bottom: 1px solid #1f2937; }
    main { max-width: 800px; margin: 0 auto; padding: 18px; }
    h1 { margin: 0 0 8px; font-size: 22px; }
    .card { background: #111827; border: 1px solid #1f2937; border-radius: 14px; padding: 16px; }
    input, button, textarea { width: 100%; padding: 10px; border-radius: 10px; border: 1px solid #334155; background: #0b1220; color: #e5e7eb; }
    button { cursor: pointer; margin-top: 8px; border: none; background: #60a5fa; color: #0b1220; font-weight: 700; }
    .note { padding: 10px; border: 1px solid #334155; border-radius: 10px; margin-top: 10px; }
    .muted { color: #94a3b8; font-size: 14px; }
  </style>
</head>
<body>
  <header><h1> Mini Proyecto Flask + HTML</h1></header>
  <main>
    <div class="card">
      <p class="muted">Ejemplo simple: envía un mensaje y lo mostramos abajo.</p>
      <form method="post" action="/">
        <label>Tu mensaje</label>
        <input name="msg" placeholder="Escribe algo..." required>
        <button type="submit">Enviar</button>
      </form>
      {% if mensaje %}
        <div class="note">
          <strong>Resultado:</strong>
          <p>{{ mensaje }}</p>
        </div>
      {% endif %}
    </div>
  </main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    mensaje = None
    if request.method == "POST":
        mensaje = request.form.get("msg", "").strip()
    return render_template_string(HTML, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
