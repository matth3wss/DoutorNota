# Doutor Nota: O Detetive da Aprovação

O Doutor Nota é um modelo de inteligência artificial projetado para prever o desempenho acadêmico dos alunos em disciplinas relacionadas a matérias de exatas. Especificamente, foi desenvolvido com base nas disciplinas do curso de Ciência da Computação do Campus Chapecó da Universidade Federal da Fronteira Sul (UFFS), assim como nas matérias de domínio conexo dos cursos de Matemática e Engenharia Ambiental. O modelo foi construído levando em consideração as diretrizes dos Projetos Pedagógicos dos Cursos (PPCs) de Matemática de 2021, Ciência da Computação de 2018 e Engenharia Ambiental de 2013.

## Requisitos

- Python 3.10.11

## Instalação

Para configurar o ambiente de desenvolvimento e instalar as dependências necessárias, siga os passos abaixo:

1. Crie um ambiente virtual no VSCode. Para fazer isso, utilize o atalho `CTRL+SHIFT+P` e selecione a opção "Python: Create Environment".

2. Escolha o tipo de ambiente virtual `Venv`.

3. Selecione a versão do Python que deseja utilizar para o seu projeto.

4. Por fim, selecione o arquivo `requirements.txt` para instalar as dependências necessárias. Isso garantirá que o ambiente virtual seja configurado com as bibliotecas corretas para o seu projeto.

## Instruções de Execução

Para seguir adiante com a execução deste projeto, siga as etapas abaixo:

1. **Preparação do Ambiente Virtual**: Certifique-se de que o ambiente virtual necessário esteja configurado e pronto para uso.

2. **Download de Dados**: Navegue até a pasta `src\notebooks` e execute o notebook `download_data.ipynb`. Esse passo é fundamental para obter os dados necessários para o treinamento do modelo.

3. **Normalização dos Dados**: Execute o notebook `data_normalization.ipynb` para realizar a normalização dos dados. Isso é crucial para garantir que os dados estejam em um formato adequado para o treinamento do modelo.

4. **Treinamento do Modelo**: Por fim, execute o notebook `LGBMClassifier.ipynb` para iniciar o treinamento do modelo. Este é o passo final que permitirá criar o modelo de classificação desejado.

Siga essas etapas sequencialmente para obter os melhores resultados no seu projeto.

## Realizando a predição

No notebook `LGBMClassifier.ipynb` é possível realizar a predição de uma materia específica. Para isso, basta alterar o valor do dropdown `ccr`, do dropdown `docentes` e usar o slider `frequencia` para definir a frequência do aluno.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```bash
├── src
│   ├── input
│   │   ├── alunos.csv
│   │   ├── test.json
├── models
│   └── LGBMClassifier.pkl
├── notebooks
│   ├── data_normalization.ipynb
│   ├── download_dataset.ipynb
│   └── LGBMClassifier.ipynb
├── output
│   └── alunos_final.csv
├── .gitignore
├── README.md
├── requirements.txt
```
