# Qualified gravitational-wave scientific review form

This form is deliberately unsigned. It prepares, but does not simulate, the
separate human-scientific review required by `review-signoff.json`. Review the
exact case commit, `scientific-review-dossier.json`, the cited sources, and the
machine evidence before recording a disposition.

## Reviewer and scope

- Reviewer name:
- Affiliation or independent capacity:
- Relevant GW strain/data-quality expertise:
- Conflicts, prior involvement, and shared implementation/data dependencies:
- Exact Git commit reviewed:
- Date:

An incomplete qualification or conflict declaration is a reason to return the
packet without a scientific disposition. Execution competence alone is not GW
domain authority.

## Required determinations

For each item, choose **accept**, **accept with required change**, or **reject**;
cite the inspected artifact/source and explain the scientific reason.

1. **Filter path (HD-01).** Is the declared fourth-order 35--350 Hz
   forward--backward Butterworth filter, without whitening or line notches,
   acceptable for this bounded demonstration? The discovery paper uses the same
   band edges for a visualization but also uses line-rejection filters. The LVC
   data guide uses whitening, a taper, and an eighth-order zero-phase filter and
   labels the narrow passband visualization-only. These are context, not
   validation of this implementation.
2. **Window geometry (HD-02).** Is the 820-sample (0.2001953125 s) window centered
   at GPS 1126259462.4 adequate and non-misleading? The published signal lasts
   about 0.2 s, while the LVC data guide shows that correlation changes with
   window duration and placement. The exact local window is a registered protocol
   choice and should be tested for sensitivity if the candidate conclusion needs
   it.
3. **Quality and injections (HD-03).** Do DATA, CBC_CAT1/2, BURST_CAT1/2,
   NO_CBC_HW_INJ, and NO_BURST_HW_INJ support only the stated event-time
   preprocessing scope? Passing public bits is not fresh calibration,
   environmental, or detector-characterization review.
4. **Lag and sign convention (HD-04).** Are the lag sign, detector-orientation
   inversion context, and use of maximum absolute normalized correlation disclosed
   sufficiently? Explain whether any code or prose change is required.
5. **Decision rules (HD-05).** Is 10 ms used only as a necessary intersite
   propagation bound? Is the 0.30 absolute-correlation floor clearly a registered
   local threshold rather than a literature-derived detection statistic?
6. **Boundaries and conclusion (HD-06).** Are the accepted external tools,
   calibration/data products, exclusions, and strongest candidate conclusion
   complete and proportionate?

## Overall disposition

- [ ] Accept the strongest candidate conclusion exactly as stated.
- [ ] Accept only after the required changes below are made and independently
      verified.
- [ ] Reject; the packet cannot support the candidate conclusion.

Required changes or rejection reasons:

Evidence inspected and source locators:

Residual uncertainties:

Strongest warranted conclusion after review:

Explicitly unwarranted conclusions after review:

Signature or verifiable approval reference:

The completed form must be attached without overwriting this blank template. A
machine or agent may check presence, scope, and consistency, but may not fill the
scientific disposition or convert silence into approval.
