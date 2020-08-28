# dbf-to-sqlitem
  forked 
## Usage

    $ dbf-to-sqlitem --help
    Usage: dbf-to-sqlitem [OPTIONS] DBF_PATHS... SQLITE_DB

      Convert DBF files (dBase, FoxPro etc) to SQLite

      https://github.com/simonw/dbf-to-sqlite

    Options:
      --version      Show the version and exit.
      --table TEXT   Table name to use (only valid for single files)
      -v, --verbose  Show what's going oncd 
      --help         Show this message and exit.
      -n, --name     Set normal name from table.dbf name
      -t, --trim     Trim right spaces after import

Example usage:

    $ dbf-to-sqlitem TABLE.DBF database.db

This will create a new SQLite database called `database.db` containing one table for each of the `DBF` files in the current directory.

Looking for DBF files to try this out on? Try downloading the [Himalayan Database](http://himalayandatabase.com/) of all expeditions that have climbed in the Nepal Himalaya.
