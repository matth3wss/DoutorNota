# Doutor Nota: O Detetive da Aprovação

O Doutor Nota é um modelo de inteligência artificial projetado para prever o desempenho acadêmico dos alunos em disciplinas relacionadas a matérias de exatas. Especificamente, foi desenvolvido com base nas disciplinas do curso de Ciência da Computação do Campus Chapecó da Universidade Federal da Fronteira Sul (UFFS), assim como nas matérias de domínio conexo dos cursos de Matemática e Engenharia Ambiental. O modelo foi construído levando em consideração as diretrizes dos Projetos Pedagógicos dos Cursos (PPCs) de Matemática de 2021, Ciência da Computação de 2018 e Engenharia Ambiental de 2013.

## Requisitos

- Python 3.11.6

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

## Fine-tuning do dataset

### 1ª Iteração

Antes de iniciar a documentação das melhorias nas métricas, eu havia decidido que o modelo preveria o status (aprovado (0) ou reprovado (1)) com base nos seguintes atributos: ccr, frequência, disciplina e docentes.

A tabela a seguir apresenta as métricas de desempenho do modelo:

| Model | Accuracy | AUC    | Recall | Precision | F1    | Kappa  | MCC  |
| ----- | -------- | ------ | ------ | --------- | ----- | ------ | ---- |
| LGBM  | 0.7663   | 0.7884 | 0.407  | 0.6604    | 0.503 | 0.3618 | 0.38 |

A imagem a seguir representa a importância das features do modelo em relação ao status, ou seja, quais dos atributos na tabela têm maior influência sobre a previsão do status.

![png](/src/static/feature_importance/fi_1.png)

A matriz de confusão do modelo apresenta os seguintes valores: TP, FP, FN e TN. Isso pode parecer um pouco confuso, mas esses valores desempenham papéis importantes. Os valores "TP" (0,0) indicam que o modelo acertou a previsão de aprovação do aluno em 91% das vezes, enquanto os valores "TN" (1,1) representam a precisão do modelo ao prever a reprovação do aluno em 41% das vezes.

Aqui está o porquê disso ser relevante: prever a reprovação de um aluno é uma questão séria. A métrica de Precisão ajuda a determinar quantas das previsões de reprovação feitas pelo modelo realmente correspondem à realidade. Por que isso é crucial? Se você basear suas decisões em minha IA para planejar seus estudos, ela poderá erroneamente prever que você será reprovado, mesmo que você possa passar no exame. Portanto, a precisão é uma métrica fundamental para avaliar a confiabilidade do modelo e a precisão de suas previsões.

![png](/src/static/confusion_matrix/cm_1.png)

| **Iteração** | **TP** | **FP** | **FN** | **TN** |
| ------------ | ------ | ------ | ------ | ------ |
| 1ª Iteração  | 91%    | 9%     | 59%    | 41%    |

### 2ª Iteração

Após várias tentativas de aprimorar os atributos, optei por revisitar a correlação entre algumas colunas do conjunto de dados para determinar se elas afetavam no status. Verifiquei que as colunas "faltas" e "nome_curso" não apresentavam uma correlação significativa, enquanto o atributo "ano" demonstrou ter uma correlação mais forte do que a frequência.

| Model | Accuracy | AUC    | Recall | Precisão | F1     | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | -------- | ------ | ------ | ------ |
| LGBM  | 0.7638   | 0.8052 | 0.4029 | 0.6557   | 0.4991 | 0.3559 | 0.3739 |

![png](/src/static/feature_importance/fi_2.png)
![png](/src/static/confusion_matrix/cm_2.png)

Nesta tabela, podemos ver as mudanças nas taxas de TP, FP, FN e TN antes e após as melhorias na matriz de confusão.

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |

### 3ª Iteração

Percebi, ao analisar os dados manualmente, que alguns alunos estavam sendo reprovados mesmo tendo 100% de presença. Isso ocorria devido a alguns professores registrarem a presença dos alunos, mesmo quando estes não compareciam às aulas. Essa prática estava distorcendo as métricas.

Assim, optei por excluir as linhas em que a situação da turma era igual a 1 (reprovação) e a frequência na turma era de 100%. Com essa pequena alteração, observamos uma melhora significativa nas métricas.

