# Modeling and interpretation notes

## Source of record

The [final technical report](../reports/3D_structural_mechanics_problem_Jeff_Mathieu_Bike_crank.pdf) is the source of record. It is in Portuguese and is preserved byte-for-byte. The English README and CSV summarize it without replacing it.

## Model definition

The supplied Parasolid geometry represents an aluminum 6061-T6 bicycle crank. Three support-region holes are fully fixed. A 100 lbf load acts in +y at the opposite end; other surfaces are traction-free. The model assumes isotropic linear elasticity and small deformations, with E = 10,000,000 psi and Poisson's ratio 0.33.

The report develops the static equilibrium, Hooke's law, and displacement–strain relations, then describes the ANSYS setup and the discrete system Kq = f.

## Mesh comparison

| Mesh | Body size (in) | Hole-face size (in) | Nodes | Elements |
| --- | ---: | ---: | ---: | ---: |
| Initial | 0.15 | 0.08 | 14,311 | 2,756 |
| Refined | 0.075 | 0.04 | 91,107 | 19,752 |

The distinct 14,662-node example mentioned in Section 2.6 illustrates a degree-of-freedom count. It is not the initial mesh used in the response comparison.

Relative response change is computed as:

```text
absolute relative change (%) = abs(Q_refined - Q_initial) / abs(Q_initial) * 100
```

The chart uses the signed version to show that displacement decreases and peak stress increases. Percentages are rounded to two decimal places.

## Consistency checks described in the report

- Inspect zero displacement at the fixed holes.
- Review displacement contours and the expected tensile/compressive regions under bending.
- Inspect local probes and results along a defined transverse path.
- Consider the opposite direction of the support reaction relative to the applied load.
- Compare the mesh-quality metrics and structural response for two discretizations.

The relation Ry = -100 lbf follows from the stated global force balance. A complete equilibrium check also requires the other reaction components and moments; the summary does not present it as an independently reproduced solver audit.

## Interpretation limits

The maximum displacement changes by approximately 1.05%, while the reported maximum normal stress in x changes by approximately 19.64%. This comparison measures sensitivity to the selected refinement, not error relative to an exact solution.

The model may have high stress gradients near geometric transitions. Two mesh levels do not demonstrate convergence or establish that a singularity exists. Additional refinement and comparison at equivalent physical positions would be needed.

The reported manual estimate of ±14,300 psi cannot be treated as a validated pointwise comparison without confirming the section geometry, probe positions, and coordinates. Likewise, the local normal stress in y and mean applied traction are not generally interchangeable: traction depends on the full stress tensor and local surface normal.

## Reproduction scope

The CSV and Python script reproduce the portfolio chart from reported summary values. They do not reproduce the underlying ANSYS solve, reconstruct the finite element mesh, or recover the full stress/displacement fields.
