### Característica | Detalhe
| :---  | :--- |
| Nome: | Pesquisa Industrial Mensal - Produção Física (PIMPF) |
| Fonte:| IBGE - SIDRA |
| URL de Origem: | https://sidra.ibge.gov.br/home/pimpf/fbr/brasil |
| Número de Amostras (Linhas): | 31 | 
| Número de Atributos (Colunas): | 7 | 

## Tabela de Catálogo de Atributos (Metadados)

| Nome da Variável | Tipo | Descrição | Unidades | Valores Faltantes? |
| :--- | :--- | :--- | :--- | :--- |
| **Seções e atividades industriais** | Categórico/Textual | Classifica o setor/subsetor da produção industrial (e.g., "Indústria geral"). | Não se aplica | Sim, 1 |
| **Índice de base fixa mensal sem ajuste sazonal** | Numérico (float) | Índice de produção física (Média 2022 = 100), sem ajuste sazonal. | Índice (Base 100) | Sim, 3 |
| **Índice de base fixa mensal com ajuste sazonal** | Numérico (float) | Índice de produção física (Média 2022 = 100), com ajuste sazonal. | Índice (Base 100) | Sim, 3 |
| **Variação percentual mês/mês imediatamente anterior** | Numérico (float) | Variação da produção em comparação ao mês imediatamente anterior, com ajuste sazonal. | Percentual (%) | Sim, 3 |
| **Variação percentual mensal (Ano Anterior)** | Numérico (float) | Variação da produção em comparação ao mesmo mês do ano anterior. | Percentual (%) | Sim, 3 |
| **Variação percentual acumulada no ano** | Numérico (float) | Variação acumulada da produção industrial desde o início do ano corrente. | Percentual (%) | Sim, 3 |
| **Variação percentual acumulada nos últimos 12 meses** | Numérico (float) | Variação acumulada da produção industrial nos últimos 12 meses. | Percentual (%) | Sim, 3 |