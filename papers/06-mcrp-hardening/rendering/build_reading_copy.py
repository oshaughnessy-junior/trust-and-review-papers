"""User-facing reading copies; requires bundled reportlab and local pandoc."""
from pathlib import Path
import csv, json, subprocess, sys
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.graphics.shapes import Drawing, String, Line, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderSVG

HERE=Path(__file__).resolve().parents[1]
DOSSIER=HERE
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else HERE/'build'
OUT.mkdir(parents=True,exist_ok=True)
WORK=HERE/'build/render-work';WORK.mkdir(parents=True,exist_ok=True)
FIG=DOSSIER/'results/figures';FIG.mkdir(exist_ok=True)
sys.path.insert(0,str(DOSSIER/'models'))
from dynamics import imported_mass

NAVY=colors.HexColor('#142c43');TEAL=colors.HexColor('#007f80');CORAL=colors.HexColor('#c0583d')
MUTED=colors.HexColor('#526475');PALE=colors.HexColor('#edf3f5')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleX',fontName='Helvetica-Bold',fontSize=29,leading=33,textColor=NAVY,spaceAfter=16))
styles.add(ParagraphStyle(name='SubX',fontName='Helvetica',fontSize=13,leading=18,textColor=MUTED,spaceAfter=14))
styles.add(ParagraphStyle(name='H1X',fontName='Helvetica-Bold',fontSize=19,leading=23,textColor=NAVY,spaceAfter=13))
styles.add(ParagraphStyle(name='H2X',fontName='Helvetica-Bold',fontSize=12,leading=16,textColor=TEAL,spaceBefore=10,spaceAfter=6))
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=10,leading=14,textColor=NAVY,spaceAfter=9))
styles.add(ParagraphStyle(name='SmallX',fontName='Helvetica',fontSize=8.5,leading=11.5,textColor=MUTED,spaceAfter=6))
styles.add(ParagraphStyle(name='CellX',fontName='Helvetica',fontSize=9,leading=12,textColor=NAVY))

def p(text,style='BodyX'):return Paragraph(text,styles[style])
def table(rows,widths):
    t=Table([[p(x,'CellX') for x in row] for row in rows],colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),PALE),
        ('LINEBELOW',(0,0),(-1,0),.7,TEAL),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#d9e2e7')),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
    return t

def influence_chart():
    d=Drawing(500,190)
    d.add(String(0,177,'A graph bound needs a normalized probability cap',fontName='Helvetica-Bold',fontSize=11,fillColor=NAVY))
    lp=LinePlot();lp.x=43;lp.y=32;lp.width=420;lp.height=125
    lp.data=[[(i/1000,imported_mass(a,i/1000)) for i in range(151)] for a in [.5,.85,.95]]
    lp.xValueAxis.valueMin=0;lp.xValueAxis.valueMax=.15;lp.xValueAxis.valueSteps=[0,.05,.1,.15]
    lp.yValueAxis.valueMin=0;lp.yValueAxis.valueMax=.8;lp.yValueAxis.valueSteps=[0,.2,.4,.6,.8]
    lp.xValueAxis.labels.fontSize=8;lp.yValueAxis.labels.fontSize=8
    for i,c in enumerate([TEAL,NAVY,CORAL]):lp.lines[i].strokeColor=c;lp.lines[i].strokeWidth=1.8
    d.add(lp)
    d.add(String(123,9,'Maximum normalized ingress probability',fontSize=9,fillColor=MUTED))
    for i,(a,c) in enumerate(zip([.5,.85,.95],[TEAL,NAVY,CORAL])):
        d.add(Line(305+i*62,169,317+i*62,169,strokeColor=c,strokeWidth=2))
        d.add(String(320+i*62,166,str(a),fontSize=8,fillColor=MUTED))
    d.add(String(43,159,'External stationary mass; legend = restart-walk alpha',fontSize=8,fillColor=MUTED))
    return d

def allocation_chart():
    r=json.loads((DOSSIER/'results/economics/results.json').read_text())
    cases=['known','noise_05','noise_10','noise_20']
    vals=[next(x for x in r['allocation_summary'] if x['scenario']==c and x['hours']==80 and x['policy']=='estimated_waterfill')['paired_gain_vs_uniform'] for c in cases]
    d=Drawing(500,190)
    d.add(String(0,177,'Optimizing the wrong priorities can lose to uniform effort',fontName='Helvetica-Bold',fontSize=11,fillColor=NAVY))
    x0,y0,w,h=44,30,415,126;low,high=-30,30
    yy=lambda v:y0+(v-low)/(high-low)*h
    for tick in [-30,-15,0,15,30]:
        d.add(Line(x0,yy(tick),x0+w,yy(tick),strokeColor=colors.HexColor('#dfe7eb'),strokeWidth=.5))
        d.add(String(17,yy(tick)-3,str(tick),fontSize=8,fillColor=MUTED))
    for i,(name,v) in enumerate(zip(['Known','Noise .5','Noise 1','Noise 2'],vals)):
        x=x0+30+i*98;mean,se=v['mean'],v['mc_se']
        d.add(Rect(x,min(yy(0),yy(mean)),40,abs(yy(mean)-yy(0)),fillColor=TEAL if mean>=0 else CORAL,strokeColor=None))
        d.add(Line(x+20,yy(mean-1.96*se),x+20,yy(mean+1.96*se),strokeColor=NAVY,strokeWidth=1))
        for val in [mean-1.96*se,mean+1.96*se]:d.add(Line(x+15,yy(val),x+25,yy(val),strokeColor=NAVY,strokeWidth=1))
        d.add(String(x-2,14,name,fontSize=9,fillColor=MUTED))
    d.add(String(44,159,'Paired gain in synthetic loss units; 80-hour budget',fontSize=8,fillColor=MUTED))
    return d

