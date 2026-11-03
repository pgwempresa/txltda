# -*- coding: utf-8 -*-
"""Verifica HTML local; use --live para verificar também o domínio publicado."""
import json, sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from urllib.request import urlopen, Request
ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / 'public'
c = json.loads((ROOT / 'empresa.json').read_text())
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=set(); self.links=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        for key in ('href','src'):
            if a.get(key): self.links.append(a[key])
pages={p.name:Page(p.read_text()) for p in PUBLIC.glob('*.html')}
for name,page in pages.items():
    text=(PUBLIC/name).read_text()
    assert c['razao_social'] in text and c['cnpj'] in text, name
    assert 'instagram.com' not in text and 'A confirmar antes' not in text, name
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        target=u.path.lstrip('/') or ('index.html' if u.path=='/' else name)
        assert (PUBLIC/target).is_file(), (name,link)
        if u.fragment and target in pages: assert u.fragment in pages[target].ids, (name,link)
    if name!='404.html': assert 'noindex' not in text, name
assert 'https://wa.me/5563981287218' in (PUBLIC/'index.html').read_text()
print(f'OK: {len(pages)} páginas, identidade, links, âncoras, assets e WhatsApp. Sem Instagram.')
if '--live' in sys.argv:
    base=c['dominio'].rstrip('/')
    for name in list(pages)+['style.css','site.js','logo.svg','robots.txt','sitemap.xml']:
        if name=='404.html': continue
        url=base+'/'+('' if name=='index.html' else name)
        try:
            with urlopen(Request(url,headers={'User-Agent':'TX-Site-Check/1.0'}),timeout=20) as response:
                assert response.status==200 and response.url.startswith('https://'),url
                content=response.read().decode('utf-8')
                if name.endswith('.html'): assert c['cnpj'] in content,(url,'conteúdo inesperado')
            print('OK HTTPS',url)
        except Exception as error:
            raise SystemExit(f'FALHA na publicação: {url}: {error}')
