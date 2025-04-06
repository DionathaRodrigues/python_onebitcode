# python_onebitcode

# 📘 Principais Comandos do Git

| Comando                          | Função                                                                 |
|----------------------------------|------------------------------------------------------------------------|
| `git init`                       | Inicializa um novo repositório Git local                              |
| `git clone <url>`                | Clona um repositório remoto para sua máquina local                    |
| `git status`                     | Exibe o status atual dos arquivos (modificados, não versionados etc.) |
| `git add <arquivo>`             | Adiciona um arquivo específico à área de staging                      |
| `git add .`                      | Adiciona todos os arquivos modificados à área de staging              |
| `git commit -m "mensagem"`       | Cria um commit com uma mensagem descritiva                            |
| `git push`                       | Envia os commits locais para o repositório remoto                     |
| `git pull`                       | Atualiza o repositório local com alterações do remoto                 |
| `git fetch`                      | Busca as atualizações do remoto sem mesclar                          |
| `git merge <branch>`             | Mescla outra branch à atual                                           |
| `git branch`                     | Lista todas as branches locais                                        |
| `git branch <nome-da-branch>`   | Cria uma nova branch                                                  |
| `git checkout <branch>`         | Muda para outra branch existente                                      |
| `git checkout -b <nova-branch>` | Cria e troca para uma nova branch                                     |
| `git log`                        | Mostra o histórico de commits                                         |
| `git remote -v`                  | Mostra os repositórios remotos configurados                          |
| `git reset --hard <commit>`     | Restaura o repositório para um commit específico (com perda de dados) |
| `git revert <commit>`           | Cria um novo commit que desfaz as alterações de um commit anterior    |
| `git stash`                      | Salva temporariamente alterações não commitadas                       |
| `git stash pop`                  | Restaura as alterações salvas com `stash`                             |


# 🚀 Passo a Passo para Subir Arquivos para o GitHub com Git

## 📁 1. Acesse a pasta do projeto
```bash
cd /caminho/do/seu/projeto
```

## 🔧 2. Inicialize o repositório Git (se ainda não tiver)
```bash
git init
```

## ➕ 3. Adicione todos os arquivos ao controle de versão
```bash
git add .
```

## ✅ 4. Faça o primeiro commit
```bash
git commit -m "Atualização"
```

## ⬆️ 5. Envie os arquivos para o GitHub
```bash
git push origin main
```