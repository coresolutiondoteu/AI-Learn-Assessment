#!/usr/bin/env python3
"""Offline editorial/data/packaging validator for the complete v2 academy."""
from pathlib import Path
import json, re, hashlib, collections, statistics
root=Path(__file__).resolve().parent.parent
load=lambda n:json.loads((root/'source'/n).read_text(encoding='utf8'))
legacy=load('question-bank.json'); extra=load('scenario-questions.json'); modules=load('modules.json')
clinics=load('engineering-clinics.json');glossary=load('glossary.json');resources=load('resources.json')
terms={x['term'] for x in glossary};modids={m['id'] for m in modules}; ids=set()
assert len(legacy)==252 and len(extra)==120 and len(modules)==len(clinics)==10 and len(glossary)==99
for q in legacy:
 assert q['id'] not in ids,q['id'];ids.add(q['id'])
 assert q['module'] in modids and q['term'] in terms,q['id']
 assert q['difficulty'] in {'advanced','foundation'},q['id']
 assert len(q['options'])==len(set(q['options']))==4 and q['answer'] in q['options'],q['id']
 assert all(q.get(k,'').strip() for k in ('question','hint','explanation')),q['id']
 for opt,note in q.get('distractor_notes',{}).items(): assert opt in q['options'] and opt!=q['answer'] and note.strip(),q['id']
for q in extra:
 assert q['id'] not in ids,q['id'];ids.add(q['id'])
 assert q['module'] in modids and q['term'] in terms,q['id']
 assert q['level'] in {2,3} and q['quality']=='curated',q['id']
 assert isinstance(q['lesson'],int) and 0<=q['lesson']<6,q['id']
 assert q['scenario'].strip() and q['question'].strip() and q['learning_note'].strip(),q['id']
 assert len(q['options'])==len(set(q['options']))==4 and q['answer'] in q['options'],q['id']
 assert len(q['distractor_notes'])==3,q['id']
 assert set(q['distractor_notes'])==set(q['options'])-{q['answer']},q['id']
 assert all(n.strip() for n in q['distractor_notes'].values()),q['id']
 assert not any('<script' in t.lower() for t in [q['question'],q['scenario']]),q['id']
 if q['evidence']:
  assert len(q['evidence'])>=2 and all(len(r)==len(q['evidence'][0]) for r in q['evidence']),q['id']
for m in modules:
 original=[q for q in legacy if q['module']==m['id']]; added=[q for q in extra if q['module']==m['id']]
 assert len(original)>=25 and len(added)==12,m['id']
 assert sum(q['difficulty']=='foundation' for q in original)>=12,m['id']
 assert sum(q['difficulty']=='advanced' for q in original)>=13,m['id']
 assert sum(q['level']==2 for q in added)==6 and sum(q['level']==3 for q in added)==6,m['id']
 assert len(m['topics'])==6,m['id']
 assert sorted([q['lesson'] for q in added if q['level']==2])==list(range(6)),m['id']
 assert sorted([q['lesson'] for q in added if q['level']==3])==list(range(6)),m['id']
assert len({x['id'] for x in clinics})==10 and {x['id'] for x in clinics}==modids
for c in clinics:
 assert len(c['steps'])==3 and len(c['evidence'])>=3 and c['proof'] and c['constraints'],c['id']
 assert all(len(row)==len(c['evidence'][0]) for row in c['evidence']),c['id']
 assert set(c['connections'])<=modids,c['id']
 for s in c['steps']:
  assert len(s['options'])==len(set(s['options']))==4 and s['answer'] in s['options'],c['id']
  assert set(s['distractor_notes'])==set(s['options'])-{s['answer']},c['id']
  assert all(s.get(k,'').strip() for k in ('question','explanation','insight')),c['id']
# Demonstrate no mechanically obvious correct-answer-length pattern for curated questions.
for lev in [2,3]:
 subset=[q for q in extra if q['level']==lev]
 longest=sum(len(q['answer'])>max(map(len,q['options'][1:])) for q in subset)
 shortest=sum(len(q['answer'])<min(map(len,q['options'][1:])) for q in subset)
 assert 8<=longest<=48 and 8<=shortest<=48,(lev,longest,shortest)
# Ensure the final single HTML file carries the exact approved content.
html=(root/'index.html').read_text(encoding='utf8')
mt=re.search(r'<script id="academy-data" type="application/json">(.*?)</script>',html,re.S);assert mt
payload=json.loads(mt.group(1))
assert payload['questions'][:252]==[{**q,'level':(1 if q['difficulty']=='foundation' else 2),'quality':'legacy'} for q in legacy]
assert payload['questions'][252:]==extra and payload['clinics']==clinics
assert payload['modules']==modules and payload['glossary']==glossary and payload['resources']==resources
assert html.count('__ACADEMY_DATA__')==0
assert 'function sampleBlueprint' in html and 'function clinicPage' in html
assert "const KEY='ai-systems-academy-v1'" in html
assert '<script src=' not in html.lower() and '<link rel="stylesheet"' not in html.lower()
assert (root/'docs/Opening_Study_Guide.pdf').is_file() and (root/'docs/AI_Systems_Field_Manual.pdf').is_file()
assert (root/'docs/Opening_Study_Guide.pdf').read_bytes().startswith(b'%PDF-')
assert (root/'docs/AI_Systems_Field_Manual.pdf').read_bytes().startswith(b'%PDF-')
print('CONTENT_VALIDATION=PASS')
print('Modules:',len(modules),'| Source lessons:',sum(len(m['topics']) for m in modules),'| Engineering clinics:',len(clinics),'| Guided clinic stages:',sum(len(c['steps']) for c in clinics))
print('Question bank:',len(legacy)+len(extra),'| L1:',sum(q['difficulty']=='foundation' for q in legacy),'| L2:',sum(q['difficulty']=='advanced' for q in legacy)+sum(q['level']==2 for q in extra),'| L3:',sum(q['level']==3 for q in extra))
print('Manual resources:',len(resources),'| Glossary entries:',len(glossary),'| PDF guides:',2)
