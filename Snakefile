rule step1:
    output:
        "data/wine+quality.zip",
        "data/winequality-red.csv",
        "data/winequality-white.csv"
    shell:
        "python3 scripts/prepare_data.py"

rule step2:
    input:
        "data/winequality-red.csv",
        "data/winequality-white.csv"
    output:
        "profiling/report-red.html",
        "profiling/report-white.html"
    shell:
        "python3 scripts/profile.py"

rule step3:
    input:
        "data/winequality-red.csv",
        "data/winequality-white.csv"
    output:
        "results/alcohol_histogram-red.png",
        "results/alcohol_histogram-white.png",
        "results/regression_prediction_plot-red.png",
        "results/regression_prediction_plot-white.png",
        "results/summary_statistics-red.csv",
        "results/summary_statistics-white.csv"
    shell:
        "python3 scripts/analysis.py"
