# Agent uptake theory pass

Three complementary toy models examine what could make a protocol useful before widespread uptake and what repeated agent reviews cannot establish.

- [Adoption](adoption/MANUSCRIPT.md): standalone benefit, network externalities, seed withdrawal, and limits of synchronous coordination.
- [Adversarial review](adversarial/manuscript.md): shared-error floors, indistinguishability, method-family allocation and review shopping.
- [Decision-value bridge](integration/MANUSCRIPT.md): detection gains, false alarms, prevalence, costs and exact rectangular uncertainty bounds.

These are mathematical examples, not calibrated predictions. The two specialist agents reviewed each other's lane; reports are retained beside the manuscripts. All agents operated under one orchestration. This is internal adversarial checking, not independent scientific review.

Run from this directory:

```sh
python3 -m unittest discover -s adoption -p 'test_*.py' -v
python3 -m unittest discover -s adversarial -p 'test_*.py' -v
python3 -m unittest discover -s integration -p 'test_*.py' -v
```

Prose in this directory is offered under CC BY 4.0; code under MIT, using the MIT text in ../07-release-packet/LICENSES/MIT.txt and the CC BY 4.0 terms at https://creativecommons.org/licenses/by/4.0/. This scoped grant does not change licenses elsewhere. The frozen v0.1.0 release remains unchanged.
