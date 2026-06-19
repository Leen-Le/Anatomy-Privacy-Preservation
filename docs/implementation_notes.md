# Dataset Selection

## Adult Dataset

The Adult Dataset was selected for the implementation of the Anatomy privacy-preserving technique.

This dataset contains demographic and socioeconomic information collected from census records.

## Selected Quasi Identifiers (QI)

The following attributes will be used as quasi-identifiers:

* Age
* Sex
* Education

These attributes may not directly identify individuals, but they can be combined with external information to reveal identity.

## Selected Sensitive Attribute (SA)

The sensitive attribute selected for this project is:

* Income

Income represents confidential information and will be protected using the Anatomy method.

## Project Goal

The implementation will separate the dataset into:

* Quasi-Identifier Table (QIT)
* Sensitive Table (ST)

The relationship between the two tables will be maintained through a Group ID.

# Initial Dataset Analysis

The Adult Dataset contains demographic and socioeconomic information collected from census records.

For this project, only a subset of attributes will be used.

Selected attributes:

* Age
* Sex
* Education
* Income

The first three attributes will be treated as quasi-identifiers (QI), while Income will be treated as the sensitive attribute (SA).

This simplification reduces implementation complexity while preserving the main concepts of the Anatomy method.

# Dataset Exploration

The dataset was loaded using the Pandas library.

The initial exploration included:

* Viewing sample records
* Inspecting available attributes
* Identifying quasi-identifiers
* Identifying the sensitive attribute

This step helped prepare the dataset for the implementation of the Anatomy algorithm.

# Data Preparation Results

The original Adult Dataset was processed to create a simplified version suitable for the Anatomy implementation.

Only four attributes were retained:

* Age
* Education
* Sex
* Target

The resulting dataset will be used to generate the Quasi-Identifier Table (QIT) and the Sensitive Table (ST) in the next phase of the project.
