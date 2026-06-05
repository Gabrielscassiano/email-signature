/* Gate de senha (HTTP Basic Auth) para o portal de dados cadastrais.
 *
 * A senha NÃO fica no código. Configure no painel do Cloudflare Pages em
 * Settings > Variables and Secrets (escopo Production e Preview):
 *   PORTAL_PASSWORD  = a senha   (obrigatório)
 *   PORTAL_USER      = usuário   (opcional; padrão "onegroup")
 *
 * Enquanto PORTAL_PASSWORD não estiver definida, o site fica BLOQUEADO
 * por segurança (não publica os dados sem senha por engano).
 */
export async function onRequest(context) {
  const { request, env, next } = context;

  const expectedPass = env.PORTAL_PASSWORD;
  const expectedUser = env.PORTAL_USER || "onegroup";

  if (!expectedPass) {
    return new Response(
      "Portal bloqueado: defina a variável PORTAL_PASSWORD no Cloudflare Pages.",
      { status: 503, headers: { "Content-Type": "text/plain; charset=utf-8" } }
    );
  }

  const header = request.headers.get("Authorization") || "";
  if (header.startsWith("Basic ")) {
    let user = "", pass = "";
    try {
      const decoded = atob(header.slice(6));
      const idx = decoded.indexOf(":");
      user = decoded.slice(0, idx);
      pass = decoded.slice(idx + 1);
    } catch (_) {}

    if (safeEqual(user, expectedUser) && safeEqual(pass, expectedPass)) {
      return next();
    }
  }

  return new Response("Autenticação necessária.", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Dados Cadastrais One Group", charset="UTF-8"',
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}

// comparação em tempo constante para evitar timing attacks
function safeEqual(a, b) {
  a = String(a); b = String(b);
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}
