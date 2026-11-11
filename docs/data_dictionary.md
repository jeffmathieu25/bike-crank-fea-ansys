# Mesh-summary data dictionary

File: [mesh_comparison.csv](../data/mesh_comparison.csv). One row per mesh, with decimal points and no thousands separators. All values are manually transcribed from the final report; these are summary values, not raw nodal or element results.

| Field | Meaning | Unit | Report source |
| --- | --- | --- | --- |
| `mesh` | Initial or refined discretization | — | Section 3 |
| `node_count` | Number of mesh nodes | count | Table 2 |
| `element_count` | Number of mesh elements | count | Table 2 |
| `body_element_size_in` | Characteristic body element size | in | Sections 2.4 and 3.1 |
| `hole_element_size_in` | Characteristic hole-face element size | in | Sections 2.4 and 3.1 |
| `max_total_displacement_in` | Maximum total displacement magnitude | in | Table 2 |
| `max_normal_stress_x_psi` | Reported maximum normal stress in x | psi | Section 2.7.2 and Table 2 |
| `max_skewness` | Maximum element skewness | dimensionless | Table 1 |
| `min_skewness` | Minimum element skewness | dimensionless | Table 1 |
| `mean_skewness` | Mean element skewness | dimensionless | Table 1 |
| `elements_skewness_gt_0_5_pct` | Share of elements with skewness > 0.50 | % | Table 1 |

In the supplied PDF, Table 1 appears on PDF page 22 (printed page 18), and Table 2 on PDF page 23 (printed page 19). Section headings and table numbers are the preferred references if pagination changes.

Percent fields contain percentage values: `0.44` means 0.44%, not 44%. Mesh-size values are in inches. Total displacement has units of length and is distinct from strain.
