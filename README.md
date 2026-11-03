# TX Pay — site institucional

Projeto estático local, sem dependências JavaScript e sem serviço de backend. Arquivos publicáveis em `public/`. Não há pagamentos, formulários, analytics, Meta Pixel ou cookies implementados.

## Situação atual

Dados preenchidos com os contatos, domínio e atividades informados pelo responsável. Site institucional: não possui catálogo, checkout ou processamento de pagamentos. A marca visual TX Pay foi mantida do projeto inicial.

Endereço e razão social consultados no Serasa em 03/11/2026: PAGAMENTOS E TECNOLOGIA TX LTDA - EPP; Rua Washington Luis 59 Lote 10B Quad, Centro, Nossa Senhora das Graças - PR, CEP 86680-000. O complemento foi preservado exatamente como exibido ("LOTE 10B QUAD"); conferir no comprovante oficial se existe informação adicional.

O Serasa informa como atividade principal 6619-3/02 — Correspondentes de instituições financeiras e não lista atividades secundárias. O responsável confirmou vendas de infoprodutos e produtos físicos e atuação como correspondente de instituições financeiras. O site apresenta essas três frentes, sem atribuir instituições parceiras, operações específicas ou autorizações não informadas. Conferir a consistência do cadastro oficial antes de submeter documentos à Meta. O site não resolve divergências cadastrais.

## Finalizar os dados

1. Editar `empresa.json`: razão social exatamente como consta no documento, endereço com CEP, e-mail comercial que funciona, telefone com DDI/DDD, URL HTTPS do domínio e descrição fiel da atuação.
2. Preencher `servicos` com objetos no formato `{"titulo": "Serviço real", "descricao": "Descrição confirmada"}`. Não descrever serviços regulados, integrações, licenças ou parceiros sem confirmação.
3. Revisar as páginas legais de acordo com a operação real, provedores, retenção de dados e canal de privacidade. O texto é uma base para este site institucional, não certificação de conformidade jurídica.
4. Marcar `dados_confirmados` como `true` somente depois de revisar todos os dados.
5. Executar `python3 scripts/build.py --release`. O comando falha se faltarem campos obrigatórios. A validação verifica preenchimento; não verifica autenticidade.
6. Versionar também os HTMLs gerados em `public/`. A Vercel publica os arquivos prontos e não executa Python.

Para gerar uma prévia com pendências: `python3 scripts/build.py`.
Para visualizar: `python3 -m http.server 4173 --directory public`, depois abrir http://localhost:4173.

## GitHub e Vercel

1. Criar um repositório GitHub e enviar todos os arquivos deste projeto.
2. Na Vercel, importar o repositório. Framework: Other. Build Command: vazio. Output Directory: public. O arquivo `vercel.json` já define essas opções.
3. Conectar o domínio da empresa e configurar o DNS conforme as instruções exibidas pela Vercel. Confirmar HTTPS e ausência de proteção por senha no site de produção.
4. Usar a URL final em `empresa.json`, gerar novamente e enviar ao GitHub.
5. Conferir início, contatos, páginas legais e versão celular no domínio final. As URLs .html funcionam no servidor local; Vercel pode redirecioná-las para URLs limpas.

## Preparação para a Meta

O site não garante aprovação e não substitui os documentos e a confirmação de vínculo exigidos pela Meta. Verificação da empresa e verificação do domínio são processos distintos. A elegibilidade e os documentos aplicáveis devem ser conferidos na Central de Segurança da conta.

- Manter nome legal, endereço, telefone e domínio consistentes no site, nos documentos e no portfólio empresarial.
- Utilizar contatos controlados pela empresa e ter os documentos oficiais atualizados.
- Caso a Meta forneça uma meta tag de verificação de domínio, preencher somente o valor do token em `meta_verification`, gerar novamente e publicar. A tag será colocada no HTML inicial, sem depender de JavaScript. Alternativamente usar a verificação DNS indicada pela Meta.
- Não inserir token fictício nem anunciar que a empresa foi verificada antes de isso ocorrer.
- Se forem adicionados Pixel, analytics, formulários ou um produto financeiro, revisar funcionalidades, políticas, bases legais e consentimento antes de publicar.

Referências (Serasa consultado pelo navegador; as páginas da Meta exigiram login/bloquearam leitura):
- https://www.facebook.com/business/help/2058515294227817
- https://www.facebook.com/business/help/159334372093366
- https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares
- Link cadastral fornecido: https://empresas.serasaexperian.com.br/consulta-gratis/PAGAMENTOS-E-TECNOLOGIA-TX-LTDA-EPP-58302216000191
