"""Optional shareable brief. Requires ReportLab, Pillow and pypdf; core models do not.
Run from the packet root: python3 surfaces/build_brief.py
"""
from pathlib import Path
import reportlab
from reportlab import rl_config
import hashlib
import json
import io
import pypdf
rl_config.invariant = 1
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image

PACKET=Path(__file__).resolve().parents[1]
OUT=PACKET/'results/mcrp-release-brief.pdf'
FONT_LICENSE=PACKET/'publication/notices/bitstream-vera-license.txt'
fontdir=Path(reportlab.__file__).parent/'fonts'
for name,file in [('Vera','Vera.ttf'),('Vera-Bold','VeraBd.ttf'),('Vera-Italic','VeraIt.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
pdfmetrics.registerFontFamily('Vera',normal='Vera',bold='Vera-Bold',italic='Vera-Italic',boldItalic='Vera-Bold')
INK=colors.HexColor('#183338');TEAL=colors.HexColor('#007e82');MUTED=colors.HexColor('#536b70');PAPER=colors.HexColor('#f4f5ef')
styles={
 'title':ParagraphStyle('title',fontName='Vera-Bold',fontSize=30,leading=35,textColor=INK,spaceAfter=20),
 'h1':ParagraphStyle('h1',fontName='Vera-Bold',fontSize=22,leading=27,textColor=INK,spaceAfter=18),
 'h2':ParagraphStyle('h2',fontName='Vera-Bold',fontSize=12,leading=17,textColor=TEAL,spaceBefore=14,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Vera',fontSize=9.5,leading=14,textColor=INK,spaceAfter=10),
 'small':ParagraphStyle('small',fontName='Vera',fontSize=8.3,leading=12,textColor=MUTED,spaceAfter=8),
 'eyebrow':ParagraphStyle('eyebrow',fontName='Vera-Bold',fontSize=9,leading=13,textColor=TEAL,spaceAfter=16),
 'cell':ParagraphStyle('cell',fontName='Vera',fontSize=9,leading=13,textColor=INK),
}
story=[]
def p(text,kind='body'):story.append(Paragraph(text,styles[kind]))
def h(text):p(text,'h2')
def page(kicker,title):
 if story:story.append(PageBreak())
 p(kicker.upper(),'eyebrow');p(title,'h1')
def table(rows,widths):
 t=Table([[Paragraph(str(v),styles['cell']) for v in row] for row in rows],colWidths=widths,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4efea')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#c2ceca'))]))
 story.extend([t,Spacer(1,12)])
def footer(c,d):
 c.setStrokeColor(colors.HexColor('#c2ceca'));c.line(46,43,566,43)
 c.setFont('Vera',8);c.setFillColor(MUTED);c.drawString(46,29,'MCRP  /  Research prototype  /  25 September 2026');c.drawRightString(566,29,str(d.page))

p('MCRP / PUBLIC-PROTOTYPE RELEASE CANDIDATE','eyebrow')
p('What can we rely on?', 'title')
p('A small protocol for claims that can be checked, used and repaired.','h1')
p('The Minimum Credible Reproducibility Protocol connects a versioned claim, the work actually performed to check it, and an accountable decision to use it. A material change makes affected uses visible for reconsideration.')
h('Recommendation: release a protocol seed')
p('The research prototype is suitable for public discussion after the exact artifact, responsible attribution, rights and destination are settled. Its contribution is an inspectable interface, conditional mathematics, runnable synthetic examples and documented counterexamples. It does not need to be a complete review institution to be useful.')
p('Existing provenance, research packages and versioned review already supply much of the machinery. The proposed increment is a testable profile for preserving scoped uses and repair commitments across systems.', 'small')
table([['Action','Small record'],['<b>Offer</b>','One claim, its version, evidence and limits.'],['<b>Check</b>','What was examined, by which method, with what result and uncertainty.'],['<b>Rely</b>','A responsible decision for a bounded use of that version.'],['<b>Amend</b>','A material change and the uses that need reconsideration.']],[80,440])
p('These are actions, not rank levels or mandatory sequential stages. A solo author, a collaboration and a large agent team can expose the same boundary while retaining different internal workflows.','small')
p('The embedded font license is attached to this PDF and retained in the accompanying packet.', 'small')
p('<b>Status:</b> prepared research candidate; not publicly deployed or licensed. Substantial AI drafting, coding and internal adversarial review under one operator. No external peer review, human efficacy study or operational certification.','small')

