## files-2-db

Uploading data from files to database made easy! 

## Background

Importing a file from your local machine into a database which is in a remote server is painful process. The exact same process can be done through a command now. 

### Current implementation
- File formats supported - `.csv`
- Database engines supported - `mysql`

### Usage

The tool can be used in two ways. 
- Through command line, where you do not even need a python script to be created. 
    ```cmd
    usage: file2db [-h] --host HOST [--port PORT] --user USER --password PASSWORD
                --database DATABASE --table TABLE [--seperator SEPERATOR]
                [--ignore_errors IGNORE_ERRORS] [--n_rows N_ROWS]
                Source-file Target-database


    file2db - Transfer of data from your local file to Database, made simple.

    positional arguments:
    Source-file           Absolute path of the file to be uploaded, with suffix
    Target-database       Target database where the file has to be uploaded

    options:
    -h, --help            show this help message and exit
    --host HOST           URL or IP address representation of database host
    --port PORT           Port number to connect to the database
    --user USER           Username for database authentication
    --password PASSWORD   Password for database authentication
    --database DATABASE   Target database
    --table TABLE         Target table to insert the data
    --seperator SEPERATOR
                            Column seperator in the file
    --ignore_errors IGNORE_ERRORS
                            Try to keep reading lines if some lines yield errors. default
                            value -> False
    --n_rows N_ROWS       Number of rows from the file to be inserted to database.
                            Default -> all
    ```

- Otherwise, you can access the `ingest_data_from_file` API of the module. It takes the same set of parameters to the API in the below format, 

    ```python
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
        ...
    ```

### Roadmap

In upcoming versions, `files2db` will support commonly used file formats like, `.json`, `.parquet`, `.tsv`, `.xlsx`, `.arrow` and the databases, not limited to, `postgresql`, `sqlite`, `MSSQL` and what not. 
