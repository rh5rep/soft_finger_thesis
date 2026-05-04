# Statistics For This Thesis

## Goal

Use statistics to:

- estimate quantities you care about
- quantify uncertainty
- compare simple model predictions with data
- avoid overclaiming

Do **not** start with:

- trying to force `p < 0.05`
- trying to imitate a clinical trial paper

This thesis is more likely to need `good estimation and model validation` than complex inferential statistics.

## The Main Statistical Ideas You Actually Need

### 1. Descriptive Statistics

Use these first:

- mean
- median
- standard deviation
- range
- interquartile range

Purpose:

- summarize behavior of actuator and finger variables
- describe repeatability and variability

### 2. Effect Size

Effect size means `how big the difference is`.

Examples for this thesis:

- how many degrees joint angle changes under assistance
- how much force output changes with pressure or displacement
- how much tracking error decreases under one controller versus another
- how much effective stiffness changes across settings

This is often more important than p-values in engineering work.

### 3. Confidence Intervals

A confidence interval gives a plausible range for the true value.

Examples:

- fitted passive stiffness parameter
- mean tracking error
- average ROM gain

Why this matters:

- it shows how uncertain the estimate is
- it is much more informative than simply saying `significant` or `not significant`

### 4. Regression

For this thesis, regression should mostly mean:

- `curve fitting`
- `parameter estimation`
- `relating inputs to outputs`

Likely uses:

- fit torque-angle curves
- fit pressure-force or displacement-force relationships
- estimate passive joint stiffness
- relate actuator commands to kinematic outputs

This is a good use of regression.

Less important right now:

- complex predictive regression with many clinical covariates

### 5. Goodness Of Fit

When comparing model and experiment, look at:

- `R^2`
- `RMSE`
- mean absolute error
- residual plots

Important:

- high `R^2` alone does not prove the model is good
- always inspect whether residuals show systematic error

### 6. Hypothesis Testing

Use hypothesis tests only when they answer a real comparison question.

Examples:

- does one actuator setting produce consistently lower tracking error than another?
- does one model structure fit significantly better than another?

Do not use tests just because papers report p-values.

## What A Good Statistical Workflow Might Look Like

### For Simulation

1. define the outputs of interest
   - joint angle
   - torque
   - force
   - displacement
   - stiffness
2. simulate under several parameter settings
3. visualize sensitivity
4. identify which parameters most strongly affect behavior

### For Bench Experiments

1. collect repeated trials
2. summarize repeatability
3. fit simple relationships
   - e.g. input to angle, angle to torque
4. compute uncertainty in fitted parameters
5. compare model prediction vs measured data

### For Model Validation

Use metrics such as:

- `RMSE`
- bias
- hysteresis measures
- repeatability across repeated trials
- confidence intervals on fitted parameters

## How To Think About `R^2`

`R^2` tells you how much of the variation in the observed data is explained by the model.

Good use:

- comparing whether a simple model captures most of the data trend

Bad use:

- treating high `R^2` as proof of causality
- treating high `R^2` as proof the model is mechanistically correct

## How To Think About P-Values

P-values ask:

- `if there were no real effect, how surprising would this result be?`

That can be useful, but in this thesis p-values should stay secondary to:

- effect size
- confidence intervals
- fit quality
- physical interpretability

## Regression For This Thesis Vs Regression In Clinical Papers

In clinical rehab papers, regression is often used to ask:

- which baseline factors predict post-treatment outcomes?

In this thesis, regression is more likely to be used to ask:

- what parameters best fit the actuator-finger behavior?
- how strongly does output depend on a controllable variable?
- can a low-order model explain the measured data?

That is simpler, cleaner, and more appropriate for the project.

## What To Learn Next

Priority order:

1. descriptive statistics
2. curve fitting and least squares
3. confidence intervals and uncertainty
4. residual analysis
5. comparing model vs experiment

Only after that:

- formal hypothesis testing
- more advanced regression

## Practical Rule

For each analysis, ask:

1. what quantity am I estimating?
2. how uncertain is it?
3. is the size of the effect meaningful?
4. does the model miss the data in a systematic way?
5. does this analysis help me make a thesis decision?