page('01 / Mathematical foundations','Useful guarantees have named premises')
h('A label is not an independent reviewer')
p('Three declared groups compete for two seats. Group A has n interchangeable labels; B and C each have one. Uniform feasible representative selection gives A a seat with probability 2n/(2n+1). Selecting a group panel first gives 2/3. At n = 100 these are 99.5% and 66.7%.')
p('The exact invariance result assumes correct, fixed control groups and unchanged eligibility. It is not identity discovery or a guarantee about completed reviews.')
h('Completion changes the denominator')
p('If an adverse offer has frequency e and completion probability 1, while other offers complete with probability c, its share among completions is e / [e + (1 - e)c]. At e = .1 and c = .01, that is 91.7%. All refused and unresolved requests must remain in the accounting.')
h('A hard budget is stronger than an expected budget')
p('For N identical-cost audit opportunities, cost a and budget B, a pathwise quota is k = floor(B/a). Blinded fixed-size or adjacent-size sampling can support marginal audit probability q only with q &lt;= k/N. The incentive lower bound and participation upper bound must intersect this funded range. Concealment, detection and enforceable loss remain assumptions.')
p('Exact rational endpoints govern the implementation. For a singleton interval [5/6, 5/6], convenience floating displays must not decide feasibility.')
p('A companion model actually executes funded inspections and token transfers for a fixed offered population. Concealed selection supports the stated marginal; revealing selected slots early leaves unaudited actors choosing shallow work. Increasing false sanctions can make every actor refuse. These are conditional toy behaviors, not a cooperation equilibrium. See manuscripts/funded-audits.md.')
h('Stable snapshots do not guarantee stable repair')
p('Two repair maps can each have spectral radius zero yet double work when alternated. A common positive weighted contraction condition can bound cumulative expected repair under stated conditional assumptions. Average snapshots cannot substitute for that common condition.')
p('<b>Evidence:</b> self-contained proofs, independent finite oracles, 115 retained sweep rows and 80,000 Monte Carlo requests. These characterize mathematical and synthetic models, not scientific communities. Full derivations: manuscripts/math-foundations.md.','small')

page('02 / Coupled toy agents','Follow selection through the whole lifecycle')
p('The coupled model charges intake, invitations, checking, reliance and repair against one shared person ledger. Agents choose among stipulated honest, shallow and refusal options with heterogeneous costs. Perceived auditing is an exogenous belief; the model does not deliver or fund those audits.')
from PIL import Image as PILImage
figure_path=PACKET/'results/figures/selection-through-stages.png'
with PILImage.open(figure_path) as bitmap: w,h_px=bitmap.size
im=Image(str(figure_path),width=500,height=500*h_px/w);story.append(im);story.append(Spacer(1,8))
p('Figure: pooled shares across 100 synthetic replicates per policy, 12 requests each. Group A has 100 labels; reroll retries and 20 hours per person are stipulated. These are stage denominators, not independent human observations.','small')
h('What the joined model exposes')
p('Group-first selection removes this label-multiplicity advantage at invitation. Capacity and completion can still change the distribution. An A-only reliance rule makes A appear in every relied-on panel. Repair work does not automatically renew a reliance decision.')
p('The sweep retains 7,400 runs over 74 scenarios. Hidden dependency tracking uses a simulation oracle, not real-world discovery.')
p('The coupled simulation and receipt runtime are separate engines; their guarantees do not automatically compose. Full model: manuscripts/coupled-agents.md.','small')

page('03 / Recognition and cooperation','Keep the tradeoffs and the gaming example')
p('A small ecology compares uniform routing, cumulative prestige and capped recognition with exploratory access. All use shared integer effort and persistent correction work. Defects and diligence are stipulated; these agents do not learn human norms or choose their defect rates.')
table([['Overload: seed means','Uniform','Bounded credit','Prestige'],['Least-served group coverage','.486','.613','.552'],['Correct checks / all offers','.687','.682','.693'],['Recognized repair debt','15.50','19.75','31.00']],[238,94,94,94])
p('Eight seeds per policy; 80 periods. Full ecology: 216 retained runs over nine regimes. Bounded credit improves one coverage measure while slightly reducing correct checks per offer relative to uniform. There is no dominating policy in this comparison.','small')
h('Manufactured corrections can become profitable')
p('A separate one-step game uses the actual bounded score update. The author compares clean work with creating a correctable defect and obtaining repair. Private gain equals the attention benefit minus manufacture cost, the internalized repair cost and expected enforceable loss.')
table([['Correction allocation credit','Author gain','Coalition gain'],['Author and repairer','+7.27','+17.54'],['Repairer only','-19.11','+13.11'],['No correction priority credit','-3.00','-3.00']],[292,114,114])
p('Illustrative assumptions: three groups, no clean-work credit, 20 available repair tokens, attention value 100, and 90% of repair cost externalized. Each manufactured repair adds a social-cost proxy of 26. This is a two-action counterexample, not a repeated-game equilibrium or recommendation to punish genuine corrections.','small')
h('A quiet queue can hide failure')
p('With shared blindness, fewer than half of offered defects are found in the retained ecology cases, while correct checks per offer stay above .85 because most offers are nondefective. Low repair debt can reflect missed problems. Full analysis: manuscripts/local-rules.md.')