def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#d9e2e7'));canvas.line(48,42,564,42)
    canvas.setFont('Helvetica',8);canvas.setFillColor(MUTED)
    canvas.drawString(48,29,'MCRP  /  Private research brief  /  25 September 2026')
    canvas.drawRightString(564,29,str(doc.page));canvas.restoreState()

def pdf():
    story=[p('MCRP: bounded reliance','TitleX'),p('A small publication and review protocol, tested against its own failure modes.','SubX'),
        p('RESEARCH POSITION  /  NOT AN OPERATING CERTIFICATE','SmallX'),
        p('The useful promise is precise: <b>for this exact release and this use, these checks were performed; these assumptions remain; this party made the decision; this change would reopen it.</b>'),
        Spacer(1,9),table([['Action','What the participant does'],['<b>Offer</b>','Name an exact claim, evidence boundary, requested check and effort envelope.'],['<b>Check</b>','Record performed work, findings, limits and shared dependencies.'],['<b>Rely</b>','An authorized party states which use it accepts and under which conditions.'],['<b>Amend</b>','Correct, challenge or narrow affected reliance when evidence changes.']],[85,415]),
        p('Simple at the boundary; honest about what lies underneath','H2X'),
        p('The same interface can wrap one person, a large collaboration or an agent team. Internal copies do not create independent authority. Start with qualified, conflict-aware assignment and workload limits. More elaborate trust routing must outperform a simple baseline before earning a role.'),
        p('Four specialist perspectives and four dedicated adversarial reviewers developed and challenged the package. All four adversarial lanes assented to the final <i>limited research conclusion</i>; none certified deployment, legal compliance, human uptake or scientific truth. All agents share the orchestration and operator.'),
        p('Read the full dossier and collective review for derivations, primary sources, retained objections, author responses and executable fixtures.','SmallX'),PageBreak(),
        p('Mathematics that exposes the boundary','H1X'),
        influence_chart(),p('Conditional analytical bound. Raw edge capacity is not normalized ingress: a sole edge of weight 0.001 can normalize to probability 1 and produce external mass 0.85. The curve is not a probability of scientific error.','SmallX'),
        allocation_chart(),p('Exploratory simulation: 30 matched seeds, 80 lots, invented distributions. Bars show mean gain; whiskers are descriptive 1.96 Monte Carlo standard errors. At log-error SD 2, the modeled gain is -22.44 loss units. This is sensitivity evidence, not measured reviewer behavior.','SmallX'),
        p('Two further warnings','H2X'),
        p('<b>Correlated checks:</b> 20 equal-variance reviewers with pairwise correlation 0.2 have variance-equivalent independent count 4.17, not 20. Shared bias remains outside that calculation.'),
        p('<b>Repair bottlenecks:</b> a synthetic workload fits 7.62 total hours into 8 available, but demands 5.08 hours from a specialty with only 4. A stable average can conceal a failing subsystem.'),PageBreak(),
        p('What the collective red team changed','H1X'),
        table([['Objection','Revision or retained limit'],
        ['Graph safety is not assignment safety','Enforce joint final allocation; sample accountable groups before their representatives. Refusals and completion require separate probability boundaries.'],
        ['An old authentic receipt can look current','Separate historical disposition from current reliance. Show stale/unknown, unavailable evidence and unresolved changes; allow authorized renewal.'],
        ['Each discipline spends the same staff hour','Use one skill/person/epoch ledger for review, audit, repair, supervision, rights intake and appeal.'],
        ['Dispute limits can erase the protected route','Pause new commitments while preserving appropriate existing-obligation reporting. Track deadlines and required recipient disclosures.'],
        ['A nominal alternate can be controlled','Require real access, resources, recusal, appointment protections and reversal authority. Otherwise report independence unavailable.'],
        ['Numerical helpers failed valid inputs','Fixed high-budget allocation, zero-productivity and malformed-vector cases. Extreme numeric scales now remain explicit failures, not false allocations.']],[155,345]),
        Spacer(1,10),p('What agreement does not settle','H2X'),
        p('Identity and common control, credible enforcement, true dependency completeness, applicable law, live freshness, privacy, institutional independence and human adoption remain open. The red team retained these as operational gates, not defects to hide in polished prose.'),
        p('The full record preserves 24 dedicated findings, first-round critiques, adverse simulations, peer exchanges and all four final verdicts. Author responses distinguish code repair from specification repair and unresolved empirical claims.','SmallX'),PageBreak(),
        p('A credible next experiment','H1X'),
        p('1  Demonstrate one complete synthetic reliance cycle','H2X'),
        p('Freeze a claim; attach a scoped check; record separately authorized reliance; observe delivered bytes; introduce a material amendment; expose affected uses as pending; resolve them with a new decision. Include failed authorization, stale evidence and inaccessible dependencies.'),
        p('2  Compare the smallest useful interfaces','H2X'),
        p('Use the same tasks and labor budgets for ordinary review, a structured claim/scope template, and the four-action interface. Add trust routing later as a separate factor. Prefer the plain template if it matches utility at lower total cost.'),
        p('3  Count every stage, cost and excluded participant','H2X'),
        p('Report offered, eligible, invited, accepted, completed and relied-upon denominators; include refusals, rerolls, unresolved cases and supervision. Measure scientific scope errors, correction precision/recall, specialist delay and total staff labor. A shorter queue created by rejecting work is a tradeoff.'),
        Spacer(1,10),table([['Delivered evidence','What it establishes'],['25 dossier unit tests + model/counterexample scripts','Selected mathematical and boundary behavior on synthetic inputs.'],['26 reference-tooling unit tests','Bounded traversal, domain, revocation and input-validation regressions.'],['3,591 synthetic table rows','Exploratory parameter sensitivity, including adverse outcomes.'],['Four explicit red-team verdicts','Agreement on a narrowed research claim, not external peer review.']],[220,280]),
        p('Repository and release posture','H2X'),
        p('Working changes belong in the existing private trust-and-review papers and tooling repositories. The public site and hosted Commons remain unchanged. Human authorship, public release, contested pilot participation and legal applicability require their own decisions.'),
        p('Source trail: specialist manuscripts and ledgers; SOURCE_LINEAGE.json; results/validation.json; reviews/COLLECTIVE.md and ADJUDICATION.md. All model quantities shown here are analytical or synthetic.','SmallX')]
    SimpleDocTemplate(str(OUT/'mcrp-hardening-brief.pdf'),pagesize=(612,792),rightMargin=56,leftMargin=56,topMargin=47,bottomMargin=58,title='MCRP: bounded reliance',author='Codex research orchestration').build(story,onFirstPage=footer,onLaterPages=footer)
    for name,d in [('influence-bound',influence_chart()),('allocation-sensitivity',allocation_chart())]:renderSVG.drawToFile(d,str(FIG/(name+'.svg')))

