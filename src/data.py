from typing import List, Dict

class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            'id': 1,
            'nome': 'iPhone 14',
            'descricao': 'Apple iPhone 14 128GB Meia-Noite 5G Tela 6,1" Câm. Traseira 12+12MP Frontal 12MP',
            'preco': 4699.00,
        },

        {
            'id': 2,
            'nome': 'ThinkPad L14',
            'descricao': 'Notebook ThinkPad L14 (14” Intel)',
            'preco': 3328.00,
        },

        {
            'id': 3,
            'nome': 'iPad 10.9',
            'descricao': 'Apple iPad 10.9" 10ª Geração, Wi-Fi, 256GB, Prateado',
            'preco': 4699.00,
        }
    ]

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto['id'] == id:
                return produto
        return {'Status': 404, 'Mensagem': 'Produto não encontrado'}
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto