# Doutor Nota: O Detetive da Aprovação

O Doutor Nota é um modelo de inteligência artificial projetado para prever o desempenho acadêmico dos alunos em disciplinas relacionadas a matérias de exatas. Especificamente, foi desenvolvido com base nas disciplinas do curso de Ciência da Computação do Campus Chapecó da Universidade Federal da Fronteira Sul (UFFS), assim como nas matérias de domínio conexo dos cursos de Matemática e Engenharia Ambiental. O modelo foi construído levando em consideração as diretrizes dos Projetos Pedagógicos dos Cursos (PPCs) de Matemática de 2021, Ciência da Computação de 2018 e Engenharia Ambiental de 2013. O dataset utilizado para treinar o modelo é composto exclusivamente por matérias de exatas.

## Requisitos

- Python 3.11.6

## Instalação

Crie um ambiente virtual e instale as dependências:

no vscode é possivel criar um ambiente virtual com o comando `CTRL+SHIFT+P` e selecionando a opção Python: Create Environment

escolha `Venv` como o tipo de ambiente virtual
em seguida escolha a versão do python que deseja utilizar
por fim selecione o arquivo `requirements.txt` para instalar as dependências

## Execução

Quando o seu ambiente virtual estiver pronto, navegue até a pasta `src` e execute o notebook `download_data.ipynb` para baixar os dados necessários para treinar o modelo.
Em seguida execute o notebook `data_normalization.ipynb` para realizar a normalização dos dados.
Por fim execute o notebook `tf-keras_layers` para treinar o modelo.
