## Requisitos

- Python 3.X
- Pip (já vem instalado no python 3.X)

## Instalação

O primeiro passo é clonar o repositório e acessar o directório do projecto na linha de comando:

```bash
git clone https://github.com/paulocuambe/mexe.git
cd mexe
```

## Configurações

O próximo passo é configurar o ambiente para correr a aplicação.

### Ambiente virtual e dependências

Vamos criar um ambiente virtual onde a aplicação vai correr.

```bash
python -m venv env
env/Scripts/activate
```

**Nota**: Todos comandos daqui pra frente **devem** correr dentro do ambiente.
Estando dentro do ambiente virtual, vamos instalar as dependências do projecto:

```bash
(env) python -m pip install -r requirements.txt
```

### Configurando a aplicação

```bash
// Se estiver a no CMD
set FLASK_APP=run.py
set FLASK_ENV=development

// Se estiver no Powershell
$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"

// Se estiver em ambiente UNIX
export FLASK_APP=run.py
export FLASK_ENV=development

```

## Correndo a aplicação

Para correr a aplicação basta correr o comando abaixo.

```bash
python -m flask run
```

## Bónus

Se quiseres abrir uma nova aba na linha do comando, sempre deves correr o comando para activar o ambiente antes de correr qualquer outro comando no escopo do problema.

```bash
env/Scripts/activate
```