page('04 / Science cases','The same record must carry different scientific limits')
h('Physics and astronomy: common calibration')
p('Two pipelines can reproduce an estimate while sharing the same uncertain calibration. Agreement is useful, but it does not remove the common error. The worked case separates independent noise from the shared calibration term; averaging more pipelines cannot eliminate that variance floor.')
p('<b>Exercise:</b> record a numerical reproduction check, then change the calibration evidence. Identify which downstream estimate and population-analysis use needs reconsideration. A missing dependency edge is an explicit negative control: the runtime cannot propagate along a path it was never told about.')
p('<b>Useful contribution:</b> one synthetic calibration update, a declared dependency graph, the old scoped decision and the renewed decision after new checks. Do not substitute a passing numerical test for an astrophysical interpretation.')
h('Biology: reproduction versus identification')
p('A batch-confounded contrast can reproduce exactly and still fail to identify a treatment effect. The case exhibits an observationally equivalent countermodel with zero causal effect. A crossed design can identify an additive-model contrast under conditional exogeneity; that premise must be stated.')
p('<b>Exercise:</b> contrast differences of 1 and 3 have average 2, but they do not fit a common exact additive effect. The oracle reports the average, marks exact additivity false and leaves the exact additive coefficient null. A supported receipt is scoped to the calculation it actually establishes.')
p('<b>Useful contribution:</b> a counterexample that changes the scientific interpretation without breaking the rerun. A well-formed record should keep the unsupported causal use visible rather than make the model seem more authoritative.')
h('What both groups can contribute immediately')
p('Use shareable synthetic examples first. A domain expert can add one missing assumption in plain language. An agent can generate the paired input/output and replay the actual toy receipt sequence. Neither needs to join a new credentialing institution.')
p('Full worked cases, primary-source links and executable oracles: domains/physics-astro.md and domains/biology.md. No real astronomy result, biological discovery or clinical claim is reported.','small')

page('05 / Economics and law','Capacity, incentives and authority remain distinct')
h('Economics and social science: selection after selection')
p('A sample of successful reviews is selected twice: some invited work completes, then some completed work is relied upon. The case makes those denominators explicit and separates reproducibility, causal assumptions and transport to another population.')
p('<b>Exercise:</b> start with a 10% adverse offered share. Change completion behavior, then introduce a selective reliance policy. Report the offered, completed, relied and unresolved populations. An apparently fair invitation mechanism can coexist with concentrated final influence.')
p('<b>Useful contribution:</b> identify the scarce resource, specify the outside option and utility assumptions, and compare a simpler allocation baseline at equal total labor. Preserve the cases where the proposed mechanism loses.')
h('Law: a checked source is not a grant of authority')
p('A quotation can be accurate while a proposed operational decision remains unsupported. The legal case separates records, evidentiary uses, appointed decision makers and actual obligations. Its federal evidence discussion is limited to covered federal proceedings; it does not generalize to every jurisdiction.')
p('<b>Exercise:</b> a fictional set of obligations fits the total labor budget but misses a deadline because the appropriate person is unavailable when needed. A sum-of-hours invariant cannot prove deadline feasibility or legal compliance.')
p('<b>Useful contribution:</b> one precise boundary between checking a citation and making a legally consequential decision. Keep jurisdiction, authority and procedural requirements explicit. The toy registry supplies fictional roles; it does not appoint anyone.')
h('Publishing the research is a smaller step than operating a service')
p('A static research artifact can be publicly discussed before a complete dispute institution exists. Accepting real sensitive evidence, adjudicating third-party disputes or promising operational remedies would introduce responsibilities this packet has not implemented.')
p('Full cases, scope limits and primary sources: domains/economics-social-science.md and domains/law.md. These are synthetic teaching examples, not legal advice or an empirical evaluation of institutions.','small')

