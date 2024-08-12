import os
import shutil

# Defina o diretório onde estão os arquivos
diretorio = "C:\\Users\\IQ-TREE-trial"

# Verifique se o diretório existe
if not os.path.exists(diretorio):
    print(f"O diretório {diretorio} não existe.")
else:
    # Iterar sobre todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        print(f"Encontrado arquivo: {nome_arquivo}")  # Mensagem de depuração
        # Verificar se o arquivo é um arquivo de alinhamento ou relacionado a um gene
        if "_aligment." in nome_arquivo:
            # Extrair o nome do gene
            nome_gene = nome_arquivo.split("_aligment.")[0]
            # Criar o diretório para o gene, se não existir
            caminho_diretorio_gene = os.path.join(diretorio, nome_gene)
            if not os.path.exists(caminho_diretorio_gene):
                os.makedirs(caminho_diretorio_gene)
            # Caminho completo do arquivo antigo e novo
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            caminho_novo = os.path.join(caminho_diretorio_gene, nome_arquivo)
            # Mover o arquivo para o novo diretório
            shutil.move(caminho_antigo, caminho_novo)
            print(f'Movido: {caminho_antigo} -> {caminho_novo}')