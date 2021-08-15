import win32api, win32con, sys, os
print(len(sys.argv))

if not os.path.exists('config.hide'):
    open('config.hide', 'w').close()

if(len(sys.argv) < 2):
    with open('config.hide', 'r') as f:
        nome = f.readline()
    try:
        win32api.WinExec(nome, win32con.SW_HIDE)
    except:
        print(f'- não foi encontrado nenhum arquivo chamado {nome}')
else:
    try:
        win32api.WinExec(sys.argv[1], win32con.SW_HIDE)
    except:
        nome = sys.argv[1]
        print(f'- não foi encontrado nenhum arquivo chamado {nome}')

