from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Lista para armazenar os agendamentos
agendamentos = []

# HTML com visual de app (Bootstrap)
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Agendamento</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#0d6efd">
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

if __name__ == '__main__':
    app.run(debug=True)
