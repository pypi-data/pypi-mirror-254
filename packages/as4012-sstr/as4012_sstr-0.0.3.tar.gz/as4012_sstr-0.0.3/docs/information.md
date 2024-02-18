# Information

## Submission

All materials must be submitted through Moodle by **23:59 February 23rd, 2024**. There will be a penalty of 5% of the total available marks per day or partial day of late submission, including weekends and holidays.

Use the Moodle to submit:

**Report** containing the narrative text, plots, and numerical results requested for each question via [this Moodle Link](https://moody.st-andrews.ac.uk/moodle/mod/assign/view.php?id=1062940). You are free to prepare this report with whatever combination of tools you wish, but it must contain all of your answers and be self-contained *as a single PDF*. I would suggest either
* save plots as `*.png`, insert into Word or LaTeX document, add text, save to PDF.
* work directly in a Jupyter Notebook combining text, numbers and plots then [export to PDF](https://jupyterlab.readthedocs.io/en/stable/user/export.html).

**Code**: your `*.py` or `*.ipynb` files via [this Moodle Link](https://moody.st-andrews.ac.uk/moodle/mod/assign/view.php?id=1125515), or create a "secret" [Gist](https://gist.github.com/) with your code and submit the link. These will not be graded, nor will I reference them for numerical answers or plots.

## Grading Rubric

**Excellent** quality reports will:
* Demonstrate a correct understanding of the underlying physics solved by the MESA code.
* Concisely and directly explain the significance of numerical results using narrative text.
* Contain correct numerical results and properly labeled plots.

**Average** quality reports may:
* Demonstrate a largely correct understanding of the subject matter, but may evidence small misconceptions.
* Present correct numerical results, but may sometimes fail to fully explain their significance.
* Be vague or overly wordy with their narrative text.

**Poor** quality reports may:
* Demonstrate an incorrect understanding of the subject matter and the numerical calculations.
* Contain numerical errors.
* Fail to connect physical and numerical understanding across parts of the assignment.
* Be incomplete.

The assignment counts for 25% of your module grade. The [**Assignment Questions**](assignment.md) are worth 2 points each, for a total of 24 pts. The remaining 1 point is awarded for general report quality.

The narrative aspect of your report is as important to understanding the results of your analysis as your numerical values are. Assume that you are writing a technical report to your manager or team members. Take pride in your work and strive for clarity, concision, and excellence.

## Code Installation

[![tests](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml/badge.svg)](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml)

This repository repackages the `mesa_web.py` reader routines to help you analyze the output from your MESA-Web run. To install this code into your Python environment

1. Download this repository from GitHub.
2. Enter the root of the repository, and run 
```
pip install .
```
3. Now, in your Python interpreter, you should be able to do
```
>>> from as4012_sstr import reader
>>> table = reader.read_history(...)
```

See the [](api.md) for full documentation of the reading routines.

If you have any issues, please review the [guide to installing Python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). If your issues persist, please contact <ic95@st-andrews.ac.uk> listing the steps you tried following the guide.

## References

* [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract) You can download the article if you are on the StA network, otherwise there is a copy on Moodle.  
* [R. Kippenhahn, A. Weigert, A. Weiss (2013) "Stellar structure and Evolution](https://sta.rl.talis.com/link?url=https%3A%2F%2Fdoi-org.ezproxy.st-andrews.ac.uk%2F10.1007%2F978-3-642-30304-3&sig=fdcd1071b225a1cf90b44eda5279280c95987ab43c127ec62127524cf667c523) E-Textbook (free to StA)
* [MESA-Web](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web) the online interface you will use to run MESA.
* [Paxton et al. 2011](https://ui.adsabs.harvard.edu/abs/2011ApJS..192....3P/abstract): the definitive MESA publication
* [Fields et al. 2023](https://ui.adsabs.harvard.edu/abs/2023arXiv230915930F/abstract): Publication to appear in the Astronomy Education Journal describing MESA-Web
* [DSFE 2018 grading rubric](https://matthew-brett.github.io/dsfe/projects/rubric), inspiration for rubric.