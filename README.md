# PROJECT DASHBOARD: hotel-sort-revenue-optimization

## `Link to Confluence`: https://confluence.expedia.biz/display/ECT/Starting+a+new+data+science+project+with+EGE+data-science+code+and+document+templates
## `Link to DropBox`: None
<hr>
<hr>


## Summary
**Project Dashboard**

This is the project dashboard where you put key project information (for example, a project summary, with relevant links). In your actual project, replace the rest of the content with project-specific summary.

## CRISP-DM project structure

This repository contains an instantiation of the [**CRISP-DM**](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) structure for organizing and executing data science projects. The CRISP-DM data science lifecycle is composed of six major stages that are executed iteratively. This includes:

* Business Understanding
* Data Understanding
* Data Preparation
* Modeling
* Evaluation
* Deployment

The documentation and code are organized accordingly to have some standardization across project structure.

<p align="center"> <img src="__images/CRISP-DM_Process_Diagram.png" width="400" height="400"> </p>

<hr>
<hr>

## Project Documentation
There are three places where you can store documentation for a project.
* `REQUIRED`: `Confluence page` for the project. If not created, please create a Confluence page and link it to the EGE DS Confluence landing page.
* `REQUIRED`: A running `project report in the Git repo`. This should serve as the basic documentation for a project (with pointers to other resources, e.g. Confluence). A report of work in progress. Whereas the Confluence may serve as a resource for ex-Data Science team collaborators (reasonably mature reports and docs), this report of work in progress may be used for peer-review by data-scientists and developers in the Technology team.
* `OPTIONAL`: `Dropbox resource` for the project. As and when you have other documemtation or presentations, please create and link your Dropbox folder here.

We recommend that you include information in the [ProjectReport](https://github.expedia.biz/Egencia/data-science-project-template-repo/blob/master/ProjectReport.md) file. This template should be filled out with information that is specific to your project. 

In addition to the [ProjectReport](https://github.expedia.biz/Egencia/data-science-project-template-repo/blob/master/ProjectReport.md), which serves as the primary project document in the repository, we provide another template, [ProjectLearnings](https://github.expedia.biz/Egencia/data-science-project-template-repo/blob/master/ProjectLearnings.md), to include any learnings and information, which may not be included in the primary project document, but still useful to document. Other `optional` templates may be found [here](https://github.expedia.biz/Egencia/data-science-project-template-repo/tree/master/doc_templates); please feel free to use as needed.


## Project Folders and Files
The  project template contains top-level folders corresponding to the CRISP-DM stages. In each of these folders you should save both code and documentation. Documentation can include information about code (so someone else can reproduce the work as needed), as well as methods, results, observations etc., which may not all be appropriate to include in the overall ProjectReport.md file. 

In addition, we recommend you include `__sample_data` folder that can be used for early development or testing. Typically, not more than several (5) Mbs. Not for full or large data-sets. Any images related to documentation may be stored in `__images`. Configurations for running code or setting up the run-times can be stored under `__configs`. There are additional optional templates (`__optional_doc_templates`) which you can modify and adopt as needed.

The files Jenkinsfile, build.sh, Dockerfile, Makefile and requirements.txt are part of the CICD set up. Do not remove them unless you don't need any CICD. Instructions for setting up unit test can be found in `__tests folder`.

<hr>
<hr>

## `NOTES`: 
1. If your project currently doesn't get to modeling, evaluation or deployment phases, please just populate the other early phases of the CRISP-DM lifecycle with your documentation and code. 

2. In some cases, it may be difficult to break up the code and/or documentation into these specific stages (e.g. modeling and evaluation may be more easily done in one integrated Jupyter file). In that case, it is OK to keep the code/documentation into one sub-folder (instead of several). But please document why you deviated from the structure and where one can find the complete documentation and code for each phase.

3. In each of the sub-folders for the CRISP-DM stages, it is advised you keep documentation about the code and also someo of your results which won't fit into the Project Report or Project Learnings markdown. Details of parameters, results, observations would be useful to store in respective sub-folders, and can be linked to from the main project report.