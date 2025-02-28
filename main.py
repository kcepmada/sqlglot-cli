"""SQLGlot Command-line Interface"""

import argparse
import sqlglot


def main(args=None):
    # Params
    parser = argparse.ArgumentParser(
        description="SQLGlot Command-line Interface | Dialect Transpiler (https://sqlglot.com/sqlglot.html#transpile)"
    )
    parser.add_argument(
        "-i",
        "--iDialect",
        type=str,
        default="databricks",
        dest="input_dialect",
        help="Source dialect",
    )
    parser.add_argument(
        "-o",
        "--oDialect",
        type=str,
        default="spark",
        dest="output_dialect",
        help="Target dialect",
    )
    parser.add_argument(
        "-p",
        "--pretty",
        action="store_true",
        default=False,
        help="Format with newlines and indentation for readability",
    )
    parser.add_argument("sql", type=str, help="Code")
    args = parser.parse_args(args)

    # Execute
    # eg. `create or replace materialized view "VENICE-MT-0"."proteus-irp-test$myview" (KEY, "flagshipGnnEmbedding304") as select "entityUrn", "embedding"['tensor']['staticDense']['values']['floats'] from queuing."proteus-flink-venice-testing" where "embedding"['embeddingName'] = 'urn:li:mlFeatureVersion:(urn:li:mlFeature:(flagship,gnnEmbedding),3,0,4)';`
    sql = sqlglot.transpile(
        args.sql,
        read=args.input_dialect,
        write=args.output_dialect,
        pretty=args.pretty,
        leading_comma=False,  # do not use leading comma in select expressions
        normalize=False,  # does not convert identifiers to lower case
        normalize_functions=True,  # converts function names to upper case
    )

    # Result
    for stmt in sql:
        print(stmt)


if __name__ == "__main__":
    main()

