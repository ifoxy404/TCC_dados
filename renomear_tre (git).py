import os

# Defina o diretório onde estão os arquivos
diretorio = "C:\\Users\\IQ-TREE-trial"

# Verifique se o diretório existe
if not os.path.exists(diretorio):
    print(f"O diretório {diretorio} não existe.")
else:
    # Iterar sobre todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        print(f"Encontrado arquivo: {nome_arquivo}")  # Mensagem de depuração
        # Verificar se o arquivo termina com .treefile
        if nome_arquivo.endswith(".treefile"):
            # Criar o novo nome do arquivo
            novo_nome_arquivo = nome_arquivo.replace(".treefile", ".tre")
            # Caminho completo do arquivo antigo e novo
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            caminho_novo = os.path.join(diretorio, novo_nome_arquivo)
            # Renomear o arquivo
            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {caminho_antigo} -> {caminho_novo}')