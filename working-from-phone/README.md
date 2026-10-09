# Working from Phone: noisy linear fit

This example generates synthetic linear data with Gaussian noise, fits it using [lmfit](https://lmfit.github.io/lmfit-py/), and saves a PDF plot alongside the Python code.

True model: `y = 2.5*x + 1.0 + Normal(0, 2.0)`. NumPy random seed: 42.

## Run locally or using Codex Cloud

```bash
python -m pip install -r working-from-phone/requirements.txt
python working-from-phone/linear_fit.py
```

Output: `working-from-phone/linear_fit.pdf`, plus a printed lmfit report.

A GitHub Actions workflow also runs the script and commits the PDF automatically when the Python code or dependencies change on `main`. See `.github/workflows/working-from-phone-plot.yml`. This requires the repo's Actions permissions to allow workflow write access.

## Suggested Codex Cloud task

"Run the working-from-phone example. Verify the fit recovers a slope near 2.5 and intercept near 1.0, inspect the PDF, and propose improvements through a pull request. Do not change unrelated files."
