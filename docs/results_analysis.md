# Initial Evaluation

The Anatomy implementation successfully generated two independent tables:

* Quasi-Identifier Table (QIT)
* Sensitive Table (ST)

The original dataset was transformed while preserving the relationship between records through the Group ID.

This structure reduces direct disclosure of sensitive information and represents the main objective of the Anatomy method.

## Expected Benefits

* Improved privacy protection
* Reduced information loss
* Better data utility compared to traditional generalization methods

# Observations

The generated QIT table contains only quasi-identifiers and group information.

The generated ST table contains only sensitive values and group identifiers.

This separation prevents direct linkage between individuals and sensitive attributes.

The implementation demonstrates the core principle of the Anatomy privacy-preserving technique.

# Discussion

Traditional generalization methods modify original values and may reduce data quality.

In contrast, Anatomy preserves the original attribute values while separating sensitive information.

This approach improves analytical usefulness and reduces information loss.

The implementation confirms that privacy protection can be achieved without excessive data modification.

# Performance Analysis

The Anatomy implementation successfully separated quasi-identifiers from sensitive attributes.

The generated tables preserve the original values while reducing the risk of direct disclosure.

The use of Group IDs allows the relationship between records to be maintained without exposing sensitive information.

The resulting dataset structure improves privacy protection while preserving analytical usefulness.

# Dataset Statistics

Basic statistical analysis was performed on the simplified Adult Dataset.

The analysis included:

* Number of records
* Income distribution
* Gender distribution
* Education distribution

These statistics provide a better understanding of the dataset before and after applying the Anatomy structure.

# Visualization

A graphical analysis of the Income attribute was generated.

The visualization helps identify the distribution of sensitive values within the dataset and supports the evaluation of the Anatomy method.

Charts improve the interpretability of the results and facilitate comparison between groups.

# Conclusion

This project studied and implemented the Anatomy privacy-preserving technique using the Adult Dataset.

The implementation separated quasi-identifiers and sensitive attributes into two independent tables:

* Quasi-Identifier Table (QIT)
* Sensitive Table (ST)

The results demonstrated that Anatomy can protect sensitive information while preserving the original attribute values.

Compared to traditional generalization methods, Anatomy reduces information loss and improves data utility.

Overall, the Anatomy method provides an effective balance between privacy protection and analytical usefulness.

# Future Work

Several improvements can be made in future versions of this project.

Possible extensions include:

* Implementing full l-diversity constraints.
* Comparing Anatomy with k-anonymity.
* Comparing Anatomy with slicing techniques.
* Evaluating performance on larger datasets.
* Applying additional privacy-preserving techniques.