def html():
    css='''body{font-family:Georgia,serif;color:#142c43;line-height:1.6;max-width:1000px;margin:3rem auto;padding:0 2rem}h1,h2,h3,nav{font-family:system-ui,sans-serif}h1{line-height:1.18;margin-top:3rem}h2{color:#007f80;border-top:1px solid #dae3e8;padding-top:1rem}a{color:#006d80}table{font-family:system-ui,sans-serif;font-size:.85rem;border-collapse:collapse;width:100%;display:block;overflow:auto}td,th{padding:.6rem;border:1px solid #dae3e8;vertical-align:top}th{background:#edf3f5}pre{padding:1rem;background:#edf3f5;overflow:auto}math[display="block"]{overflow-x:auto;padding:.8rem 0}#TOC{background:#edf3f5;padding:1rem 2rem;border-radius:8px}#TOC ul{padding-left:1.3rem}p{overflow-wrap:anywhere}@media print{#TOC{page-break-after:always}h1{page-break-before:always}body{font-size:10pt;max-width:none}}'''
    (WORK/'reading.css').write_text(css)
    paths=['SYNTHESIS.md','protocol/minimal-profile.md','manuscripts/economics.md','manuscripts/game-theory.md','manuscripts/legal-operations.md','manuscripts/scientific-dynamics.md','manuscripts/compositional-science.md','manuscripts/frontier-critique.md','reviews/COLLECTIVE.md','reviews/ADJUDICATION.md']
    reviews=['reviews/COLLECTIVE.md','reviews/ADJUDICATION.md']+[f'reviews/red-team/{lane}/{file}' for lane in ['economics','games','science','law'] for file in ['report.md','collective.md','verdict.md']]
    for name,title,items in [('mcrp-research-dossier','MCRP hardening and modeling',paths),('mcrp-collective-red-team','MCRP collective adversarial review',reviews)]:
        source=WORK/(name+'.md')
        source.write_text('\n\n'.join((DOSSIER/f).read_text() for f in items))
        subprocess.run(['pandoc',str(source),'-f','markdown+tex_math_single_backslash+tex_math_dollars','-s','--mathml','--toc','--toc-depth=2','--metadata',f'title={title}','--css',str(WORK/'reading.css'),'--embed-resources','-o',str(OUT/(name+'.html'))],check=True)

if __name__=='__main__':pdf();html();print('Reading copies created')
