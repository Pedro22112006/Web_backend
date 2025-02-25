from flask import Flask, request

app = Flask(__name__)

tarefas =  [
    {
        "id" : 1,
        "titulo" : "Lavar a louca",
        "status": "Em andamento",
        "descricao": "Lavar todos os pratos sujos",
        "horas_paralavarlouca": "2 horas",
        "qtde_loucas": "20"
    },
    {
        "id" : 2,
        "titulo": "Estudar Flask",
        "status": "Nao iniciado",
        "descricao": "Ler documentação e praticar exemplos",
        "horas_paralavarlouca": "3 horas",
        "qtde_loucas": "15"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def create_(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa
    return 'tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['horas_paralavarlouca'] = task_body.get('horas_paralavarlouca')
    task_search['qtde_loucas'] = task_body.get('qtde_loucas')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa.get('id') != task_id]
    return {"message": "Tarefa removida com sucesso"}, 200



if __name__ == '__main__':
    app.run(debug=True)