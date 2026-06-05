# Portal de Dados Cadastrais — One Group

Página estática, na identidade da marca, com **botão de copiar em cada campo**
(e "Copiar tudo" por seção), para entregar os dados cadastrais da empresa a
**clientes e fornecedores** fazerem o cadastro nos sistemas deles.

Protegida por **senha** (Cloudflare Pages + Basic Auth).

## Arquivos

| Arquivo | O que é |
|---|---|
| `index.html` | A página (não precisa editar). |
| `dados-empresa.js` | **Os dados** — edite só este arquivo. |
| `functions/_middleware.js` | Gate de senha (Cloudflare Pages Function). |

## Como preencher

Abra `dados-empresa.js` e preencha os campos. O que ficar `""` aparece como `—`.

## Uma página por empresa (reutilizável)

Toda empresa do grupo vai precisar de uma. É só **duplicar esta pasta** e editar
o `dados-empresa.js` da cópia — cada uma vira um projeto/deploy próprio.

## Deploy no Cloudflare Pages (com senha)

1. No painel da Cloudflare: **Workers & Pages → Create → Pages → Connect to Git**
   e selecione este repositório.
2. Configurações de build:
   - **Framework preset:** None
   - **Build command:** *(deixe vazio)*
   - **Build output directory:** `/`
   - **Root directory (advanced):** `portal`
3. Após o primeiro deploy, vá em **Settings → Variables and Secrets** e adicione
   (para Production **e** Preview):
   - `PORTAL_PASSWORD` = a senha de acesso  *(obrigatório)*
   - `PORTAL_USER` = usuário *(opcional; padrão `onegroup`)*
4. Faça um novo deploy (Retry/Redeploy) para as variáveis valerem.

> Sem `PORTAL_PASSWORD` definida, o portal fica **bloqueado** de propósito —
> assim os dados nunca ficam públicos por engano.

### Alternativa: Cloudflare Access (Zero Trust)
Se preferir login por e-mail/OTP em vez de senha única, dá para usar
**Cloudflare Access** no lugar do gate acima (apague `functions/_middleware.js`):
Zero Trust → Access → Applications → Add → Self-hosted, apontando para o domínio
do Pages, com uma policy de e-mails permitidos. O gate por senha deste repo é o
caminho mais simples e já funciona sem configurar o Zero Trust.
