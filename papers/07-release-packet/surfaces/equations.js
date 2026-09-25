/* Exact formulas for the deliberately restricted interactive examples.
 * No data collection, network calls, operational decisions or toy-agent execution.
 */
(function (root) {
  "use strict";
  function probability(x) {
    if (!Number.isFinite(x) || x < 0 || x > 1) throw new Error("Probability outside [0,1]");
    return x;
  }
  function clones(n) {
    if (!Number.isInteger(n) || n < 1) throw new Error("Positive integer copies required");
    return { representativeFirst: 2 * n / (2 * n + 1), groupFirst: 2 / 3 };
  }
  function completion(epsilon, adverse, other) {
    [epsilon, adverse, other].forEach(probability);
    const completed = epsilon * adverse + (1 - epsilon) * other;
    return { offered: epsilon, completed: completed,
      adverseAmongCompleted: completed === 0 ? null : epsilon * adverse / completed,
      unresolved: 1 - completed };
  }
  function repair(multiplier, generations) {
    if (!Number.isFinite(multiplier) || multiplier < 0 || !Number.isInteger(generations) || generations < 0 || generations > 30)
      throw new Error("Invalid repair example input");
    let tasks = 1, total = 1;
    for (let i = 0; i < generations; i++) { tasks *= multiplier; total += tasks; }
    return { lastGeneration: tasks, cumulative: total };
  }
  const api = { clones, completion, repair };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.MCRPEquations = api;
})(typeof window !== "undefined" ? window : globalThis);
