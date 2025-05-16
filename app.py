from flask import Flask, render_template_string, request, redirect
import os

app = Flask(__name__)

# Lista em memória para armazenar agendamentos
agendamentos = []

# HTML com Bootstrap e PWA básico
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Agendamento</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#0d6efd">
    <link rel="manifest" href="/static/manifest.json">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container mt-5">
    <h2 class="mb-4 text-center">📅 Agendamento de Corte</h2>

    <form method="post" class="card p-3 shadow">
        <div class="mb-3">
            <label class="form-label">Nome:</label>
            <input type="text" name="nome" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Data:</label>
            <input type="date" name="data" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Hora:</label>
            <input type="time" name="hora" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Serviço:</label>
            <input type="text" name="servico" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-primary w-100">Agendar</button>
    </form>

    <hr class="my-4">

    <h4 class="text-center">📋 Agendamentos Feitos</h4>
    <ul class="list-group">
        {% for a in agendamentos %}
            <li class="list-group-item">
                <strong>{{ a['nome'] }}</strong> - {{ a['data'] }} às {{ a['hora'] }} ({{ a['servico'] }})
            </li>
        {% else %}
            <li class="list-group-item text-muted">Nenhum agendamento ainda.</li>
        {% endfor %}
    </ul>
</div>

<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/service-worker.js')
      .then(function(reg) {
        console.log('Service Worker registrado');
      })
      .catch(function(err) {
        console.error('Erro ao registrar Service Worker:', err);
      });
  }
</script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        agendamentos.append({
            'nome': request.form['nome'],
            'data': request.form['data'],
            'hora': request.form['hora'],
            'servico': request.form['servico']
        })
        return redirect('/')
    return render_template_string(html, agendamentos=agendamentos)

# Configuração final para Render: porta e host
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
