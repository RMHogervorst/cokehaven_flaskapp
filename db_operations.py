from sqlite3 import connect, Row
import logging

logger = logging.getLogger(__name__)


def insert_into_db(kilos, streetworth, team_naam, opmerking):
    try:
        with connect("database.db") as con:
            logger.debug(f'trying to insert data {team_naam},{kilos},{opmerking}, {streetworth}')
            cur = con.cursor()
            # submissions (team_naam TEXT, kilos INT, straatwaarde INT, opmerking TEXT)')
            cur.execute(
                "INSERT INTO submissions (team_naam,kilos,straatwaarde,opmerking) VALUES(?, ?, ?, ?);",
                (team_naam,int(kilos),streetworth,opmerking) ) # je moet dit klaarblijkelijk ech heel erg willen als int.
            con.commit()
            msg = "Score successvol toegevoegd"
            logger.info(msg)
    except:
        con.rollback()
        msg = "error in insert operatie"
        logger.warning(msg)
    finally:
        con.close()
        return msg


def create_database():
    conn = connect('database.db')
    logger.info("database succesvol geopend.")
    # team_naam, kilos, straatwaarde, opmerking
    conn.execute('CREATE TABLE submissions (team_naam TEXT, kilos INTEGER, straatwaarde TEXT, opmerking TEXT)')
    logger.info("Table created successfully")
    conn.execute('CREATE INDEX {ix} on {tn}({cn})'.format(ix="score_idx", tn="submissions", cn="kilos"))
    logger.info("created index")
    conn.close()


def get_latest_results():
    logger.info("getting results")
    con = connect("database.db")
    con.row_factory = Row
    cur = con.cursor()
    cur.execute("select team_naam, kilos, straatwaarde, opmerking from submissions order by kilos desc limit 200")
    rows = cur.fetchall()
    return rows
