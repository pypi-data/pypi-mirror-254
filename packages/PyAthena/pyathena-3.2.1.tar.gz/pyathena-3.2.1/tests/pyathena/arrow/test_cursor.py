# -*- coding: utf-8 -*-
import contextlib
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from decimal import Decimal

import pandas as pd
import pyarrow as pa
import pytest

from pyathena.arrow.cursor import ArrowCursor
from pyathena.arrow.result_set import AthenaArrowResultSet
from pyathena.error import DatabaseError, ProgrammingError
from tests import ENV
from tests.pyathena.conftest import connect


class TestArrowCursor:
    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_fetchone(self, arrow_cursor):
        arrow_cursor.execute("SELECT * FROM one_row")
        assert arrow_cursor.rownumber == 0
        assert arrow_cursor.fetchone() == (1,)
        assert arrow_cursor.rownumber == 1
        assert arrow_cursor.fetchone() is None

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_fetchmany(self, arrow_cursor):
        arrow_cursor.execute("SELECT * FROM many_rows LIMIT 15")
        assert len(arrow_cursor.fetchmany(10)) == 10
        assert len(arrow_cursor.fetchmany(10)) == 5

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_fetchall(self, arrow_cursor):
        arrow_cursor.execute("SELECT * FROM one_row")
        assert arrow_cursor.fetchall() == [(1,)]
        arrow_cursor.execute("SELECT a FROM many_rows ORDER BY a")
        if arrow_cursor._unload:
            assert sorted(arrow_cursor.fetchall()) == [(i,) for i in range(10000)]
        else:
            assert arrow_cursor.fetchall() == [(i,) for i in range(10000)]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_iterator(self, arrow_cursor):
        arrow_cursor.execute("SELECT * FROM one_row")
        assert list(arrow_cursor) == [(1,)]
        pytest.raises(StopIteration, arrow_cursor.__next__)

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_arraysize(self, arrow_cursor):
        arrow_cursor.arraysize = 5
        arrow_cursor.execute("SELECT * FROM many_rows LIMIT 20")
        assert len(arrow_cursor.fetchmany()) == 5

    def test_arraysize_default(self, arrow_cursor):
        assert arrow_cursor.arraysize == AthenaArrowResultSet.DEFAULT_FETCH_SIZE

    def test_invalid_arraysize(self, arrow_cursor):
        arrow_cursor.arraysize = 10000
        assert arrow_cursor.arraysize == 10000
        with pytest.raises(ProgrammingError):
            arrow_cursor.arraysize = -1

    def test_complex(self, arrow_cursor):
        arrow_cursor.execute(
            """
            SELECT
              col_boolean
              ,col_tinyint
              ,col_smallint
              ,col_int
              ,col_bigint
              ,col_float
              ,col_double
              ,col_string
              ,col_varchar
              ,col_timestamp
              ,CAST(col_timestamp AS time) AS col_time
              ,col_date
              ,col_binary
              ,col_array
              ,CAST(col_array AS json) AS col_array_json
              ,col_map
              ,CAST(col_map AS json) AS col_map_json
              ,col_struct
              ,col_decimal
            FROM one_row_complex
            """
        )
        assert arrow_cursor.description == [
            ("col_boolean", "boolean", None, None, 0, 0, "UNKNOWN"),
            ("col_tinyint", "tinyint", None, None, 3, 0, "UNKNOWN"),
            ("col_smallint", "smallint", None, None, 5, 0, "UNKNOWN"),
            ("col_int", "integer", None, None, 10, 0, "UNKNOWN"),
            ("col_bigint", "bigint", None, None, 19, 0, "UNKNOWN"),
            ("col_float", "float", None, None, 17, 0, "UNKNOWN"),
            ("col_double", "double", None, None, 17, 0, "UNKNOWN"),
            ("col_string", "varchar", None, None, 2147483647, 0, "UNKNOWN"),
            ("col_varchar", "varchar", None, None, 10, 0, "UNKNOWN"),
            ("col_timestamp", "timestamp", None, None, 3, 0, "UNKNOWN"),
            ("col_time", "time", None, None, 3, 0, "UNKNOWN"),
            ("col_date", "date", None, None, 0, 0, "UNKNOWN"),
            ("col_binary", "varbinary", None, None, 1073741824, 0, "UNKNOWN"),
            ("col_array", "array", None, None, 0, 0, "UNKNOWN"),
            ("col_array_json", "json", None, None, 0, 0, "UNKNOWN"),
            ("col_map", "map", None, None, 0, 0, "UNKNOWN"),
            ("col_map_json", "json", None, None, 0, 0, "UNKNOWN"),
            ("col_struct", "row", None, None, 0, 0, "UNKNOWN"),
            ("col_decimal", "decimal", None, None, 10, 1, "UNKNOWN"),
        ]
        assert arrow_cursor.fetchall() == [
            (
                True,
                127,
                32767,
                2147483647,
                9223372036854775807,
                0.5,
                0.25,
                "a string",
                "varchar",
                datetime(2017, 1, 1, 0, 0, 0),
                datetime(2017, 1, 1, 0, 0, 0).time(),
                datetime(2017, 1, 2).date(),
                b"123",
                "[1, 2]",
                [1, 2],
                "{1=2, 3=4}",
                {"1": 2, "3": 4},
                "{a=1, b=2}",
                Decimal("0.1"),
            )
        ]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [
            {
                "cursor_kwargs": {"unload": True},
            },
        ],
        indirect=["arrow_cursor"],
    )
    def test_complex_unload(self, arrow_cursor):
        # NOT_SUPPORTED: Unsupported Hive type: time
        # NOT_SUPPORTED: Unsupported Hive type: json
        arrow_cursor.execute(
            """
            SELECT
              col_boolean
              ,col_tinyint
              ,col_smallint
              ,col_int
              ,col_bigint
              ,col_float
              ,col_double
              ,col_string
              ,col_varchar
              ,col_timestamp
              ,col_date
              ,col_binary
              ,col_array
              ,col_map
              ,col_struct
              ,col_decimal
            FROM one_row_complex
            """
        )
        assert arrow_cursor.description == [
            ("col_boolean", "boolean", None, None, 0, 0, "NULLABLE"),
            (
                "col_tinyint",
                "tinyint",
                None,
                None,
                3,
                0,
                "NULLABLE",
            ),
            (
                "col_smallint",
                "smallint",
                None,
                None,
                5,
                0,
                "NULLABLE",
            ),
            ("col_int", "integer", None, None, 10, 0, "NULLABLE"),
            ("col_bigint", "bigint", None, None, 19, 0, "NULLABLE"),
            ("col_float", "float", None, None, 17, 0, "NULLABLE"),
            ("col_double", "double", None, None, 17, 0, "NULLABLE"),
            ("col_string", "varchar", None, None, 2147483647, 0, "NULLABLE"),
            ("col_varchar", "varchar", None, None, 2147483647, 0, "NULLABLE"),
            ("col_timestamp", "timestamp", None, None, 3, 0, "NULLABLE"),
            ("col_date", "date", None, None, 0, 0, "NULLABLE"),
            ("col_binary", "varbinary", None, None, 1073741824, 0, "NULLABLE"),
            ("col_array", "array", None, None, 0, 0, "NULLABLE"),
            ("col_map", "map", None, None, 0, 0, "NULLABLE"),
            ("col_struct", "row", None, None, 0, 0, "NULLABLE"),
            ("col_decimal", "decimal", None, None, 10, 1, "NULLABLE"),
        ]
        assert arrow_cursor.fetchall() == [
            (
                True,
                127,
                32767,
                2147483647,
                9223372036854775807,
                0.5,
                0.25,
                "a string",
                "varchar",
                pd.Timestamp(2017, 1, 1, 0, 0, 0),
                datetime(2017, 1, 2).date(),
                b"123",
                [1, 2],
                [(1, 2), (3, 4)],
                {"a": 1, "b": 2},
                Decimal("0.1"),
            )
        ]

    def test_fetch_no_data(self, arrow_cursor):
        pytest.raises(ProgrammingError, arrow_cursor.fetchone)
        pytest.raises(ProgrammingError, arrow_cursor.fetchmany)
        pytest.raises(ProgrammingError, arrow_cursor.fetchall)
        pytest.raises(ProgrammingError, arrow_cursor.as_arrow)

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_as_arrow(self, arrow_cursor):
        table = arrow_cursor.execute("SELECT * FROM one_row").as_arrow()
        assert table.shape[0] == 1
        assert table.shape[1] == 1
        assert [row for row in zip(*table.to_pydict().values())] == [(1,)]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_many_as_arrow(self, arrow_cursor):
        table = arrow_cursor.execute("SELECT * FROM many_rows").as_arrow()
        assert table.shape[0] == 10000
        assert table.shape[1] == 1
        assert [row for row in zip(*table.to_pydict().values())] == [(i,) for i in range(10000)]

    def test_complex_as_arrow(self, arrow_cursor):
        table = arrow_cursor.execute(
            """
            SELECT
              col_boolean
              ,col_tinyint
              ,col_smallint
              ,col_int
              ,col_bigint
              ,col_float
              ,col_double
              ,col_string
              ,col_varchar
              ,col_timestamp
              ,CAST(col_timestamp AS time) AS col_time
              ,col_date
              ,col_binary
              ,col_array
              ,CAST(col_array AS json) AS col_array_json
              ,col_map
              ,CAST(col_map AS json) AS col_map_json
              ,col_struct
              ,col_decimal
            FROM one_row_complex
            """
        ).as_arrow()
        assert table.shape[0] == 1
        assert table.shape[1] == 19
        assert table.schema == pa.schema(
            [
                pa.field("col_boolean", pa.bool_()),
                pa.field("col_tinyint", pa.int8()),
                pa.field("col_smallint", pa.int16()),
                pa.field("col_int", pa.int32()),
                pa.field("col_bigint", pa.int64()),
                pa.field("col_float", pa.float32()),
                pa.field("col_double", pa.float64()),
                pa.field("col_string", pa.string()),
                pa.field("col_varchar", pa.string()),
                pa.field("col_timestamp", pa.timestamp("ms")),
                pa.field("col_time", pa.string()),
                pa.field("col_date", pa.timestamp("ms")),
                pa.field("col_binary", pa.string()),
                pa.field("col_array", pa.string()),
                pa.field("col_array_json", pa.string()),
                pa.field("col_map", pa.string()),
                pa.field("col_map_json", pa.string()),
                pa.field("col_struct", pa.string()),
                pa.field("col_decimal", pa.string()),
            ]
        )
        assert [row for row in zip(*table.to_pydict().values())] == [
            (
                True,
                127,
                32767,
                2147483647,
                9223372036854775807,
                0.5,
                0.25,
                "a string",
                "varchar",
                datetime(2017, 1, 1, 0, 0, 0),
                "00:00:00.000",
                datetime(2017, 1, 2, 0, 0, 0),
                "31 32 33",
                "[1, 2]",
                "[1,2]",
                "{1=2, 3=4}",
                '{"1":2,"3":4}',
                "{a=1, b=2}",
                "0.1",
            )
        ]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [
            {
                "cursor_kwargs": {"unload": True},
            },
        ],
        indirect=["arrow_cursor"],
    )
    def test_complex_unload_as_arrow(self, arrow_cursor):
        # NOT_SUPPORTED: Unsupported Hive type: time
        # NOT_SUPPORTED: Unsupported Hive type: json
        table = arrow_cursor.execute(
            """
            SELECT
              col_boolean
              ,col_tinyint
              ,col_smallint
              ,col_int
              ,col_bigint
              ,col_float
              ,col_double
              ,col_string
              ,col_varchar
              ,col_timestamp
              ,col_date
              ,col_binary
              ,col_array
              ,col_map
              ,col_struct
              ,col_decimal
            FROM one_row_complex
            """
        ).as_arrow()
        assert table.shape[0] == 1
        assert table.shape[1] == 16
        assert table.schema == pa.schema(
            [
                pa.field("col_boolean", pa.bool_()),
                pa.field("col_tinyint", pa.int8()),
                pa.field("col_smallint", pa.int16()),
                pa.field("col_int", pa.int32()),
                pa.field("col_bigint", pa.int64()),
                pa.field("col_float", pa.float32()),
                pa.field("col_double", pa.float64()),
                pa.field("col_string", pa.string()),
                pa.field("col_varchar", pa.string()),
                pa.field("col_timestamp", pa.timestamp("ns")),
                pa.field("col_date", pa.date32()),
                pa.field("col_binary", pa.binary()),
                pa.field("col_array", pa.list_(pa.field("array_element", pa.int32()))),
                pa.field("col_map", pa.map_(pa.int32(), pa.field("entries", pa.int32()))),
                pa.field(
                    "col_struct",
                    pa.struct([pa.field("a", pa.int32()), pa.field("b", pa.int32())]),
                ),
                pa.field("col_decimal", pa.decimal128(10, 1)),
            ]
        )
        assert [row for row in zip(*table.to_pydict().values())] == [
            (
                True,
                127,
                32767,
                2147483647,
                9223372036854775807,
                0.5,
                0.25,
                "a string",
                "varchar",
                pd.Timestamp(2017, 1, 1, 0, 0, 0),
                datetime(2017, 1, 2).date(),
                b"123",
                [1, 2],
                [(1, 2), (3, 4)],
                {"a": 1, "b": 2},
                Decimal("0.1"),
            )
        ]

    def test_cancel(self, arrow_cursor):
        def cancel(c):
            time.sleep(random.randint(5, 10))
            c.cancel()

        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(cancel, arrow_cursor)

            pytest.raises(
                DatabaseError,
                lambda: arrow_cursor.execute(
                    """
                    SELECT a.a * rand(), b.a * rand()
                    FROM many_rows a
                    CROSS JOIN many_rows b
                    """
                ),
            )

    def test_cancel_initial(self, arrow_cursor):
        pytest.raises(ProgrammingError, arrow_cursor.cancel)

    def test_open_close(self):
        with contextlib.closing(connect()) as conn:
            with conn.cursor(ArrowCursor):
                pass

    def test_no_ops(self):
        conn = connect()
        cursor = conn.cursor(ArrowCursor)
        cursor.close()
        conn.close()

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_show_columns(self, arrow_cursor):
        arrow_cursor.execute("SHOW COLUMNS IN one_row")
        assert arrow_cursor.description == [("field", "string", None, None, 0, 0, "UNKNOWN")]
        assert arrow_cursor.fetchall() == [("number_of_rows      ",)]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_empty_result(self, arrow_cursor):
        table = "test_arrow_cursor_empty_result_" + "".join(
            [random.choice(string.ascii_lowercase + string.digits) for _ in range(10)]
        )
        df = arrow_cursor.execute(
            f"""
            CREATE EXTERNAL TABLE IF NOT EXISTS
            {ENV.schema}.{table} (number_of_rows INT)
            ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
            LINES TERMINATED BY '\n' STORED AS TEXTFILE
            LOCATION '{ENV.s3_staging_dir}{ENV.schema}/{table}/'
            """
        ).as_arrow()
        assert df.shape[0] == 0
        assert df.shape[1] == 0

    @pytest.mark.parametrize(
        "arrow_cursor",
        [
            {
                "cursor_kwargs": {"unload": True},
            },
        ],
        indirect=["arrow_cursor"],
    )
    def test_empty_result_unload(self, arrow_cursor):
        table = arrow_cursor.execute(
            """
            SELECT * FROM one_row LIMIT 0
            """
        ).as_arrow()
        assert table.shape[0] == 0
        assert table.shape[1] == 0

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_executemany(self, arrow_cursor):
        rows = [(1, "foo"), (2, "bar"), (3, "jim o'rourke")]
        table_name = f"execute_many_arrow{'_unload' if arrow_cursor._unload else ''}"
        arrow_cursor.executemany(
            f"INSERT INTO {table_name} (a, b) VALUES (%(a)d, %(b)s)",
            [{"a": a, "b": b} for a, b in rows],
        )
        arrow_cursor.execute(f"SELECT * FROM {table_name}")
        assert sorted(arrow_cursor.fetchall()) == [(a, b) for a, b in rows]

    @pytest.mark.parametrize(
        "arrow_cursor",
        [{"cursor_kwargs": {"unload": False}}, {"cursor_kwargs": {"unload": True}}],
        indirect=["arrow_cursor"],
    )
    def test_executemany_fetch(self, arrow_cursor):
        arrow_cursor.executemany("SELECT %(x)d AS x FROM one_row", [{"x": i} for i in range(1, 2)])
        # Operations that have result sets are not allowed with executemany.
        pytest.raises(ProgrammingError, arrow_cursor.fetchall)
        pytest.raises(ProgrammingError, arrow_cursor.fetchmany)
        pytest.raises(ProgrammingError, arrow_cursor.fetchone)
        pytest.raises(ProgrammingError, arrow_cursor.as_arrow)

    def test_iceberg_table(self, arrow_cursor):
        iceberg_table = "test_iceberg_table_arrow_cursor"
        arrow_cursor.execute(
            f"""
            CREATE TABLE {ENV.schema}.{iceberg_table} (
              id INT,
              col1 STRING
            )
            LOCATION '{ENV.s3_staging_dir}{ENV.schema}/{iceberg_table}/'
            tblproperties('table_type'='ICEBERG')
            """
        )
        arrow_cursor.execute(
            f"""
            INSERT INTO {ENV.schema}.{iceberg_table} (id, col1)
            VALUES (1, 'test1'), (2, 'test2')
            """
        )
        arrow_cursor.execute(
            f"""
            SELECT COUNT(*) FROM {ENV.schema}.{iceberg_table}
            """
        )
        assert arrow_cursor.fetchall() == [(2,)]

        arrow_cursor.execute(
            f"""
            UPDATE {ENV.schema}.{iceberg_table}
            SET col1 = 'test1_update'
            WHERE id = 1
            """
        )
        arrow_cursor.execute(
            f"""
            SELECT col1
            FROM {ENV.schema}.{iceberg_table}
            WHERE id = 1
            """
        )
        assert arrow_cursor.fetchall() == [("test1_update",)]

        arrow_cursor.execute(
            f"""
            CREATE TABLE {ENV.schema}.{iceberg_table}_merge (
              id INT,
              col1 STRING
            )
            LOCATION '{ENV.s3_staging_dir}{ENV.schema}/{iceberg_table}_merge/'
            tblproperties('table_type'='ICEBERG')
            """
        )
        arrow_cursor.execute(
            f"""
            INSERT INTO {ENV.schema}.{iceberg_table}_merge (id, col1)
            VALUES (1, 'foobar')
            """
        )
        arrow_cursor.execute(
            f"""
            MERGE INTO {ENV.schema}.{iceberg_table} AS t1
            USING {ENV.schema}.{iceberg_table}_merge AS t2
              ON t1.id = t2.id
            WHEN MATCHED
              THEN UPDATE SET col1 = t2.col1
            """
        )
        arrow_cursor.execute(
            f"""
            SELECT col1
            FROM {ENV.schema}.{iceberg_table}
            WHERE id = 1
            """
        )
        assert arrow_cursor.fetchall() == [("foobar",)]

        arrow_cursor.execute(
            f"""
            VACUUM {ENV.schema}.{iceberg_table}
            """
        )

        arrow_cursor.execute(
            f"""
            DELETE FROM {ENV.schema}.{iceberg_table}
            WHERE id = 2
            """
        )
        arrow_cursor.execute(
            f"""
            SELECT COUNT(*) FROM {ENV.schema}.{iceberg_table}
            """
        )
        assert arrow_cursor.fetchall() == [(1,)]
