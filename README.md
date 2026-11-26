# 🍽️ Sabor Express (Orientação a Objetos)

Projeto de estudos em Python desenvolvido durante o curso de **Orientação a Objetos em Python** da Alura. O Sabor Express é um app de restaurantes executado no terminal, onde é possível cadastrar restaurantes, listá-los, ativá-los/desativá-los e registrar avaliações.

## 📌 Sobre o projeto

Esta é a evolução do projeto Sabor Express original, que usava funções e listas de dicionários. Nesta versão, o código foi reorganizado com **programação orientada a objetos**: restaurantes e avaliações passam a ser classes, cada uma com seus atributos e comportamentos.

## 🛠️ Tecnologias

- Python 3
- Git e GitHub

## 📂 Estrutura

```
oo-sabor-express/
├── app.py                  # Ponto de entrada da aplicação
└── modelos/
    ├── restaurante.py      # Classe Restaurante
    └── avaliacao.py        # Classe Avaliacao
```

## 🧠 O que aprendi

- **Classes e objetos:** modelar um restaurante e uma avaliação como classes.
- **Método construtor (`__init__`) e `self`:** inicializar os atributos de cada instância.
- **Atributos privados (`_nome`, `_ativo`):** convenção com `_` para indicar que o atributo não deve ser alterado diretamente.
- **Método `__str__`:** representação em texto do objeto, útil para visualizar os dados no terminal.
- **Atributos de classe:** a lista `restaurantes` compartilhada por todas as instâncias.
- **Métodos de classe (`@classmethod`):** `listar_restaurantes` acessa a lista da classe, sem depender de uma instância.
- **Propriedades (`@property`):** acesso controlado a atributos, como o status `ativo`.
- **Tratamento de strings:** `title()`, `upper()` e `ljust()` para padronizar e formatar a saída em tabela.
- **Docstrings e comentários:** documentação do código.
- **Módulos e imports:** separar as classes em arquivos dentro de `modelos/`.
- **Git e GitHub:** versionamento do projeto, commits, merge de históricos e push para o repositório remoto.

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/davi-lemes/sabor_express.git

# Entre na pasta do projeto
cd sabor_express

# Execute a aplicação
python app.py
```

## 🚧 Próximos passos

- [ ] Finalizar o sistema de avaliações dos restaurantes
- [ ] Concluir ativar/desativar restaurantes
- [ ] Explorar herança e polimorfismo
- [ ] Adicionar tratamento de erros nas entradas do usuário

## 👤 Autor

Davi Lemes – [GitHub](https://github.com/davi-lemes)
