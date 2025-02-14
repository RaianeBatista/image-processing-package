# Módulo vs Pacote

## Módulo
Objeto que serve como unidade organizacional do código que é carregado pelo comando `import`.

## Pacote
Coleção de módulos com hierarquia.

# Modularização
## Vantagens da modularização:
- Legibilidade
- Manutenção
- Reaproveitamento de código

# Pacote em Python
## Vantagens de criar um pacote:
- Facilidade de compartilhamento
- Facilidade de instalação

## Conceitos:
- **PyPI**: Repositório público oficial de pacotes em Python.
- **Wheel e Sdist**: Dois tipos de distribuições.
- **Setuptools**: Pacote usado em `setup.py` para gerar as distribuições.
- **Twine**: Pacote usado para subir as distribuições no repositório PyPI.

# Criando o projeto e gerando as distribuições
Descomplicando a criação de pacotes em Python.

## Arquivo `requirements.txt`
Usado para especificar as dependências que devem ser instaladas com o pacote. Opcionalmente, podem ser especificadas as versões.

# Arquivo `setup.py`
Usado para especificar como o pacote deve ser construído.
[Documentação](https://setuptools.readthedocs.io/en/latest/setuptools.html)

# Distribuições
Para subir o pacote, é necessário criar uma distribuição binária ou uma distribuição de código fonte.
As versões mais recentes do `pip` instalam primeiramente a versão binária e usam a distribuição de código fonte apenas se necessário.
De qualquer forma, iremos criar ambas as distribuições.

## Comandos de instalação
```bash
python -m pip install --upgrade pip
pip install twine
pip install setuptools
```

## Comandos para criar distribuições
```bash
python setup.py sdist bdist_wheel
```

# Publicando o pacote
## Passos para subir o pacote  
1. Criar conta no Test PyPI
2. Publicar no Test PyPI
3. Instalar o pacote usando Test PyPI
4. Testar pacote
5. Criar conta no PyPI
6. Publicar no PyPI
7. Instalar o pacote usando PyPI

## Comando para publicar no Test PyPI
```bash
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

## Criando contas no PyPI
- [Criar conta no PyPI](https://pypi.org/account/register/)
- [Criar conta no Test PyPI](https://test.pypi.org/account/register/)

## Comando para instalar o pacote do PyPI
```bash
python -m pip install package_name
```

