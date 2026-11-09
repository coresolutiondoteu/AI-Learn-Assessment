// Offline contract/behavior regression using Node VM; no external packages.
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const html=fs.readFileSync(path.join(__dirname,'..','index.html'),'utf8');
const dataMatch=html.match(/<script id="academy-data" type="application\/json">([\s\S]*?)<\/script>/);
const jsMatch=html.match(/<script>\s*([\s\S]*?)<\/script>/);
assert(dataMatch&&jsMatch,'embedded course payload and script');
const raw=dataMatch[1],data=JSON.parse(raw),app={innerHTML:'',addEventListener(){}},events={};
// Realistic v1 persisted progress: current app must load the same key/schema.
const store={'ai-systems-academy-v1':JSON.stringify({version:1,doneTopics:{'stack:0':true},doneLabs:{},labSteps:{},labEvidence:{},checkpoints:{},vocab:{},exams:[],activeExam:null})};
const ctx={console,setTimeout,clearTimeout,Math,Date,JSON,Object,Array,Map,Set,Number,String,Boolean,
 window:{addEventListener(){},scrollTo(){}},document:{querySelector(sel){if(sel==='#academy-data')return {textContent:raw};throw Error(sel)},getElementById(id){if(id==='app')return app;if(id==='toast')return {innerHTML:''};throw Error(id)}},
 localStorage:{getItem(k){return store[k]||null},setItem(k,v){store[k]=v}},location:{hash:''},confirm(){return true}};
const js=jsMatch[1].replace(/\n\}\)\(\);\s*$/,`\nwindow.__test={UI,M,Q,V,S:()=>S,render,assessment,startGuided,guidedUI,handleAction,learningPanel,createExam,examUI,submitExam,resultView,clinicPage,clinicRecord,casebookPage,gradeBreakdown,levelOf,sampleBlueprint};\n})();\n`);
assert(js.includes('window.__test='));
vm.runInNewContext(js,ctx,{filename:'academy inline script',timeout:2000});
const t=ctx.window.__test, QMAP=Object.fromEntries(t.Q.map(q=>[q.id,q]));
function pass(cond,msg){assert(cond,msg);console.log('PASS',msg)}
pass(app.innerHTML.includes('AI Systems Academy'),'application initializes');
pass(t.M.length===10&&t.V.length===99&&t.Q.length===372&&data.clinics.length===10,'all base and expansion content embedded');
pass(t.S().doneTopics['stack:0']===true,'pre-existing v1 learner progress preserved');
pass(new Set(t.Q.map(q=>q.id)).size===372,'no duplicate identifiers');
for(let q of t.Q){assert(q.options.length===4&&new Set(q.options).size===4,q.id);assert(q.options.includes(q.answer),q.id);assert([1,2,3].includes(t.levelOf(q)),q.id);for(let alt of Object.keys(q.distractor_notes||{})){assert(q.options.includes(alt)&&alt!==q.answer,q.id)}}
pass(true,'four distinct choices and one valid answer on all 372 questions');
for(let m of t.M){const z=t.Q.filter(q=>q.module===m.id),breakdown=[1,2,3].map(l=>z.filter(q=>t.levelOf(q)===l).length);
 assert(breakdown[0]>=12&&breakdown[1]>=19&&breakdown[2]===6,m.id);}
