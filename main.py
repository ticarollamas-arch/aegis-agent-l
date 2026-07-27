#!/usr/bin/env python3
import os
import sys
import argparse
from cli.banner import show_startup_banner, banner_3d
from cli.menu import interactive_menu
from core.engine import run_audit, check_ollama_health
from core.logger import log_info, log_error, log_success

def main():
    parser = argparse.ArgumentParser(description='Aegis-Audit: Enterprise AI Security Auditor')
    parser.add_argument('--target', '-t', help='URL alvo para auditoria')
    parser.add_argument('--model', '-m', help='Modelo Ollama específico')
    parser.add_argument('--interactive', '-i', action='store_true', help='Iniciar modo interativo')
    args = parser.parse_args()

    show_startup_banner()

    if args.interactive or not args.target:
        interactive_menu()
        sys.exit(0)

    log_info(f'Iniciando diagnóstico de dependências...')
    model = check_ollama_health(args.model)
    if not model:
        log_error('Falha ao conectar com Ollama. Verifique se o serviço está rodando.')
        sys.exit(1)

    log_success(f'Ollama operacional. Modelo selecionado: {model}')
    os.system('clear' if os.name == 'posix' else 'cls')
    banner_3d(args.target, model)
    
    run_audit(args.target, model)

if __name__ == '__main__':
    main()
