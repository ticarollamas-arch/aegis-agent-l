from colorama import init, Fore, Style
init(autoreset=True)

def show_startup_banner():
    print(Fore.CYAN + Style.BRIGHT + '╔══════════════════════════════════╗')
    print(Fore.CYAN + Style.BRIGHT + '║         AEGIS FRAMEWORK          ║')
    print(Fore.CYAN + Style.BRIGHT + '║     Enterprise CLI Platform      ║')
    print(Fore.CYAN + Style.BRIGHT + '╚══════════════════════════════════╝')
    print(Fore.WHITE + 'Version: 1.0.0 | Status: Ready\n')

def banner_3d(target, model):
    print(Fore.MAGENTA + Style.BRIGHT + '   🛡️  AUDITORIA DE SEGURANÇA AI  🛡️')
    print(Fore.GREEN + f'🎯 Target: {target} | 🧠 Model: {model}\n')

def show_agent_3d(num, nome, desc, icone):
    print(Fore.YELLOW + f'╔══ AGENTE #{num:02d} ════════════════════════════════════════════════════╗')
    print(Fore.CYAN + f'║ {icone} {nome} - {desc}')
    print(Fore.YELLOW + '╚════════════════════════════════════════════════════════════════╝')

def progress_bar_3d(current, total, name):
    percent = (current / total) * 100
    filled = int(percent / 100 * 40)
    bar = '█' * filled + '░' * (40 - filled)
    print(Fore.GREEN + f'📊 Progresso: [{bar}] {percent:.1f}%')

def show_result_3d(target, model, elapsed, agents, path):
    print(Fore.GREEN + Style.BRIGHT + '\n🎉 AUDITORIA CONCLUÍDA COM SUCESSO!')
    print(Fore.WHITE + f'📁 Relatório salvo em: {path}')
