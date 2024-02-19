from pathlib import Path
from argparse import ArgumentParser

from polars import scan_csv, LazyFrame

from files2db.databases import MySQLConnector

def convert_csv_to_df(
    file_path: str,
    seperator: str,
    ignore_file_errors: bool,
    n_rows_to_consider: int,
) -> LazyFrame:
    """Converts the input file to dataframe using polars LazyFrame to handle bigger than RAM size files

    Args:
        file_path (str): Absolute path to the file
        seperator (str): Column seperator
        ignore_file_errors (bool): Try to keep reading lines if some lines yield errors
        n_rows_to_consider (int): Number of rows to consider

    Returns:
        LazyFrame: LazyFrame object of polars
    """
    file_to_df = scan_csv(
        source=file_path,
        separator=seperator,
        ignore_errors=ignore_file_errors,
        n_rows=n_rows_to_consider,
    )
    return file_to_df


def validate_file(file_path: Path) -> None:
    """Validation method for the input file
    with file type and file extension

    Args:
        file_path (str): Absolute path to the file

    Raises:
        ValueError: Not a valid file location
        TypeError: Not acceptable file type

    """
    if not file_path.is_file():
        raise ValueError("Input file doesn't exists.")

    if file_path.suffix not in [".csv"]:
        raise TypeError(f"Input file type => '{file_path.suffix}' is not supprted")


def ingest_data_from_file(
    file_path: str,
    target_database: str,
    db_host: str,
    db_port: int,
    db_user: str,
    db_password: str,
    data_db: str,
    data_table: str,
    file_seperator: str,
    ignore_file_errors: bool,
    n_rows_to_insert: int,
) -> None:
    """Main method to access to instantiate the functionality

    Args:
        file_path (str): Absolute path to the file
        target_database (str): Target database type
        db_host (str): URL or IP address representation of database host
        db_port (int): Port number to connect to the database
        db_user (str): Database username for authentication
        db_password (str): Database password for authentication
        data_db (str): Target database name to store data
        data_table (str): Target table name to store data
        file_seperator (str): Column seperator
        ignore_file_errors (bool): Try to keep reading lines if some lines yield errors
        n_rows_to_consider (int): Number of rows to consider
    """

    # create connector with appropriate database driver
    if target_database == "mysql":
        database_class = MySQLConnector(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=data_db,
        )

    # validate file path and extension
    validate_file(Path(file_path))

    # read as dataframe
    dataframe = convert_csv_to_df(
        file_path=file_path,
        seperator=file_seperator,
        ignore_file_errors=ignore_file_errors,
        n_rows_to_consider=n_rows_to_insert,
    )

    # pass to query builder to insert
    # considered there are no change in field names and field datatypes
    database_class.insert_data(table_name=data_table, data_df=dataframe.collect())

    return None


def main():
    arg_parser = ArgumentParser(
        prog="file2db",
        description="%(prog)s - Transfer of data from your local file to Database, made simple.",
    )

    arg_parser.add_argument(
        "source_file",
        metavar="Source-file",
        help="Absolute path of the file to be uploaded, with suffix",
    )
    arg_parser.add_argument(
        "database_engine",
        metavar="Target-database",
        help="Target database where the file has to be uploaded",
        choices=["mysql"],
        default="mysql",
    )

    # database parameters
    arg_parser.add_argument(
        "--host",
        help="URL or IP address representation of database host",
        required=True,
    )
    arg_parser.add_argument(
        "--port", help="Port number to connect to the database", default=3306, type=int
    )
    arg_parser.add_argument(
        "--user", help="Username for database authentication", required=True
    )
    arg_parser.add_argument(
        "--password", help="Password for database authentication", required=True
    )
    arg_parser.add_argument("--database", help="Target database", required=True)
    arg_parser.add_argument(
        "--table", help="Target table to insert the data", required=True
    )

    # file_parameters
    arg_parser.add_argument(
        "--seperator", default=",", help="Column seperator in the file"
    )
    arg_parser.add_argument(
        "--ignore_errors",
        default=False,
        help="Try to keep reading lines if some lines yield errors. default value -> False",
        type=bool,
    )
    arg_parser.add_argument(
        "--n_rows",
        default=None,
        help="Number of rows from the file to be inserted to database. Default -> all",
    )

    parameters = arg_parser.parse_args()

    ingest_data_from_file(
        file_path=parameters.source_file,
        target_database=parameters.database_engine,
        db_host=parameters.host,
        db_user=parameters.user,
        db_port=parameters.port,
        db_password=parameters.password,
        data_db=parameters.database,
        data_table=parameters.table,
        file_seperator=parameters.seperator,
        ignore_file_errors=parameters.ignore_errors,
        n_rows_to_insert=parameters.n_rows,
    )


if __name__ == "__main__":
    main()