#### Danilo III O. Gonzales (29225)
#### Master's in Green Data Science
### Project in Introduction to Python

# Growing Degree Days (GDD) and Crop Phenology Estimation

## Project Description

<div>
  <p style="text-indent: 0.5in;  text-align: justify;">
    This project implements a Python-based tool to compute the growing degree days (GDD) and determine the current crop growth stage (phenology) for selected vegetable and field crops. The model uses daily air temperature data retrieved from the Open-Meteo API and applies crop-specific thermal thresholds derived from the revised FAO56 guidelines (FAO56rev).
  </p>

  <p style="text-indent: 0.5in; text-align: justify; ">
    Unlike cropping calendar-based approaches, this project estimates crop development using cumulative thermal time, providing a biologically meaningful representation of crop growth.
  </p>
</div>

### Growing Degree Days (GDD)

<div>
  <p style="text-indent: 0.5in; text-align: justify;">
    Growing Degree Days (GDD) represent the accumulated thermal time available for crop growth and development and are calculated using daily air temperature relative to crop-specific base and upper thresholds. Daily GDD values are defined as zero when the mean air temperature falls below the base temperature, increase linearly b etween the base and upper thresholds, and are capped when temperatures exceed the upper threshold to reflect saturation of crop development. By summing daily GDD from the planting date onward, cumulative GDD provides a biologically meaningful measure of crop progress that is independent of calendar time. In practice, cumulative GDD is widely used to estimate phenological stages, schedule management operations such as fertilization and pest control, and anticipate harvest timing under varying climatic conditions.
  </p>

  <p style="text-indent: 0.5in; text-align: justify;">
    The Growing Degree Days (GDD) used in this project are computed using the piecewise temperature-threshold formulation shown in Equations&nbsp;1 and&nbsp;2 based on the works of Paredes et&nbsp;al.&nbsp;(2025). Equation&nbsp;1 defines daily GDD as a function of the mean air temperature relative to crop-specific base and upper temperature thresholds, while Equation&nbsp;2 defines the daily mean air temperature as the average of the daily maximum and minimum temperatures.
  </p>
</div>

$$
\mathrm{GDD} =
\begin{cases}
0, & T_{\text{avg}} < T_{\text{base}} \\
T_{\text{avg}} - T_{\text{base}}, & T_{\text{base}} \le T_{\text{avg}} \le T_{\text{upper}} \\
T_{\text{upper}} - T_{\text{base}}, & T_{\text{avg}} > T_{\text{upper}}
\end{cases}
\tag{1}
$$

<br>

$$
T_{\text{avg}} = \frac{T_{\max} + T_{\min}}{2}
\tag{2}
$$

$$
\begin{array}{l}
\text{where} \\[4pt]
\hspace{0.4in}\text{GDD is the growing degree days,} \\
\hspace{0.4in}T_{\max}\;(^\circ\text{C}) \text{ is the daily maximum air temperature,} \\
\hspace{0.4in}T_{\min}\;(^\circ\text{C}) \text{ is the daily minimum air temperature,} \\
\hspace{0.4in}T_{\text{avg}}\;(^\circ\text{C}) \text{ is the daily mean air temperature,} \\
\hspace{0.4in}T_{\text{base}}\;(^\circ\text{C}) \text{ is the base temperature below which crop development ceases, and} \\
\hspace{0.4in}T_{\text{upper}}\;(^\circ\text{C}) \text{ is the upper temperature threshold above which crop development no longer increases.}
\end{array}
$$

### References

<div style="margin-left: 0; text-indent: -2em; padding-left: 2em; text-align: justify;">
Paredes, P., López-Urrea, R., Martínez-Romero, Á., Petry, M., Cameira, M. R., Montoya, F., Salman, M., & Pereira, L. S. (2025). Estimating the lengths of crop growth stages to define the crop coefficient curves using growing degree days (GDD): Application of the revised FAO56 guidelines. <i>Agricultural Water Management</i>, 319, 109758.
</div>