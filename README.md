#### Danilo III O. Gonzales (29225)
#### Master's in Green Data Science
### Project in Introduction to Python

# Growing Degree Days (GDD) and Crop Phenology Estimation of a Cropping Season

## Project Description

This project implements a Python-based tool to compute the growing degree days (GDD) and determine the current crop growth stage (phenology) for selected vegetable and field crops. The model uses daily air temperature data retrieved from the Open-Meteo API and applies crop-specific thermal thresholds derived from the revised FAO56 guidelines (FAO56rev).

Unlike cropping calendar-based approaches, this project estimates crop development using cumulative thermal time, providing a biologically meaningful representation of crop growth.

### Growing Degree Days (GDD)

Growing Degree Days (GDD) represent the accumulated thermal time available for crop growth and development and are calculated using daily air temperature relative to crop-specific base and upper thresholds. Daily GDD values are defined as zero when the mean air temperature falls below the base temperature, increase linearly b etween the base and upper thresholds, and are capped when temperatures exceed the upper threshold to reflect saturation of crop development. By summing daily GDD from the planting date onward, cumulative GDD provides a biologically meaningful measure of crop progress that is independent of calendar time. In practice, cumulative GDD is widely used to estimate phenological stages, schedule management operations such as fertilization and pest control, and anticipate harvest timing under varying climatic conditions.

The Growing Degree Days (GDD) used in this project are computed using the piecewise temperature-threshold formulation shown in Equations 1 and 2 based on the works of Paredes et al. (2025). Equation 1 defines daily GDD as a function of the mean air temperature relative to crop-specific base and upper temperature thresholds, while Equation 2 defines the daily mean air temperature as the average of the daily maximum and minimum temperatures.

$$
\mathrm{GDD} =
\begin{cases}
0, & T_{avg} < T_{base} \\
T_{avg} - T_{base}, & T_{base} \le T_{avg} \le T_{upper} \\
T_{upper} - T_{base}, & T_{avg} > T_{upper}
\end{cases}\;\;\;\;\;\;\;\;(1)
$$

<br>

$$
T_{avg} = \frac{T_{max} + T_{min}}{2}\;\;\;\;\;\;\;\;(2)
$$

**where:**

- **GDD** is the growing degree days  
- **T<sub>max</sub> (°C)** is the daily maximum air temperature  
- **T<sub>min</sub> (°C)** is the daily minimum air temperature  
- **T<sub>avg</sub> (°C)** is the daily mean air temperature  
- **T<sub>base</sub> (°C)** is the base temperature below which crop development ceases  
- **T<sub>upper</sub> (°C)** is the upper temperature threshold above which crop development no longer increases


While daily GDD values describe short-term thermal accumulation, crop development is more accurately represented by the cumulative sum of GDD over time. Cumulative Growing Degree Days (CGDD), as shown in Equation 3,  are obtained by summing daily GDD values from the planting date onward and serve as a thermal-time proxy for crop phenological progression.



$$
\mathrm{CGDD} = \sum_{i=1}^{n} \mathrm{GDD}_i\;\;\;\;\;\;\;\;(3)
$$

**where:**

- **CGDD** is the cumulative growing degree days  
- **GDD<sub>i</sub>** is the growing degree days on day *i*  
- **n** is the number of days elapsed since planting



In this project, cumulative GDD is used as the primary indicator for estimating the progress of the current crop season. Because CGDD integrates the effects of daily temperature variability, it provides a more biologically consistent measure of crop development than calendar-based approaches, particularly under variable or changing climatic conditions.

### FAO-56 Crop Growth Stages

The FAO-56 framework defines crop development as a sequence of four generalized growth stages: initial, development, mid-season, and late season. The initial stage begins immediately after planting and is characterized by slow growth and limited canopy development. During the development stage, vegetative growth accelerates as leaf area expands and thermal accumulation increases rapidly. The mid-season stage corresponds to effective full canopy cover and sustained physiological activity, during which crop development progresses at a relatively steady rate. Finally, the late-season stage marks the transition toward maturity, as growth slows, senescence begins, and the crop approaches harvest. In this project, these stages are represented using crop-specific cumulative Growing Degree Day (GDD) thresholds, allowing phenological progression to respond dynamically to temperature conditions rather than fixed calendar dates (Pereira et al., 2025).

**Figure 1** <br>
*FAO-56 Crop Growth Stage*<br>
![Crop](./images/crop_growth_stage.png)



### References

Paredes, P., López-Urrea, R., Martínez-Romero, Á., Petry, M., do Rosário Cameira, M., Montoya, F., … Pereira, L. S. (2025). Estimating the lengths of crop growth stages to define the crop coefficient curves using growing degree days (GDD): Application of the revised FAO56 guidelines. *Agricultural Water Management*, 319, 109758. [doi:10.1016/j.agwat.2025.109758](https://doi.org/10.1016/j.agwat.2025.109758)

Pereira, L. S., Allen, R. G., Paredes, P., López-Urrea, R., Raes, D., Smith, M., Kilic, A., & Salman, M. (2025). Crop evapotranspiration: Guidelines for computing crop water requirements (FAO Irrigation and Drainage Paper No. 56rev). Food and Agriculture Organization of the United Nations. https://www.fao.org/4/x0490e/x0490e00.htm

Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.7970649