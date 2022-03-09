import scrapy

class Pcgamer(scrapy.Spider):
	name = 'pcgamer'
	start_urls = ['https://www.shopinfo.com.br/computadores-gamer']

	def parse(self, response):
		for produtos in response.css('div.mz__item'):
			#lista_preco = produtos.css('span.value::').getall()[1::2]
			preco = produtos.css('span.value::text').get().strip()[3:].replace('R$', '').strip()
			preco_full = float(preco.replace(',', '.')) * 10
			try:

				yield {
					'name': produtos.css('div.mz__product-name::text').get(),
					'price': str(preco_full),
					'link': produtos.css('a.mz__link').attrib['href'],
				}
			except:
				yield {
					'name': produtos.css('div.mz__product-name::text').get(),
					'price': 'sem estoque',
					'link': produtos.css('a.mz__link').attrib['href'],
				}

			#proxima_pagina = response.css('a.action.next').attrib['href']
			#if proxima_pagina is not None:
			#	yield response.follow(proxima_pagina, callback=self.parse)