pass(true,'every domain has at least 12 L1, 19 L2 and six L3 questions');
// Section assessment: 6 / 10 / 4 exact mix with fresh random option order.
for(let m of t.M){t.createExam('section',m.id,20);let ex=t.S().activeExam;
 assert(ex.count===20);assert.strictEqual(new Set(ex.items.map(x=>x.id)).size,20);
 assert.deepStrictEqual([1,2,3].map(l=>ex.items.filter(x=>t.levelOf(QMAP[x.id])===l).length),[6,10,4]);
 assert(ex.items.every(x=>QMAP[x.id].module===m.id));
 t.S().activeExam=null;
}
pass(true,'10 section blueprints have 30/50/20 level mix and unique items');
for(let len of [20,30,40]){t.createExam('full',null,len);let ex=t.S().activeExam;
 assert.strictEqual(ex.count,len);assert.strictEqual(new Set(ex.items.map(x=>x.id)).size,len);
 assert.deepStrictEqual([1,2,3].map(l=>ex.items.filter(x=>t.levelOf(QMAP[x.id])===l).length),[len*.3,len*.5,len*.2]);
 for(let m of t.M)assert.strictEqual(ex.items.filter(x=>QMAP[x.id].module===m.id).length,len/10,'domain-balanced '+len);
 ex.index=len-1;t.render();assert(app.innerHTML.includes('Submit exam')&&!app.innerHTML.includes('data-action="exam-next" disabled'));
 t.S().activeExam=null;
}
pass(true,'20/30/40 full blueprints meet exact weighting, ten-domain balance, and final-button contract');
// A learner who answers every L1 and L2 correctly, misses every L3, reaches exactly 80%.
t.createExam('full',null,20);let ex=t.S().activeExam;
for(let rec of ex.items){const q=QMAP[rec.id];ex.answers[rec.id]=t.levelOf(q)===3?q.options.find(x=>x!==q.answer):q.answer;}
t.submitExam();let scored=t.S().exams.at(-1);
pass(scored.score===16&&scored.percent===80&&scored.passed,'L1+L2 correct, all L3 wrong yields 80% pass');
pass(scored.levels[0].correct===6&&scored.levels[1].correct===10&&scored.levels[2].correct===0,'correct level breakdown saved');
pass(app.innerHTML.includes('Mastery by difficulty')&&app.innerHTML.includes('TARGETED NEXT STEPS'),'results show level mastery and linked remediation');
pass(t.S().doneTopics['stack:0']===true,'old learner state preserved after scored exam');
// 100% requires successful Level 3 cases as well.
t.createExam('full',null,30);ex=t.S().activeExam;
for(let rec of ex.items)ex.answers[rec.id]=QMAP[rec.id].answer;
t.submitExam();scored=t.S().exams.at(-1);
pass(scored.score===30&&scored.percent===100&&scored.levels[2].correct===6,'100% requires correct L3 selections');
// Guided session uses all 10 domains and offers a learning-panel even when correct.
t.UI.screen='assessment';t.startGuided();let g=t.UI.guided;
pass(g.items.length===10&&new Set(g.items.map(x=>QMAP[x.id].module)).size===10,'guided cross-domain exercise covers all modules');
pass([1,2,3].every(l=>g.items.some(x=>t.levelOf(QMAP[x.id])===l)),'guided challenge includes all three difficulty levels');
let id=g.items[g.index].id;g.answers[id]=QMAP[id].answer;t.render();
pass(app.innerHTML.includes('Learn beyond the answer')&&app.innerHTML.includes('Why the other options do not fit'),'guided post-answer learning/alternative review');
t.UI.guided=null;
// Each engineering clinic is browsable with three questions and persistent answers; retake is safe.
t.UI.mod='tools';t.UI.tab='clinic';t.UI.screen='learn';t.render();
pass(app.innerHTML.includes('48 tools, lower success')&&app.innerHTML.includes('94%')&&app.innerHTML.includes('99%'),'engineering clinic renders its evidence table');
const c=data.clinics.find(x=>x.id==='tools');for(let i=0;i<3;i++)t.clinicRecord('tools').answers[i]=c.steps[i].answer;
t.S().clinics.tools.answers={...t.clinicRecord('tools').answers};t.render();
pass(app.innerHTML.includes('3/3 stages explored')&&app.innerHTML.includes('Why the other options do not fit'),'three-step clinical reasoning feedback and progress');
pass(JSON.parse(store['ai-systems-academy-v1']).doneTopics['stack:0']===true,'progress storage remains compatible');
t.UI.screen='casebook';t.render();pass(app.innerHTML.includes('10 ENGINEERING CLINICS'),'global casebook routes exist');
t.UI.screen='progress';t.render();pass(app.innerHTML.includes('Clinic stages')&&app.innerHTML.includes('3/3 decisions'),'engineering-clinic attempts visible alongside legacy progress');
console.log('ACADEMY_V2_LOGIC_REGRESSION=PASS');
