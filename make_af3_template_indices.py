#!/usr/bin/env python3

import json
import sys


def make_index_mapping(
    aligned_query: str,
    aligned_template: str,
) -> tuple[list[int], list[int]]:
    """Convert a pairwise sequence alignment into AF3 template mappings."""

    aligned_query = aligned_query.replace(" ", "").upper()
    aligned_template = aligned_template.replace(" ", "").upper()

    if len(aligned_query) != len(aligned_template):
        raise ValueError(
            "The aligned query and template must have the same alignment length."
        )

    query_indices: list[int] = []
    template_indices: list[int] = []

    query_position = 0
    template_position = 0

    for query_residue, template_residue in zip(
        aligned_query, aligned_template
    ):
        query_has_residue = query_residue != "-"
        template_has_residue = template_residue != "-"

        if query_has_residue and template_has_residue:
            query_indices.append(query_position)
            template_indices.append(template_position)

        if query_has_residue:
            query_position += 1

        if template_has_residue:
            template_position += 1

    return query_indices, template_indices


def main() -> None:
    if len(sys.argv) != 3:
        print(
            "Usage:\n"
            "  python make_af3_template_indices.py "
            "ALIGNED_QUERY ALIGNED_TEMPLATE",
            file=sys.stderr,
        )
        sys.exit(1)

    query_indices, template_indices = make_index_mapping(
        sys.argv[1], sys.argv[2]
    )

    print('"queryIndices":')
    print(json.dumps(query_indices))
    print()
    print('"templateIndices":')
    print(json.dumps(template_indices))
    print()
    print(f"Number of mapped residues: {len(query_indices)}")


if __name__ == "__main__":
    main()
