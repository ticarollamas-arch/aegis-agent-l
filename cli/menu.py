import sys
from core.logger import log_info, log_warning
from core.engine import check_ollama_health

def interactive_menu():
    while True:
        print('\n--- MENU AEGIS ---')
        print('[1] Iniciar Auditoria AI')
        print('[2] Doctor (Health Check)')
        print('[3] Sair')
        choice = input('Selecione: ')
        
        if choice == '1':
            log_warning('Execute via linha de comando: python main.py -t <URL>')
        elif choice == '2':
            log_info('Verificando dependências...')
            if check_ollama_health():
                log_info('Sistema Saudável.')
        elif choice == '3':
            sys.exit(0)
