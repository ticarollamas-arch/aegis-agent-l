import time
import json
import os
from datetime import datetime
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError
from crewai import Agent, Task, Crew, Process, LLM
from core.logger import log_info, log_error, log_success, log_warning
from cli.banner import show_agent_3d, progress_bar_3d, show_result_3d

NOMES_AGENTES = [
    ('Reconhecimento Web', 'Mapeia tecnologias e estrutura', '🧠'),
    ('Headers de Segurança', 'Analisa headers HTTP', '🛡️'),
    ('Cookies', 'Verifica segurança de cookies', '🔒'),
    ('SSL/TLS', 'Analisa certificados SSL', '🔑'),
    ('CORS', 'Verifica configuração CORS', '🌍')
    # Reduzido para brevidade no blueprint, expansível para 30
]

def check_ollama_health(preferred_model: str = None) -> str:
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=5.0)
        response.raise_for_status()
        data = response.json()
        models = [m.get('name') for m in data.get('models', [])]
        if not models:
            log_error('Nenhum modelo encontrado no Ollama.')
            return None
        if preferred_model and preferred_model in models:
            return preferred_model
        return models[0]
    except Timeout:
        log_error('Timeout: A conexão com o Ollama excedeu o tempo limite (5.0s).')
    except ConnectionError:
        log_error('ConnectionError: Falha ao conectar no Ollama. O serviço está rodando?')
    except HTTPError as http_err:
        log_error(f'HTTPError: Erro na API do Ollama: {http_err}')
    except Exception as e:
        log_error(f'Erro inesperado ao contatar Ollama: {str(e)}')
    return None

def run_audit(target: str, model: str):
    log_info('Configurando LLM...')
    llm = LLM(model=f'ollama/{model}', base_url='http://localhost:11434', temperature=0.7)
    
    agents = []
    tasks = []
    
    for i, (nome, desc, icone) in enumerate(NOMES_AGENTES, 1):
        agent = Agent(
            role=f'Especialista em {nome}',
            goal=f'Analisar {desc} do target {target}',
            backstory=f'Especialista sênior em {nome}',
            llm=llm,
            verbose=False,
            allow_delegation=False
        )
        agents.append(agent)
        task = Task(
            description=f'Análise de {nome} para {target}',
            expected_output=f'Relatório de {nome}',
            agent=agent
        )
        tasks.append(task)

    start_time = time.time()
    for i, agent in enumerate(agents):
        nome, desc, icone = NOMES_AGENTES[i]
        show_agent_3d(i+1, nome, desc, icone)
        tasks[i].execute_sync(agent=agent, context=None, tools=None)
        progress_bar_3d(i+1, len(agents), nome)

    elapsed = time.time() - start_time
    os.makedirs('reports', exist_ok=True)
    report_path = f'reports/audit_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    
    report_data = {'target': target, 'model': model, 'time': elapsed, 'status': 'Concluído'}
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2)
    
    show_result_3d(target, model, elapsed, len(agents), report_path)
