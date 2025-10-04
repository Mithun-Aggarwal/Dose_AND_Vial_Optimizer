Code Logic Analysis

The calculator logic does the following:

Inputs captured

Patient weight (kg)

Dose regimen (mg/kg) → either 2.5 or 1.9

Max number of vials allowed (default = 10, adjustable)

Available vial strengths → 70 mg and 100 mg (fixed, no other sizes).

Calculate required dose

Multiply weight × regimen

Round up to the nearest whole mg

This ensures no underdosing.

requiredMg = ceil(weight × regimen)


Enumerate vial combinations

Loop over possible counts of 70 mg vials (x) and 100 mg vials (y).

Constraint: total vials ≤ max vials.

Compute total drug in mg = 70x + 100y.

Discard combinations where total < required (i.e. underdosing not allowed).

Calculate waste

Waste = total – required

Waste% = waste / total.

Rank combinations

Sort primarily by least waste.

If tie → pick fewest vials.

If still tie → smaller total amount.

Mark best option as “Min waste option” (or “Exact match” if waste = 0).

Display results

Show best option as recommendation.

Show up to 4 scenarios:

Best option

“Only 70 mg” option

“Only 100 mg” option

Next best mixed option.

Tie-breaker reminder shown under the table:

“Least waste → Fewest vials”.

Self-tests run automatically on load to ensure logic is consistent.