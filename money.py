
 
import csv
from datetime import datetime

class Transacao:
    """
    Classe para representar uma transação financeira.
    """
    def __init__(self, data, valor, tipo, categoria, descricao):
        """
        Inicializa uma nova transação com os dados fornecidos.
        """
        self.data = data
        self.valor = valor
        self.tipo = tipo  # 'despesa' ou 'receita'
        self.categoria = categoria
        self.descricao = descricao

class GerenciadorFinanceiro:
    """
    Classe para gerenciar transações financeiras.
    """
    def __init__(self):
        """
        Inicializa o gerenciador com uma lista vazia de transações.
        """
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        """
        Adiciona uma nova transação à lista de transações.
        """
        self.transacoes.append(transacao)

    def verificar_saldo(self):
        """
        Calcula o saldo total com base nas transações registradas.
        """
        saldo = 0
        for transacao in self.transacoes:
            if transacao.tipo == 'receita':
                saldo += transacao.valor
            elif transacao.tipo == 'despesa':
                saldo -= transacao.valor
        return saldo

    def relatorio_gastos_por_categoria(self):
        """
        Gera um relatório de gastos por categoria.
        """
        categorias = self.categorizar_transacoes()
        print("### Relatório de Gastos por Categoria ###")
        for categoria, total_gasto in categorias.items():
            print(f'{categoria.capitalize()}: R${total_gasto:.2f}')

    def categorizar_transacoes(self):
        """
        Categoriza as transações por tipo de despesa.
        """
        categorias = {}
        for transacao in self.transacoes:
            if transacao.tipo == 'despesa':
                if transacao.categoria not in categorias:
                    categorias[transacao.categoria] = 0
                categorias[transacao.categoria] += transacao.valor
        return categorias

    def consultar_transacoes_por_data(self, data):
        """
        Consulta as transações realizadas em uma data específica.
        """
        transacoes_data = [transacao for transacao in self.transacoes if transacao.data == data]
        return transacoes_data

    def estatisticas_financeiras(self):
        """
        Calcula as estatísticas financeiras, como média de despesas e receitas.
        """
        despesas = [transacao.valor for transacao in self.transacoes if transacao.tipo == 'despesa']
        receitas = [transacao.valor for transacao in self.transacoes if transacao.tipo == 'receita']

        media_despesas = sum(despesas) / len(despesas) if despesas else 0
        media_receitas = sum(receitas) / len(receitas) if receitas else 0

        return media_despesas, media_receitas

    def salvar_transacoes(self, nome_arquivo):
        """
        Salva as transações em um arquivo CSV.
        """
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Data', 'Valor', 'Tipo', 'Categoria', 'Descrição'])
            for transacao in self.transacoes:
                writer.writerow([transacao.data, transacao.valor, transacao.tipo, transacao.categoria, transacao.descricao])

    def carregar_transacoes(self, nome_arquivo):
        """
        Carrega as transações de um arquivo CSV.
        """
        try:
            with open(nome_arquivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data = row['Data']
                    valor = float(row['Valor'])
                    tipo = row['Tipo']
                    categoria = row['Categoria']
                    descricao = row['Descrição']
                    transacao = Transacao(data, valor, tipo, categoria, descricao)
                    self.adicionar_transacao(transacao)
            print("Transações carregadas com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando um novo.")

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n### Menu ###")
    print("1. Adicionar transação")
    print("2. Verificar saldo")
    print("3. Relatório de gastos por categoria")
    print("4. Consultar transações por data")
    print("5. Estatísticas financeiras")
    print("6. Salvar transações")
    print("7. Carregar transações")
    print("0. Sair")

def main():
    """
    Função principal para executar o sistema de gerenciamento financeiro.
    """
    gerenciador = GerenciadorFinanceiro()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            data = input("Digite a data (YYYY-MM-DD): ")
            valor = float(input("Digite o valor: "))
            tipo = input("Digite o tipo (receita ou despesa): ")
            categoria = input("Digite a categoria: ")
            descricao = input("Digite uma descrição: ")
            transacao = Transacao(data, valor, tipo, categoria, descricao)
            gerenciador.adicionar_transacao(transacao)
            print("Transação adicionada com sucesso!")

        elif opcao == '2':
            saldo = gerenciador.verificar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")

        elif opcao == '3':
            gerenciador.relatorio_gastos_por_categoria()

        elif opcao == '4':
            data = input("Digite a data (YYYY-MM-DD): ")
            transacoes_data = gerenciador.consultar_transacoes_por_data(data)
            if transacoes_data:
                print(f"Transações em {data}:")
                for transacao in transacoes_data:
                    print(f"{transacao.data}: {transacao.valor} ({transacao.categoria}) - {transacao.descricao}")
            else:
                print("Nenhuma transação encontrada para esta data.")

        elif opcao == '5':
            media_despesas, media_receitas = gerenciador.estatisticas_financeiras()
            print("Estatísticas financeiras:")
            print(f"Média de despesas por mês: R${media_despesas:.2f}")
            print(f"Média de receitas por mês: R${media_receitas:.2f}")

        elif opcao == '6':
            gerenciador.salvar_transacoes('transacoes.csv')
            print("Transações salvas com sucesso!")

        elif opcao == '7':
            gerenciador.carregar_transacoes('transacoes.csv')

        elif opcao == '0':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


