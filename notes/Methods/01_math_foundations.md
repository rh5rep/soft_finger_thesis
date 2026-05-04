# Math Foundations For This Thesis

## Goal

Learn enough math to build, test, and defend a simplified finger-actuator model without overinvesting in methods you may not need.

## Need Now

### Algebra And Trigonometry

Needed for:

- joint-angle geometry
- lever arms and moment arms
- converting between displacement, angle, and torque

### Calculus

Needed for:

- defining rates of change
- simple dynamic models
- interpreting stiffness and damping

You do not need deep formalism first. You need comfort with:

- derivatives
- integrals
- ordinary differential equations

### Statics And Basic Mechanics

Needed for:

- force balance
- torque balance
- free-body reasoning
- spring and damper abstractions

This is likely the most directly useful math in the short term.

### Linear Algebra

Needed for:

- writing compact model equations
- least-squares fitting
- parameter estimation
- understanding state-space models later if needed

### Basic Statistics

Needed for:

- summarizing experiments
- comparing repeated measurements
- reporting error bars, RMSE, variability, and repeatability

## Need Soon, But Not Necessarily First

### Optimization

Needed for:

- parameter fitting
- tuning simplified models
- maybe selecting actuator parameters later

### Signal Processing

Needed for:

- filtering noisy signals
- extracting movement frequency or variability
- analyzing repeated motion

### Control Basics

Needed for:

- understanding feedback vs feedforward
- interpreting controllability in a practical sense
- thinking about assistive vs resistive behavior

## Likely Math Sequence

1. statics and torque balance
2. spring-damper intuition
3. simple ODEs
4. least-squares parameter fitting
5. basic control and signal-processing concepts

## Practical Rule

If a math topic does not clearly help with one of these, deprioritize it:

- model a simplified finger
- model actuator-finger interaction
- fit parameters
- compare model and bench data
- report uncertainty or repeatability
