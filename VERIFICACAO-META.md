# Revisão do site para verificação da empresa — 03/11/2026

Este documento descreve o que foi conferido. Não é certificado de conformidade ou garantia de aprovação.

## Orientações oficiais consultadas diretamente no navegador

- Como verificar a empresa: https://www.facebook.com/business/help/2058515294227817
- Documentos oficiais: https://www.facebook.com/business/help/159334372093366
- Motivos de rejeição: https://www.facebook.com/business/help/2342133782492969

A Meta pede dados correspondentes à pessoa jurídica, site acessível em HTTPS e confirmação de vínculo por um método disponível na conta. Documentos oficiais podem ser solicitados para comprovar razão social e endereço ou telefone. A conta precisa estar qualificada e o responsável ter controle total do portfólio. O site não substitui essas etapas. As páginas consultadas não estabelecem que adicionar uma lista de políticas, logo ou missão garanta aprovação.

## Implementado no site

- Razão social, CNPJ, endereço e contatos visíveis em todas as páginas pelo rodapé.
- Relação explícita entre a identificação visual TX Pay e a pessoa jurídica responsável.
- Serviços confirmados pelo responsável, missão, visão e valores.
- Central de atendimento, telefone, e-mail e WhatsApp informado pelo responsável.
- Privacidade, cookies, termos, compras e entregas, trocas/cancelamentos/reembolsos.
- Conteúdo entregue em HTML, sem depender de JavaScript para ler dados da empresa.
- Nenhum perfil de Instagram; nenhum selo de aprovação, parceiro ou autorização inventados.
- Sitemap, navegação e links locais verificados. URLs .html preservadas na Vercel.
- Suporte à meta tag de domínio em empresa.json (meta_verification). O token só pode ser preenchido com o valor real fornecido pela Meta. Isso não verifica automaticamente o domínio.

## Dados e pendências externas

O responsável confirmou que a razão social e o endereço transcritos do Serasa estão exatos. Não foram examinados documentos oficiais, o cadastro da BM ou o acesso aos contatos.

O responsável confirmou atuação como correspondente, mas ainda não identificou as instituições contratantes e os serviços específicos. Não foi atestada conformidade regulatória dessa atividade nem elegibilidade de anúncios financeiros. A verificação da empresa também não aprova automaticamente anúncios, catálogo, produtos ou uso de WhatsApp.

Na consulta desta revisão, https://tecnologiatxltda.vercel.app retornou HTTP 404 com DEPLOYMENT_NOT_FOUND. Publicar o projeto na Vercel e testar novamente antes de submeter a verificação. Se o endereço final for diferente, atualizar empresa.json e gerar o site novamente.

O Gmail informado não comprova propriedade do domínio do site. Usar somente os métodos de vínculo apresentados pela Meta para a conta; não presumir que e-mail de domínio próprio ou verificação de domínio sejam obrigatórios em todos os casos.

## Conferência após publicação

1. Importar pgwempresa/txltda na Vercel: Other, sem build, saída public. Definir o nome do projeto conforme o domínio informado, se disponível.
2. Executar `python3 scripts/check.py --live`. O comando falha em HTTP de erro, HTTPS inválido ou página com conteúdo inesperado.
3. Conferir os dados da BM com os documentos, incluindo razão social, endereço e telefone.
4. Na Central de Segurança, seguir o fluxo exibido para a conta, apresentar documentos válidos quando solicitados e confirmar o vínculo pelo método disponível.
5. Se a Meta fornecer um token de domínio, inserir o token real em empresa.json e executar `python3 scripts/build.py --release`, verificar, enviar os arquivos ao GitHub e aguardar a publicação antes de tentar validar.

Não colocar documentos privados, contratos, contas ou credenciais neste repositório público.
