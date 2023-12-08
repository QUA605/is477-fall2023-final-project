# Reproduction of: Wine Quality - New Datasets for Fair Machine Learnings (IS477)

[![DOI](https://zenodo.org/badge/728463610.svg)](https://zenodo.org/doi/10.5281/zenodo.10287748)

## Overview

The datasets that I selected is "Wine Quality" which contains both red and white wines dataset. The dataset is fair that only physicochemical and sensory variables are contained which eliminates the variable such as price, types of grapes, and brand to make sure the output variable "quality" is fair. Both dataset contains twelve input variables and a output variable "quality" which in the analysis script we will try to use the twelve input variables to predict the quality. There are three scripts that would be used to reproduce this project. The scripts are to download the datasets file, profile the data, and do analyzation on the data. All the require packages are contained in the requirements.txt file which should be executed if not running on the docker virtual machine. The provided docker virtual machine can be used to run the scripts without encountering software errors. We will be focusing on the analyzation of simple regression task on predicting the quality that could be used to understand which of the twelve inputs affect quality the most.

## Analysis

After running the workflow, we will first download the two datasets and then store six files in the results folder after analzation. There will be graph that demonstrate the prediction versus actual which we could see how the prediction on the 12 input variables do. There are also histogram that are used to show the distribution of the alcohol of both white and red wine. From the distribution we can see that both of them are skewed to the right. The summary statistics shows the statistics of all 12 input variables which we could also use to learn about the distribution. 

## Workflow

![Visualization of SnakeFile](graph.png)

Make sure to run "pip install -r requirements.txt" before running the script if not using docker image.

## Reproducing

* Clone the GitHub respository containing the srcipts folder and docker image(qua65/is477-fall2023-final-project:v1). 

* Run first command: docker run --rm -v ${PWD}:/is477 qua65/is477-fall2023-final-project:v1 python prepare_data.py 

* Run second command: docker run --rm -v ${PWD}:/is477 qua65/is477-fall2023-final-project:v1 python profile.py 

* Run third command: docker run --rm -v ${PWD}:/is477 qua65/is477-fall2023-final-project:v1 python analysis.py

## License

I choose to use the MIT license which covers the content for my software. Others are free to use the software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


## References

Cortez,Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.