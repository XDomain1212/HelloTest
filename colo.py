from colorama import init,Fore
init(autoreset=True)
name =input('Please input your name:')
print(Fore.BLUE+"Hello,"+Fore.RED+name+'  '+Fore.RESET+'Welcome Home!')
