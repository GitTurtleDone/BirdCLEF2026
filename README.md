This repository is used to participate in Kaggle competition
[BirdCLEF 2026](https://www.kaggle.com/competitions/birdclef-2026).

The guide to set up enviroment and download data can be seen [here](https://github.com/GitTurtleDone/BirdCLEF2026/blob/main/docs/installation.md)

A good link to understand

- [Different quantities from a confusion matrix](https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/)
- [ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM)
- You can test your understanding of ROC and AUC [here](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc#:~:text=On%20this%20page,then%20graphing%20TPR%20over%20FPR.).
- Micor- and macro-average ROC and AUC can be learned [here](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html).

Pull a notebook from Kaggle:

```bash
kaggle kernels pull <your-account>/<slug-of-the-notebook> -p <path/to/save/folder> --wp
```

--wp without output

Push a notebook to Kaggle:

```bash
kaggle kernels push -p .
```

given that currently in the folder containing a file to push and kernel-metadata.json was initialized with:

```bash
kaggle kernels init -p .
```

and modified correctly.

Download ouput from online training after Save & Run All:

```bash
kaggle kernels output <your-account>/<slug-of-the-notebook> -p /path/to/dest
```
