import logging
import os
import time

from dotenv import load_dotenv

from database import create_session
from ingestion import DataRdCrmApi
from synchronizer import DealSynchronizer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def synchronize_deals(rd_deals: list, session):
    for rd_deal in rd_deals:
        synchronizer = DealSynchronizer(rd_deal, session)
        synchronizer.sync_with_database()


def run():
    connection_string = os.getenv('DB_MYSQL_CON_STRING')
    session = create_session(connection_string)
    token_api = os.getenv('TOKEN_API')
    api = DataRdCrmApi(token_api)

    page = 1
    has_more = True
    while has_more:
        logger.info(f'Page: {page} - Has more {has_more}')

        data = api.get_data(page)
        rd_deals = data['deals']
        synchronize_deals(rd_deals, session)
        session.commit()

        has_more = data['has_more']
        page = page + 1
        time.sleep(10)
        break


if __name__ == "__main__":
    load_dotenv()

    run()
