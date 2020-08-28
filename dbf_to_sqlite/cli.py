import click
import dbf
from pathlib import Path
from sqlite_utils import Database


@click.command()
@click.version_option()
@click.argument("dbf_paths", type=click.Path(exists=True), nargs=-1, required=True)
@click.argument("sqlite_db", nargs=1)
@click.option("--table", help="Произвольное имя таблицы (работает только с единичными файлами)")
@click.option("-v", "--verbose", help="Показывать процесс", is_flag=True)
@click.option("-n","--name", help="Установить имя таблицы как файл.dbf", is_flag=True)
@click.option("-t","--trim", help="Убрать пробелы справа в таблицах", is_flag=True)
def cli(dbf_paths, sqlite_db, table, verbose, name, trim):
    """
    Convert DBF files (dBase, FoxPro etc) to SQLite

    https://github.com/simonw/dbf-to-sqlite
    """
    if table and len(dbf_paths) > 1:
        raise click.ClickException("--table only works with a single DBF file")
    db = Database(sqlite_db)
    for path in dbf_paths:
        table_name = table if table else Path(path).stem
        if name:
            table_name = path
        if verbose:
            click.echo('Загрузка {} в таблицу "{}"'.format(path, table_name))
        table = dbf.Table(str(path))
        table.open()
        columns = table.field_names
        db[table_name].insert_all(dict(zip(columns, list(row))) for row in table)
        table.close()
        if trim:
            for col in columns:
                db.conn.execute("UPDATE ? SET ? =RTrim( ? )",(table_name, col, col,))
                
            
    db.vacuum()
