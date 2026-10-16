// Přihlašovací brána pro Netlify (Edge Function). Soubor edge-functions/brana.js z této šablony
// vyrábí tools/export_web.py – ručně neupravovat. Odpověď na rodinnou otázku tu není, jen její otisk (SHA-256).
const HASH = '{{HASH}}';

async function sha256(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

export default async (request, context) => {
  const url = new URL(request.url);
  if (url.pathname === '/prihlaseni.html') return context.next();
  const answer = context.cookies.get('rodokmen') || '';
  if (answer && (await sha256(answer)) === HASH) {
    const res = await context.next();
    res.headers.set('X-Robots-Tag', 'noindex, nofollow');
    return res;
  }
  const login = await fetch(new URL('/prihlaseni.html', url));
  return new Response(await login.text(), {
    status: 401,
    headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex, nofollow' },
  });
};

export const config = { path: '/*' };
