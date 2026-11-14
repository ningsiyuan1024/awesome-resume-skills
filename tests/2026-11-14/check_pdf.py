"""Basic fixture fidelity check. Requires PyMuPDF; still inspect rendered pages."""
import json,re,sys
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parent
fixture=json.loads((ROOT/'fixtures/canonical.json').read_text(encoding='utf-8'))
bullets=[b for _,entries in fixture['sections'] for _,_,bs in entries for b in bs]
markers=['林知远','lin.zhiyuan@example.com','示例市','虚构星河科技','虚构城市大学','计算物理学','本科','中文办公','GUI','Harness','Qwen2.5-VL-3B-Instruct','84.9%','20%','85%','知识库检索与回写','尚未测量']
def norm(s):return re.sub(r'\s|\u00ad','',s)
failed=False
for filename in sys.argv[1:]:
 with fitz.open(filename) as doc:
  text='\n'.join(p.get_text() for p in doc);n=norm(text)
  missing=[s for s in markers+bullets if norm(s) not in n]
  outside=[s['text'] for p in doc for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if not fitz.Rect(-1,-1,p.rect.width+1,p.rect.height+1).contains(fitz.Rect(s['bbox']))]
  result={'file':Path(filename).name,'pages':len(doc),'missing':missing,'outside':outside,'replacement_chars':text.count('\ufffd')}
  failed|=bool(missing or outside or result['replacement_chars'])
  print(json.dumps(result,ensure_ascii=False))
if not sys.argv[1:]:raise SystemExit('Usage: python check_pdf.py file.pdf [file2.pdf ...]')
raise SystemExit(1 if failed else 0)
