-- test0
SELECT
  from_source.col0 AS from_source_col0
  , joined_source.col0 AS joined_source_col0
FROM (
  -- from_source
  SELECT
    col0
    , join_col
  FROM demo.from_source_table from_source_table
) from_source
INNER JOIN (
  -- joined_source
  SELECT
    col0
    , join_col
  FROM demo.joined_source_table joined_source_table
) joined_source
ON
  from_source.join_col = joined_source.join_col
