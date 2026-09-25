---
layout: post
published: false
ai_generated: true
categories: [research, reproducibility]
publication_lane: ai-research-infrastructure
related_posts: false
title: "What can we rely on? A small protocol for science that can be checked and repaired"
description: "Introducing an MCRP research prototype: four actions, executable examples, and an invitation to try to break it."
date: 2026-09-25
author: "Codex (AI agent; responsible human attribution pending)"
status: "Editorial draft for a public research-prototype launch"
---

# What can we rely on?

*A small protocol for science that can be checked and repaired.*

A paper changes. A calibration is corrected. An analysis is rerun with a different
sample. A reviewer’s careful answer still exists—but it answers a question about
an earlier version. Someone downstream needs to know whether that answer still
supports what they want to do.

That is the problem behind the **Minimum Credible Reproducibility Protocol**, or
**MCRP**. We are developing a small way to connect a claim, its evidence, the checks
actually performed, and a decision to rely on it. Each record has a version. Each
decision has a scope. When something material changes, affected uses become
visible for reconsideration.

The aim of this prototype is to seed a protocol that people can try, criticize,
and adapt. Its value will depend on whether it helps real work. The release
candidate contains mathematical models, runnable toy agents, and worked examples;
it has not demonstrated improved scientific judgment or lower human workload.

## Four actions are enough to start

**Offer.** State one claim and identify the evidence for it. Say what a useful
check would cover and what remains outside the claim. An ordinary paper, notebook,
data release or referee letter can be the starting point.

**Check.** Record a particular examination of that offer. Did a calculation
reproduce? Was a sensitivity analysis performed? Was the cited authority current?
Report the result and the limits. A check can find a defect without settling the
whole scientific question.

**Rely.** Record a scoped decision: this person or institution will use this
version for this purpose, under these conditions. Permission to publish, a test
passing, and scientific acceptance remain distinct. Different communities may
reasonably reach different decisions from the same record.

**Amend.** Identify a material change and the uses it may affect. Preserve what
the earlier decision meant while making its present limitations clear. A later
decision can renew reliance after the necessary work.

These are actions people can take in different orders. A challenge can arrive
before a review, checks can happen in parallel, and one group’s reliance need not
wait for everyone else’s agreement.

## A calibration change should travel farther than an email

Imagine an astronomy collaboration releasing an estimate from a calibrated
instrument. One reviewer verifies the numerical workflow. Another examines the
calibration assumption. A downstream group uses the estimate in a population
analysis.

If the calibration changes, “the code still passes” is an incomplete answer. The
changed dependency may reach both the estimate and the population analysis. An
MCRP record makes that declared path explicit. It asks the downstream group to
reconsider its own use; it does not let an automated notice decide the astrophysics.
Undeclared dependencies remain a blind spot. That limitation belongs in the record.

The same pattern has different meanings elsewhere. In biology, repeated assays
may share a batch effect, so several agreeing runs need not supply independent
evidence. In economics, successful reproduction does not establish a causal
identification assumption or justify transport to another population. In law, an
accurate quotation does not settle the authority of a decision in another
jurisdiction. The prototype includes separate cases because these differences
matter.

## A person and a thousand-agent team can expose the same boundary

The interface should not require participants to reveal or standardize their
entire internal workflow. A solo researcher can contribute one useful check. A
large collaboration can attach its existing review procedure. An agent team can
produce a machine-readable record and a rerunnable experiment.

They still have to answer the same external questions: what was checked, for
which version, by whom or under whose responsibility, with which dependencies,
and what might invalidate the intended use? A thousand agents controlled by one
operator do not become a thousand independent reviewers.

For humans, the first exercise fits on one page. For implementers, the same
exercise has records and executable policies. The two paths meet at a shared
example rather than at a large mandatory rulebook.

## The scarce resource is attention—including attention after publication

Review costs time. So do onboarding, disputed decisions, auditing and repair.
A protocol that promises all of them without accounting for shared people can
overcommit its most important resource.

Our models deliberately include failures. Duplicating reviewer labels can bias
an apparently random assignment. Conditioning only on completed reviews can
hide selective refusal. A repair workload can fit the total budget and still
overload one specialty. These are reasons to track final assignments, unfinished
work and skill-specific capacity, rather than infer success from a single score.

The initial baseline is simple: qualified, conflict-aware assignment with declared
limits. More elaborate routing has to show that its benefits justify its cost.
If a plain structured review template performs as well with less labor, that is
a useful result for this project.

## Build on the records people already use

Provenance, research packages, versioned reviews and scholarly notifications
already exist. MCRP should use them. The proposed contribution is a small shared
profile that preserves the intended use, limits and repair commitments when a
record moves between systems. If an existing workflow already carries those
facts well, a faithful adapter - or no extra layer - may be the right answer.
The [comparison with existing infrastructure](positioning-and-adoption.md)
explains the overlap and the adoption claims still to be tested.

## Try one claim; bring one counterexample

You do not need to adopt a new institution to participate. Choose one of the
synthetic domain cases. Write an offer, carry out a bounded check, record an
appropriate reliance decision, then introduce a change. Notice which assumptions
were difficult to express and which work someone had to do.

If you write software, run the toy agents, alter a policy, and compare the result
with its baseline. A useful contribution includes the failing example, expected
behavior, actual behavior and the smallest repair you can defend. A refusal,
unknown state or unresolved disagreement may be the correct output.

The most valuable early response is a concrete case the framework handles badly:
an expensive form, an unrepresentable judgment, a missing dependency, a fairness
claim defeated by an adversary, or an operational obligation the model forgot.
That gives us something precise to improve together.

**Contribution disclosure.** This introduction and the accompanying release
candidate were drafted and revised by AI agents at the researcher's request.
Separate agent lanes developed the models and challenged their claims; they
share an operator and are not external peer review. Numerical results concern
synthetic models. Responsible human attribution, editorial approval of the exact
public artifact, licensing and live publication are pending.

**Start here:** [try the human exercise](../onboarding/human-path.md),
[run the toy agents](../onboarding/agent-path.md), explore the
[four domain cases](../domains/README.md), or read the
[collective red-team report](../reviews/COLLECTIVE.md). These links refer to this
prepared candidate; no public archive URL or DOI is claimed.
