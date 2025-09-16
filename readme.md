# 🎬 Sistema de Locadora – Filmes & Jogos

Bem-vindo ao **Sistema de Locadora**, sua plataforma interativa para **gerenciar clientes, filmes e jogos**, com controle de locações em tempo real\! 🚀

-----

## 🌟 Status do Projeto

-----

## 🏆 Funcionalidades Principais

| 🎯 Função | ✅ Descrição | GIF |
|---|---|---|
| Cadastro de Clientes | Armazena dados de clientes. |  |
| Registro de Itens | Gerencia filmes e jogos com atributos únicos. |  |
| Controle de Empréstimos | Facilita a locação e devolução de itens. |  |

-----

## 📚 Estrutura de Classes

### **Item**

Classe base para filmes e jogos.

| 📝 Atributo | Tipo | Descrição |
|---|---|---|
| `codigo` | `int` | Código único do item. |
| `titulo` | `str` | Título do item. |
| `disponivel` | `bool` | Indica se o item está disponível para locação. |

**Métodos:**

  * `alugar()` 🔴 Marca o item como alugado.
  * `devolver()` 🟢 Marca o item como disponível.

-----

### **Filme** *(herda de Item)*

| 🎬 Atributo | Tipo | Descrição |
|---|---|---|
| `genero` | `str` | Gênero do filme. |
| `duracao` | `int` | Duração do filme em minutos. |

-----

### **Jogo** *(herda de Item)*

| 🎮 Atributo | Tipo | Descrição |
|---|---|---|
| `plataforma` | `str` | Plataforma em que o jogo roda. |
| `faixaEtaria` | `int` | Faixa etária recomendada para o jogo. |

-----

### **Cliente**

| 🧑‍💼 Atributo | Tipo | Descrição |
|---|---|---|
| `nome` | `str` | Nome completo do cliente. |
| `cpf` | `str` | CPF do cliente. |
| `itensLocados` | `list[Item]` | Lista de itens atualmente alugados pelo cliente. |

**Ações do Cliente:**

  * `locar(item)` 🎯 Aluga um item.
  * `devolver(item)` 🔄 Devolve um item.
  * `listarItens()` 📋 Lista todos os itens alugados pelo cliente.

-----

### **Locadora**

| 🏢 Atributo | Tipo | Descrição |
|---|---|---|
| `clientes` | `list[Cliente]` | Lista de todos os clientes cadastrados. |
| `itens` | `list[Item]` | Lista de todos os itens (filmes e jogos) disponíveis. |

**Funções da Locadora:**

  * 📝 Cadastro de novos clientes.
  * 🎬 Registro de novos itens (Filmes e Jogos).
  * 🔄 Controle de empréstimos e devoluções.

-----

## 🎨 Demonstração Visual (Dashboard Simulado)

| Item | Tipo | Disponível | Cliente |
|---|---|---|---|
| Matrix | Filme | ✅ | - |
| God of War | Jogo | 🔴 | João |
| Stranger Things | Filme | ✅ | - |
| FIFA 23 | Jogo | ✅ | - |

-----

## ⚡ Tecnologias Utilizadas

  * Interface de console interativa utilizando `input()`.
  * Gerenciamento dinâmico de listas e controle de fluxo avançado.
  * Implementação de conceitos de Orientação a Objetos: **herança**, **encapsulamento** e **métodos customizados**.

-----

## 📞 Contato

  * **GitHub:** [Meu github 🤩](https://www.google.com/search?q=https://github.com/MatheusCatarucci)
  * **Email:** matheus.catarucci7@gmail.com

-----

> “🎥 Jogos e filmes, todos em um só lugar, organizados com eficiência e diversão\!”

