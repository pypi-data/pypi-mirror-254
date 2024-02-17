[![codecov](https://codecov.io/gh/kirill-push/polony-counting/graph/badge.svg?token=3XYNQ0GYTB)](https://codecov.io/gh/kirill-push/polony-counting)
![GitHub release (with filter)](https://img.shields.io/github/v/release/kirill-push/polony-counting?sort=semver&color=brightgreen)
[![Linting](https://github.com/kirill-push/polony-counting/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/kirill-push/polony-counting/actions/workflows/lint.yml)
[![Testing](https://github.com/kirill-push/polony-counting/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kirill-push/polony-counting/actions/workflows/test.yml)
[![Documentation](https://github.com/kirill-push/polony-counting/actions/workflows/pages.yml/badge.svg)](https://github.com/kirill-push/polony-counting/actions/workflows/pages.yml)

# Polony counting project

## Table of Contents
1. [Project Description](#project-description)
    - [Overview](#overview)
    - [Project Goals](#project-goals)
2. [Project Repository Organization](#project-repository-organization)
3. [Contributions](#contributions)
4. [Feedback](#feedback)
5. [Acknowledgments](#acknowledgments)
6. [License](#license)

## Project Description
**Polony Counter**

Polony is a solid-phase single-molecule PCR-based method originally developed by Mitra and Church in 1999. In 2018 by Baran et.al. at Lindell lab, Technion it was adapted for the quantification of marine viruses belonging to a distinct virus family or group in field samples. It goes beyond counting "how many viruses in total" and provides precise information on "how many viruses of the particular clade of interest" are present in a given sample.

### Overview

Analyzing 20-30 samples of the ocean water using the Polony protocol typically takes 2.5 days. The process is divided into two main stages:

**Molecular Biology Work**: This stage, which spans two days, is conducted in the laboratory. It involves molecular biology procedures to prepare samples for analysis. At the end of this stage for each sample 2 microscope slides containing a thin polyacrylamide gel with PCR amplicones labeled by fluorescence probes are performed.

**Polony Counting**: After completing the molecular biology work, a set of high-resolution images of the gel are captured using a scanner. For each slide the set includes one RGB image and two black-and-white images representing the green and red channels, respectively. Those images of gel contain points named "polonies". Each point is a single phage amplicone labeled by fluorescence probe. Polonies appear in red, green, and yellow colors. They are counted and the number of polonies per slide is recalculated to the number of phages in the sample depanding on the Polony efficiency known for the studied gourp of viruses.

### Project Goals

The primary objective of this project is to streamline and automate the Polony counting stage of the procedure. The aim is to reduce the amount of time that researchers spend on manual counting, which can be labor-intensive and time-consuming. The automation of counting will also help to standardize the process to eliminate the "human factor" from the final viruses concentrations meanings.

## Project Repository Organization

    ├── LICENSE
    ├── README.md               <- The top-level README for developers using this project
    │
    ├── src                     <- Source code for use in this project
    │   └── polony
    │       │
    │       ├── __init__.py     <- Makes src a Python module
    │       │
    │       ├── checkpoints     <- Model savings
    │       │
    │       ├── config          <- Configuration files for the project
    │       │
    │       ├── data            <- Scripts to download or generate data
    │       │   ├── __init__.py 
    │       │   ├── make_dataset.py
    │       │   └── utils.py
    │       │
    │       └── models          <- Scripts with models
    │           ├── __init__.py 
    │           ├── models.py
    │           ├── predict_model.py
    │           ├── train_model.py
    │           └── utils.py
    │
    └── tests                   <- Scripts for functions and module testing

--------

<!-- ## Getting Started:-->

### Contributions

Contributions to this project are welcome, and developers, scientists, and researchers are encouraged to participate in its development. Whether you have expertise in image processing, machine learning, or molecular biology, your contributions can help advance this valuable tool for virus quantification in marine water samples.

### Feedback:

I value feedback from the community. If you encounter any issues, have suggestions for improvements, or would like to report bugs, please don't hesitate to open an issue on the GitHub repository.

### Acknowledgments

I would like to express my gratitude to Lindell's Lab at Technion for their pioneering work on the Polony protocol, which serves as the foundation for this project.

### License

This project is open-source and released under the MIT License. Please refer to the project's LICENSE file for more details on licensing.