page('06 / Two entry paths','A sentence for humans. A counterexample for agents.')
h('Human path: begin alone, with one claim')
p('Choose a domain microtask. Write one sentence stating what the example supports and one thing it does not. Then fill a small card: claim/version, evidence, performed check, responsible intended use, uncertainty and material change trigger. A colleague is helpful for the later paired exercise, not required to begin.')
p('The packet offers a ten-minute entry, a paired exercise and a facilitated clinic. A minimum contribution has only three fields: the example, what was difficult or failed, and a suggested next step. Acknowledgment is not a rank or authority credential.')
h('Agent path: run, alter, preserve the failure')
p('Run <b>python3 run_checks.py</b> from the extracted packet root. Change one control-group declaration, capacity limit, target version or dependency. Preserve expected and actual outcomes, assumptions, seed and all offered-work denominators. The core models require only Python and its standard library.')
h('A bridge from ordinary review metadata')
p('The executable legacy adapter preserves the original synthetic review payload and distinguishes absent, null and explicitly empty values. A recommendation to accept does not become a positive check or an authority grant. Unaugmented metadata is refused for scoped reliance.')
p('A separately retained fictional enrichment supplies control, capacity and authority assertions for the demonstration. The adapter then exercises the actual toy runtime; amendment makes the old reliance pending. It does not authenticate the review or claim standards conformance.')
h('Test the interface before adding machinery')
p('Compare the four-action card with an ordinary structured template on matched synthetic amendment tasks. Count participant time, facilitation, refusals and unfinished work. Keep teaching clinics separate from any planned study. Human benefit remains an unanswered question; passing agent tests cannot answer it.')
p('Entry points: onboarding/human-path.md, onboarding/agent-path.md, onboarding/legacy-adapter.md and onboarding/facilitator-guide.md.','small')

page('07 / Release and dissemination','Launch a concrete invitation to improve the protocol')
h('Keep the adversarial record visible')
p('Separate internal lanes challenged mathematics, runtime semantics and domain/legal claims. Their findings changed the prototype: mismatched publication observations, stale contradictions, uncounted unresolved work, audit-budget endpoints, export leftovers, source symlinks, archive mismatches and the legacy Boolean/integer bypass were repaired or narrowed. Remaining counterexamples are retained.')
p('This is internal AI adversarial review under a shared operator, not independent human peer review. Exact test counts, source/result hashes and final export status belong to the accompanying machine-readable validation and release record.')
h('A practical launch sequence')
table([['Surface','First useful invitation'],['Project page + versioned download','Read the introduction, reproduce one case, report one failure.'],['Physics / astronomy and biology clinics','Bring a calibration dependency or identification counterexample.'],['Economics / social-science seminar','Compare allocation and correction incentives at equal labor.'],['Law and legal-informatics discussion','Separate citation checks, decisions, obligations and amendment.'],['Open-research communities','Explore fit with RDA and FORCE11; seek editorial agreement rather than presume placement.']],[190,330])
p('A Zenodo-style versioned archive is a plausible later deposit surface; no DOI or submission is claimed. arXiv requires a suitable refereeable manuscript and moderation. The present AI-heavy packet should not be uploaded to OSF Preprints under its <link href="https://help.osf.io/article/691-preprint-moderation-policies" color="#007e82">current moderation policy</link>. Venue fit and permissions must be checked for the actual later submission.','small')
h('The final release decision')
p('Set the responsible human attribution, adopt rights terms for the approved inventory, choose the destination and identify a realistic feedback owner. Proposed terms are CC BY 4.0 for newly prepared prose/figures and MIT for original code, subject to rights-holder confirmation. No license has been granted by this draft.')
p('<b>First public ask:</b> try one synthetic claim, make one material change, and report one failure or unnecessary step. The goal is to seed a protocol that earns elaboration through use.','body')
p('Source and policy details: publication/release-assessment.md, publication/dissemination.md, publication/SOURCE_CHECKS.md, reviews/COLLECTIVE.md. Read the accompanying local index.html for linked manuscripts, figures and executable evidence.','small')

OUT.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(OUT),pagesize=(612,792),rightMargin=46,leftMargin=46,topMargin=44,bottomMargin=57,title='MCRP: What can we rely on?',author='AI-assisted research prototype; responsible human attribution pending',subject='Public-prototype release brief, 25 September 2026')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=pypdf.PdfReader(io.BytesIO(OUT.read_bytes()))
writer=pypdf.PdfWriter();writer.clone_document_from_reader(reader)
writer.add_attachment("bitstream-vera-license.txt",FONT_LICENSE.read_bytes())
with OUT.open("wb") as stream:writer.write(stream)
manifest={"schema":"mcrp.brief-evidence.v1", "reportlab":reportlab.Version, "pypdf":pypdf.__version__,
          "inputs":{str(p.relative_to(PACKET)):hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [Path(__file__),figure_path,FONT_LICENSE]},
          "artifacts":{str(OUT.relative_to(PACKET)):hashlib.sha256(OUT.read_bytes()).hexdigest()},
          "scope":"Human-readable synthesis; fixed PDF metadata for reproducibility; claims derive from named packet sources"}
(OUT.parent/'brief-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({"artifact":str(OUT.relative_to(PACKET)),"sha256":manifest["artifacts"][str(OUT.relative_to(PACKET))]}))
