#!/usr/bin/env python3
"""Offline, standard-library-only rebuild of the course from editable JSON."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
src=root/'source'
files={'modules':'modules.json','glossary':'glossary.json','resources':'resources.json','questions':'question-bank.json','sourceLibrary':'source-library.json','patterns':'patterns.json','capstones':'capstones.json','studyPlan':'study-plan.json','scenarioQuestions':'scenario-questions.json','clinics':'engineering-clinics.json'}
data={name:json.loads((src/path).read_text(encoding='utf-8')) for name,path in files.items()}
data['questions']=[{**q, 'level':(1 if q['difficulty']=='foundation' else 2), 'quality':'legacy'} for q in data['questions']] + data.pop('scenarioQuestions')
payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<' + chr(92) + '/')
template=(src/'template.html').read_text(encoding='utf-8')
assert template.count('__ACADEMY_DATA__') == 1
(root/'index.html').write_text(template.replace('__ACADEMY_DATA__',payload),encoding='utf-8')
print('Rebuilt',root/'index.html')