| Model | Accuracy | AUC    | Recall | Prec.  | F1    | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | ------ | ----- | ------ | ------ |
| LGBM  | 0.8392   | 0.8927 | 0.5245 | 0.7316 | 0.611 | 0.5131 | 0.5244 |

Após implementar essas alterações, notou-se um aumento significativo na importância de todas as variáveis em relação ao atributo "status".

![png](/src/static/feature_importance/fi_3.png)

![png](/src/static/confusion_matrix/cm_3.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |

### 4ª Iteração

Anteriormente, eu havia decidido que os alunos reprovados devido a baixas notas e faltas não eram de interesse. No entanto, depois de examinar mais detalhadamente o conjunto de dados, percebi que poderia haver alunos que frequentaram algumas aulas, fizeram exames e, ao perceberem que tiveram um desempenho muito ruim, desistiram do curso. Portanto, decidi reintegrar esses alunos ao conjunto de dados, incluindo aqueles que foram reprovados por notas e reprovados por notas e faltas.

| Model | Accuracy | AUC   | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ----- | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.866    | 0.948 | 0.7379 | 0.8920 | 0.8077 | 0.7063 | 0.7138 |

![png](/src/static/feature_importance/fi_4.png)
![png](/src/static/confusion_matrix/cm_4.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |

### 5ª Iteração

Adicionei os alunos onde sit_turma = "REPROVADO POR FREQUENCIA" e com media != 0

| Model | Accuracy | AUC   | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ----- | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8690   | 0.942 | 0.7495 | 0.8894 | 0.8135 | 0.7136 | 0.7199 |

![png](/src/static/feature_importance/fi_5.png)
![png](/src/static/confusion_matrix/cm_5.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |

### 6ª Iteração

Adicionei os alunos onde sit_turma = "DESISTENTE" e com media != 0

| Model | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8697   | 0.9426 | 0.7553 | 0.8861 | 0.8155 | 0.7158 | 0.7213 |

![png](/src/static/feature_importance/fi_6.png)
![png](/src/static/confusion_matrix/cm_6.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |

7ª Iteração

Colocando apenas os professores que deram aula onde ano>=2022

| Model | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8769   | 0.9464 | 0.8026 | 0.8714 | 0.8356 | 0.7375 | 0.7391 |

![png](/src/static/feature_importance/fi_7.png)
![png](/src/static/confusion_matrix/cm_7.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |
| 7ª Iteração  | 92% ⬇️2% | 8% ⬆️2% | 20% ⬇️4% | 80% ⬆️4% |

8ª Iteração

Percebi que a função que criei para incluir as linhas com um certo atributo incluia tudo que tivesse uma string parcial e isso estava incluindo turmas onde dois professores onde um dos professores não está mais presente na UFFS. Corrigi e agora só aceita ser uma match exato. Retornado os valores de TP e de FP antes da iteração 7.

| Model | Accuracy | AUC   | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ----- | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8846   | 0.961 | 0.8    | 0.8889 | 0.8421 | 0.7516 | 0.7542 |

![png](/src/static/feature_importance/fi_8.png)
![png](/src/static/confusion_matrix/cm_8.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |
| 7ª Iteração  | 92% ⬇️2% | 8% ⬆️2% | 20% ⬇️4% | 80% ⬆️4% |
| 8ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 20%      | 80%      |

9ª Iteração

Percebi que tinha convertido gex016(sistemas digitais) para 607(algebra linear) inves de GEX606(sistemas digitais ppc2018)

| Model | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8956   | 0.9607 | 0.8286 | 0.8923 | 0.8593 | 0.7765 | 0.7778 |

![png](/src/static/feature_importance/fi_9.png)
![png](/src/static/confusion_matrix/cm_9.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |
| 7ª Iteração  | 92% ⬇️2% | 8% ⬆️2% | 20% ⬇️4% | 80% ⬆️4% |
| 8ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 20%      | 80%      |
| 9ª Iteração  | 94%      | 6%      | 17% ⬇️3% | 83% ⬆️3% |

10ª Iteração

Numa última tentativa de melhorar os TN eu resolvi adicionar o turno na qual o aluno gostaria de fazer a materia.

| Model | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
| ----- | -------- | ------ | ------ | ------ | ------ | ------ | ------ |
| LGBM  | 0.8956   | 0.9545 | 0.8592 | 0.8714 | 0.8652 | 0.7801 | 0.7801 |

![png](/src/static/feature_importance/fi_10.png)
![png](/src/static/confusion_matrix/cm_10.png)

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |
| 7ª Iteração  | 92% ⬇️2% | 8% ⬆️2% | 20% ⬇️4% | 80% ⬆️4% |
| 8ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 20%      | 80%      |
| 9ª Iteração  | 94%      | 6%      | 17% ⬇️3% | 83% ⬆️3% |
| 10ª Iteração | 92%      | 8% ⬇️2% | 14% ⬇️3% | 86% ⬆️3% |

Resumo das matrizes de confusão

| **Iteração** | **TP**   | **FP**  | **FN**   | **TN**   |
| ------------ | -------- | ------- | -------- | -------- |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 2ª Iteração  | 92% ⬆️1% | 8% ⬇️1% | 58% ⬇️1% | 42% ⬆️1% |
| 3ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 48% ⬇️10 | 52% ⬆️10 |
| 4ª Iteração  | 94%      | 6%      | 26% ⬇️22 | 74% ⬆️22 |
| 5ª Iteração  | 94%      | 6%      | 25% ⬇️1% | 75% ⬆️1% |
| 6ª Iteração  | 94%      | 6%      | 24% ⬇️1% | 76% ⬆️1% |
| 7ª Iteração  | 92% ⬇️2% | 8% ⬆️2% | 20% ⬇️4% | 80% ⬆️4% |
| 8ª Iteração  | 94% ⬆️2% | 6% ⬇️2% | 20%      | 80%      |
| 9ª Iteração  | 94%      | 6%      | 17% ⬇️3% | 83% ⬆️3% |
| 10ª Iteração | 92%      | 8% ⬇️2% | 14% ⬇️3% | 86% ⬆️3% |
|              |          |         |          |          |
| 1ª Iteração  | 91%      | 9%      | 59%      | 41%      |
| 10ª Iteração | 92%      | 8% ⬇️2% | 14% ⬇️3% | 86% ⬆️3% |

Resumo das métricas

| Iterações    | Accuracy | AUC      | Recall    | Prec.    | F1       | Kappa     | MCC       |
| ------------ | -------- | -------- | --------- | -------- | -------- | --------- | --------- |
| 1ª Iteração  | 0.7663   | 0.7884   | 0.4070    | 0.6604   | 0.5030   | 0.3618    | 0.3800    |
| 2ª Iteração  | 0.7638   | 0.8052   | 0.4029    | 0.6557   | 0.4991   | 0.3559    | 0.3739    |
| 3ª Iteração  | 0.8392   | 0.8927   | 0.5245    | 0.7316   | 0.6110   | 0.5131    | 0.5244    |
| 4ª Iteração  | 0.8660   | 0.9480   | 0.7379    | 0.8920   | 0.8077   | 0.7063    | 0.7138    |
| 5ª Iteração  | 0.8690   | 0.9420   | 0.7495    | 0.8894   | 0.8135   | 0.7136    | 0.7199    |
| 6ª Iteração  | 0.8697   | 0.9426   | 0.7553    | 0.8861   | 0.8155   | 0.7158    | 0.7213    |
| 7ª Iteração  | 0.8769   | 0.9464   | 0.8026    | 0.8714   | 0.8356   | 0.7375    | 0.7391    |
| 8ª Iteração  | 0.8846   | 0.9610   | 0.8000    | 0.8889   | 0.8421   | 0.7516    | 0.7542    |
| 9ª Iteração  | 0.8956   | 0.9607   | 0.8286    | 0.8923   | 0.8593   | 0.7765    | 0.7778    |
| 10ª Iteração | 0.8956   | 0.9545   | 0.8592    | 0.8714   | 0.8652   | 0.7801    | 0.7801    |
|              |          |          |           |          |          |           |           |
| 1ª Iteração  | 0.7663   | 0.7884   | 0.4070    | 0.6604   | 0.5030   | 0.3618    | 0.3800    |
| 10ª Iteração | 0.8956   | 0.9545   | 0.8592    | 0.8714   | 0.8652   | 0.7801    | 0.7801    |
| Resultados   | ⬆️16.87% | ⬆️21.07% | ⬆️111.11% | ⬆️31.95% | ⬆️72.01% | ⬆️115.62% | ⬆️105.29% |
