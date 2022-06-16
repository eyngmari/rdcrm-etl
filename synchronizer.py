import jmespath


from models import Deal


class DealSynchronizer:
    def __init__(self, rd_deal: dict, session) -> None:
        self.rd_deal = rd_deal
        self.session = session

    def _convert_to_deal(self) -> Deal:

        deal = Deal(
            id=self.rd_deal['_id'],
            name=self.rd_deal['name'],
            contacts_email=jmespath.search(
                'contacts[].emails[0].email | [0]', self.rd_deal
            ),
            contacts_phones=jmespath.search(
                'contacts[].phones[0].phone | [0]', self.rd_deal
            ),
            user_id=self.rd_deal['user']['_id'],
            user_name=self.rd_deal['user']['name'],
            created_at=self.rd_deal['created_at'],
            updated_at=self.rd_deal['updated_at'],
            deal_stage_id=self.rd_deal['deal_stage']['_id'],
            deal_stage_name=self.rd_deal['deal_stage']['name'],
            deal_source_id=jmespath.search('deal_source.id', self.rd_deal),
            deal_source_name=jmespath.search('deal_source.name', self.rd_deal),
            deal_products_base_price=jmespath.search(
                'deal_products[].base_price | [0]', self.rd_deal
            ),
            deal_products_id=jmespath.search(
                'deal_products[].id | [0]', self.rd_deal
            ),
            deal_products_name=jmespath.search(
                'deal_products[].name | [0]', self.rd_deal
            ),
            win=self.rd_deal['win'],
            rating=self.rd_deal['rating'],
            closed_at=self.rd_deal['closed_at']
        )
        return deal

    def sync_with_database(self):
        deal_id = self.rd_deal.get('_id')
        deal = self.session.query(Deal).get(deal_id)

        if deal:
            deal.name = self.rd_deal['name']
            deal.contacts_email = jmespath.search(
                'contacts[].emails[0].email | [0]', self.rd_deal
            )
            deal.contacts_phones = jmespath.search(
                'contacts[].phones[0].phone | [0]', self.rd_deal
            )
            deal.user_id = self.rd_deal['user']['_id']
            deal.user_name = self.rd_deal['user']['name']
            deal.created_at = self.rd_deal['created_at']
            deal.updated_at = self.rd_deal['updated_at']
            deal.deal_stage_id = self.rd_deal['deal_stage']['_id']
            deal.deal_stage_name = self.rd_deal['deal_stage']['name']
            deal.deal_source_id = jmespath.search(
                'deal_source.id', self.rd_deal
            ),
            deal.deal_source_name = jmespath.search(
                'deal_source.name', self.rd_deal
            ),
            deal.deal_products_base_price = jmespath.search(
                'deal_products[].base_price | [0]', self.rd_deal
            ),
            deal.deal_products_id = jmespath.search(
                'deal_products[].id | [0]', self.rd_deal
            ),
            deal.deal_products_name = jmespath.search(
                'deal_products[].name | [0]', self.rd_deal
            ),
            deal.win = self.rd_deal['win']
            deal.rating = self.rd_deal['rating']
            deal.closed_at = self.rd_deal['closed_at']
        else:
            deal = self._convert_to_deal()
            self.session.add(deal)
