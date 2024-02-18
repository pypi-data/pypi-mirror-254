# Assignment Questions

MESA-Web will take at least a couple hours to process each calculation submission, potentially longer under peak demand. Plan ahead.

Many questions ask for narrative text to explain your results. Direct and concise explanations are desirable.

1. Read [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract), Sections 1-3, and Table 4. What are the recommended values for *mass fractions* $X$ (H), $Y$ (He), and $Z$ (Table 4) for the protosun and the present day photospheric values. Why do they differ? 

2. Using the logarithmic abundances in Asplund+09 Table 1, calculate the present day photospheric value of $X_C$, the mass fraction of carbon. Note that Asplund+09 use $\log$ to mean $\log_{10}$, not $\ln$. 

3. Read chapter 12 of [Stellar structure and Evolution](https://sta.rl.talis.com/link?url=https%3A%2F%2Fdoi-org.ezproxy.st-andrews.ac.uk%2F10.1007%2F978-3-642-30304-3&sig=fdcd1071b225a1cf90b44eda5279280c95987ab43c127ec62127524cf667c523) by Kippenhahn et al., available through the StA library as an E-Textbook. Then read Section 6 of [Paxton et al. 2011](https://ui.adsabs.harvard.edu/abs/2011ApJS..192....3P/abstract), the paper describing MESA, which is a Henyey-like code. What are the advantages of a Henyey scheme over a Schwarzchild (shooting) scheme? 

4. Submit a MESA-Web [calculation](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web-submit) for a $1 M_\odot$ star, leaving all other parameters at their default values. Download the run output when completed. Before continuing, review the MESA-Web [output documentation](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web-output). View the `.mp4` movie. What does each frame in the movie represent? Does the movie play linearly with time? Why or why not?

5. Use {meth}`as4012_sstr.reader.read_history` and `trimmed_history.data` to plot the evolutionary track of $L$ vs. $T_\mathrm{eff}$ for all timesteps in the model. Set the axis limits to zoom into when the star is on (and nearly on) the main sequence. Use the `star_age` quantity to check your $L$ vs. $T_\mathrm{eff}$ plot comports with your understanding of the main sequence lifetime of the Sun. Is the star truly stationary in the HRD for the entirety of the main sequence? 

6. Use {meth}`as4012_sstr.reader.read_history` and `trimmed_history.data` to plot the mass fractions $X$, $Y$, $Z$, and $X_\mathrm{C}$ at the centre of the star as a function of time, up to $10^{10}$ yrs. How do they change over the main sequence lifetime of the star? How do the initial mass fractions $X$, $Y$, and $Z$ compare to the Asplund+09 values for the protosun?
    
7.  Inspect the quantities provided by {meth}`as4012_sstr.reader.read_history` and design a set of criteria by which you might determine the Zero-Age Main Sequence (ZAMS) of your model. Plot these criteria (or some combination of them) vs. stellar age to determine the ZAMS age and closest time step (model number).

8. What are the ZAMS radius $R_\star$, luminosity $L_\star$, and effective temperature $T_\mathrm{eff}$? How do these compare to present day values for the Sun?

9. Use the `profiles.index` file to map the model number to the appropriate `profileXX.data` file. To save space, MESA does not save the profile for every model number, so you may need to compromise and use a nearby profile. Read this profile and plot quantities $\nabla_\mathrm{rad}$ and $\nabla_\mathrm{ad}$ vs. mass enclosed coordinate $m$ to identify the radiative and convective zones of the sun. You may wish to plot additional quantities that will help you identify the edge of the core, since this is not technically considered part of the radiative zone.

10. Revisit the `.mp4` movie produced by MESA, and pay particular attention to the plot in the centre of the top row. Pause and advance the movie up through the model number corresponding to ZAMS. Black regions represent radiative zones. Describe how the internal structure of the star changes as it moves from the pre-main sequence to the main sequence.

10. Rerun MESA web for a $2.0 M_\odot$ star and redo your calculation for the ZAMS age. How does this value compare to the ZAMS age for your $1.0 M_\odot$ star?

11. Identify the convective and radiative regions of the $2.0 M_\odot$ star at the ZAMS and compare them to that of the $1.0 M_\odot$ star. Do all main sequence stars have a structure similar to the Sun: nuclear-burning core interior to a radiative zone interior to a convective layer?