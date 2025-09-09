# 🎬 Sistema de Locadora – Filmes & Jogos

![Banner Animado](https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif)

Bem-vindo ao **Sistema de Locadora**, sua plataforma interativa para **gerenciar clientes, filmes e jogos**, com controle de locações em tempo real! 🚀  

---

## 🌟 Status do Projeto

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python) 
![POO](https://img.shields.io/badge/POO-Orientada%20a%20Objetos-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

---

## 🏆 Funcionalidades Principais

| 🎯 Função | ✅ Descrição | GIF |
| --- | --- | --- |
| Cadastro de Clientes | Armazena dados de clientes | ![Cliente](https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif) |
| Registro de Itens | Filmes e jogos com atributos únicos | ![Registro](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif) |
| Controle de Empréstimos | Locação e devolução de itens | ![Controle](https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif) |

---

## 📚 Estrutura de Classes

### **Item**
Classe base para filmes e jogos.  

| 📝 Atributo | Tipo | Descrição |
| --- | --- | --- |
| `codigo` | int | Código único |
| `titulo` | str | Título do item |
| `disponivel` | bool | Disponibilidade |

**Métodos:**  
- `alugar()` 🔴 Marca o item como alugado  
- `devolver()` 🟢 Marca o item como disponível  

---

### **Filme** *(herda de Item)*

| 🎬 Atributo | Tipo | Descrição |
| --- | --- | --- |
| `genero` | str | Gênero do filme |
| `duracao` | int | Duração em minutos |

![Filme GIF](https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif)

---

### **Jogo** *(herda de Item)*

| 🎮 Atributo | Tipo | Descrição |
| --- | --- | --- |
| `plataforma` | str | Plataforma do jogo |
| `faixaEtaria` | int | Faixa etária recomendada |

![Jogo GIF](https://media.giphy.com/media/l0HlSNOxJB956qwfK/giphy.gif)

---

### **Cliente**

| 🧑‍💼 Atributo | Tipo | Descrição |
| --- | --- | --- |
| `nome` | str | Nome do cliente |
| `cpf` | str | CPF do cliente |
| `itensLocados` | list[Item] | Lista de itens alugados |

**Ações do Cliente:**  
- `locar(item)` 🎯 Aluga um item  
- `devolver(item)` 🔄 Devolve um item  
- `listarItens()` 📋 Lista itens alugados  

![Cliente GIF](https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif)

---

### **Locadora**

| 🏢 Atributo | Tipo | Descrição |
| --- | --- | --- |
| `clientes` | list[Cliente] | Lista de clientes |
| `itens` | list[Item] | Lista de itens disponíveis |

**Funções da Locadora:**  
- 📝 Cadastro de clientes  
- 🎬 Registro de itens (Filmes e Jogos)  
- 🔄 Controle de empréstimos  

![Locadora GIF](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

---

## 🎨 Demonstração Visual (Dashboard Simulado)

| Item | Tipo | Disponível | Cliente |
| --- | --- | --- | --- |
| Matrix | Filme | ✅ | - |
| God of War | Jogo | 🔴 | João |
| Stranger Things | Filme | ✅ | - |
| FIFA 23 | Jogo | ✅ | - |

---

## ⚡ Tecnologias

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)  
![POO](https://img.shields.io/badge/POO-Orientada%20a%20Objetos-orange?style=for-the-badge)  

- Console interativo com `input()`  
- Listas dinâmicas e controle de fluxo avançado  
- Herança, encapsulamento e métodos customizados  

---

## 📞 Contato

- **GitHub:** [Meu github 🤩](https://github.com/MatheusCatarucci)  
- **Email:** matheus.catarucci7@gmail.com  

---

> “🎥 Jogos e filmes, todos em um só lugar, organizados com eficiência e diversão!”
