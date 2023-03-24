<h1 align="center"> Teste Final Desenvolvedor Web (Back/Front-End) - Django/Python</h1>

A empresa de energia gostou de seu código para o cálculo de economia, mas necessita de algumas alterações para
disponibilizá-lo aos clientes. Assim, resolveu contratá-lo novamente para desenvolver essas novas funcionalidades.
Você continuará o projeto anterior usando a linguagem Python e o framework Django e, após finalizado, todo o código 
deve ser disponibilizado no Github para acompanhamento da empresa

Sua aplicação deverá cumprir os seguintes requisitos:

- Armazenar consumidores, seus dados pessoais e de consumo (dados para cadastro na planilha consumers.xlsx)
- Armazenar as regras de desconto seguindo a tabela dada
- Associar cada consumidor cadastrado a uma regra de desconto
- Calcular a economia baseada nos atributos do consumidor
- Listar os consumidores e a economia em uma tabela para uso dos clientes
- Permitir filtragem na tabela por tipo de consumidor e intervalo de consumo
- Permitir inclusão de consumidores por meio de formulário
- O formulário de cadastro deve preencher os campos de estado e cidade baseado no CEP. Para isso,
você deverá usar a API gratuita https://viacep.com.br/
- O documento do consumidor deve ser validado de acordo com o tipo. A validação pode ser no back ou no front-end.

Mais detalhes de cada tarefa são dados nos arquivos do projeto base.

## Tabela de Desconto
A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

## Conclusão
Você terá 4h para desenvolver a aplicação e, após finalizada, a empresa precisa de um vídeo explicativo sobre o que foi feito
e como a aplicação funciona. Faça um vídeo curto de 5 min descrevendo sua solução, tanto em termos técnicos quanto em relação ao produto final.
