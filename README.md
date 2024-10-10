Gerador de PDF de Avaliação de Funcionários

Este projeto consiste em um gerador de PDF que avalia o desempenho de funcionários com base na quantidade de vendas realizadas. O PDF gerado inclui o nome do funcionário, a quantidade de vendas e a avaliação do seu desempenho.
Uso

    Execute o script gerador_pdf.py:

    bash

    python gerador_pdf.py

    O programa solicitará que você insira o nome do funcionário e a quantidade de vendas realizadas.

    Após fornecer as informações, um PDF será gerado na pasta python-gerador-pdf/ com as informações fornecidas.

Funcionamento

    Entrada do Usuário: O programa pede ao usuário para inserir o nome do funcionário (apenas o primeiro nome) e a quantidade de vendas realizadas.
    Avaliação do Funcionário: O desempenho do funcionário é avaliado com base na quantidade de vendas:
        Se o funcionário fez 25 vendas ou mais, ele será avaliado como "Sim!".
        Se o funcionário fez menos de 25 vendas, será exibida a mensagem "Não, mínimo de 25 vendas."
    Geração do PDF: O PDF é gerado com o nome do funcionário, a quantidade de vendas e a avaliação, além de um plano de fundo personalizado.

Personalização

Você pode personalizar o fundo do PDF substituindo a imagem plano-de-fundo.png pela sua própria imagem. Certifique-se de que a nova imagem esteja no formato correto e que as dimensões sejam adequadas ao tamanho da página A4.
