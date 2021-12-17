import scrapy




class ReckSpider(scrapy.Spider):
    name = 'Reck'
    start_urls = ['https://www.bestbuy.ca/fr-ca/produit/xtrike-me-cm-406-ensemble-de-clavier-souris-casque-et-tapis-filaire-avec-retro-eclairage/14670573','https://www.bestbuy.ca/fr-ca/produit/xtrike-me-sk-501-haut-parleurs-stereo-2-x-3w-noir/14635956','https://www.bestbuy.ca/fr-ca/produit/xtrike-me-mp-204-tres-grand-tapis-de-souris-de-grande-qualite-770-x-295-x-3-mm-rouge/14635963']

   
    def parse(self, response):

        for detail in response.css('div.x-product-detail-page'):
             yield {
                'titre' : detail.css('h1.productName_3nyxM::text').get()
            }
            

        for info in response.css('div.productPricingContainer_3gTS3'):
            yield {
                'price' : info.css('span.screenReaderOnly_3anTj::text').get(),
                'eco' : info.css('span.productSaving_3YmNX::text').get()
            }
            

        for info2 in info.css('div.productSaleEnds_5TuMK'):
            yield {
                'rabais' : info.css('time::text').get()
            }
            
        
        for store in response.css('div.marketplaceInfo_3JskU'):
            yield {
                'store' : store.css('span.marketplaceNameLink_2PX6p::text').get()
            }
            

        
