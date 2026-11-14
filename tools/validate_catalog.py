import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
ids=set()
for e in data['entries']:
    assert e['id'] not in ids,e['id']
    ids.add(e['id'])
    assert re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',e['repo'])
    assert e['path'].endswith('/SKILL.md') or e['path']=='SKILL.md'
    assert e['category'] in ('layout','content')
    assert e['status'] in ('listed','watch')
    for k in ('summary','limits','languages','outputs','sources'):assert e[k],(e['id'],k)
    for url in e['sources']+e['community']:assert url.startswith('https://'),url
    assert f"https://github.com/{e['repo']}" in (root/'README.md').read_text(encoding='utf-8')
for rel in ('README.md','CONTRIBUTING.md','LICENSE','docs/community-sources.md'):assert(root/rel).is_file(),rel
print(f'Catalog checks passed: {len(ids)} entries. Upstream code was not executed.')
