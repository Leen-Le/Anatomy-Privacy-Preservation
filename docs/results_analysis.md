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
