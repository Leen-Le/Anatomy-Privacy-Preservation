# Main Concepts

## Quasi-Identifier (QI)

Attributes that do not directly identify a person but can be combined with external information to reveal identity.

Examples:

* Age
* Gender
* Zip Code

## Sensitive Attribute (SA)

Attributes containing confidential information.

Examples:

* Disease
* Income
* Medical Condition

# Problem Statement

Organizations often need to publish data for research and analysis purposes. However, publishing raw data may reveal sensitive information about individuals.

Traditional anonymization methods such as generalization reduce the risk of disclosure but often cause significant information loss.

As a result, data utility decreases and the published dataset becomes less useful for analytical tasks.

The challenge is to preserve privacy while maintaining the usefulness of the published data.

# Research Motivation

Many privacy-preserving techniques rely on generalization, where attribute values are replaced by broader ranges.

Although this approach protects privacy, it reduces data accuracy and negatively affects query results.

The Anatomy method was proposed to overcome this limitation by separating quasi-identifiers from sensitive attributes while preserving the original values.

This approach aims to achieve a better balance between privacy protection and data utility.

# Traditional Privacy Preservation Approaches

Traditional privacy-preserving techniques mainly rely on data generalization.

Instead of publishing exact values, the data owner replaces specific values with broader ranges.

Example:

Age = 23

becomes

Age = [20-30]

This reduces the possibility of identifying individuals.

However, excessive generalization decreases data utility and negatively affects data analysis.

# Generalization Example

Original Data

| Age | Zipcode |
| --- | ------- |
| 23  | 12345   |
| 24  | 12346   |

Generalized Data

| Age   | Zipcode |
| ----- | ------- |
| 20-30 | 123**   |
| 20-30 | 123**   |

Generalization improves privacy but reduces data precision.

# Information Loss

Information loss refers to the reduction in data quality caused by anonymization techniques.

When exact values are replaced by ranges, important information is lost.

For example:

Age = 23

contains more information than:

Age = 20-30

The goal of privacy-preserving data publishing is to minimize information loss while maintaining privacy.
