def ler_exe_como_binario(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            dados_binarios = arquivo.read()
            return dados_binarios
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None
    except IOError:
        print(f"Erro ao ler o arquivo: {caminho_arquivo}")
        return None

def escrever_hexadecimal_em_arquivo(dados_binarios, caminho_saida):
    representacao_hex = dados_binarios.hex()
    with open(caminho_saida, 'w') as arquivo_saida:
        for i in range(0, len(representacao_hex), 32):
            linha = representacao_hex[i:i+32] + '\n'
            arquivo_saida.write(linha)

def main():
    caminho_arquivo = r'caminho de entrada'
    caminho_saida = r'saída'
    dados_binarios = ler_exe_como_binario(caminho_arquivo)
    if dados_binarios:
        escrever_hexadecimal_em_arquivo(dados_binarios, caminho_saida)
        print(f"Código hexadecimal salvo em: {caminho_saida}")

if __name__ == "__main__":
    main()
