import scrapy
import re
import json
import os


class PasCarSpider(scrapy.Spider):
    name = "pas_car"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com/uk/legkovie/?page=1"]

    def __init__(self, *args, **kwargs):
        super(PasCarSpider, self).__init__(*args, **kwargs)
        self.load_car_types()

    def load_car_types(self):
        file_path = os.path.join(os.path.dirname(__file__), 'car_types.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.body_types = data.get('body_types', [])
            self.fuel_types = data.get('fuel_types', [])
            self.transmission_types = data.get('transmission_types', [])
            self.drive_types = data.get('drive_types', [])
            self.eco_standards = data.get('eco_standards', [])

    def parse(self, response):
        car_links = response.xpath(
            "//section[contains(@class, 'ticket-item')]//a[contains(@class, 'm-link-ticket')]/@href").extract()
        self.logger.info(f'Found {len(car_links)} car links.')
        for link in car_links:
            yield response.follow(link, callback=self.parse_car)
        # ======================================================================
        # Проверка наличия кнопки "Вперед"
        # next_page = response.xpath(
        #     "//span[contains(@class, 'next')]/a[not(contains(@class, 'disabled'))]/@href").get()
        # if next_page:
        #     self.logger.info(f'Navigating to the next page: {next_page}')
        #     yield response.follow(next_page, callback=self.parse)
        # ======================================================================

    def parse_car(self, response):
        try:
            # Извлечение данных автомобиля
            price_raw = response.xpath(
                "//div[contains(@class, 'price_value')]/strong/text()").get()
            price = self.extract_price(price_raw)

            breadcrumbs = response.xpath(
                "//div[@class='breadcrumbs size13']//span/text()").extract()
            breadcrumbs_cleaned = [crumb.strip()
                                   for crumb in breadcrumbs if crumb.strip()]
            region = breadcrumbs_cleaned[1] if len(
                breadcrumbs_cleaned) > 1 else None
            city = breadcrumbs_cleaned[2] if len(
                breadcrumbs_cleaned) > 2 else None
            brand = breadcrumbs_cleaned[3] if len(
                breadcrumbs_cleaned) > 3 else None
            model = breadcrumbs_cleaned[4] if len(
                breadcrumbs_cleaned) > 4 else None

            seller_name = response.xpath(
                "//div[contains(@class, 'seller_info_name')]/text()").get()
            seller_name = seller_name.strip() if seller_name else None
            year_raw = response.xpath(
                "//h3[contains(@class, 'auto-content_title')]/text()").get()
            year = self.extract_year(year_raw)

            color = response.xpath(
                "//span[@class='argument']//span[contains(@class, 'car-color')]/following-sibling::text()").get()
            color = color.strip() if color else None
            owners_count = response.xpath(
                "//span[contains(text(), 'Кількість власників')]/following-sibling::span[@class='argument']/text()").get()
            owners_count = owners_count.strip() if owners_count else None

            vin = response.xpath("//span[@class='label-vin']/text()").get()
            vin = vin.strip() if vin else None
            car_number = response.xpath(
                "//span[@class='state-num ua']/text()").get()
            car_number = car_number.strip().replace(" ", "") if car_number else None
            accident_info = response.xpath(
                "//span[contains(text(), 'Участь в ДТП')]/following-sibling::span[@class='argument']/text()").get()
            accident = True if accident_info and 'Був в ДТП' in accident_info else False

            mileage_raw = response.xpath(
                "//div[contains(@class, 'base-information bold')]//span[@class='size18']/text()").get()
            mileage = int(mileage_raw.strip()) * 1000 if mileage_raw else None

            body_type = self.extract_type(response, self.body_types)
            fuel_type = self.extract_type(response, self.fuel_types)
            transmission_type = self.extract_type(
                response, self.transmission_types)
            drive_type = self.extract_type(response, self.drive_types)
            eco_standard = self.extract_type(response, self.eco_standards)

            # Извлечение мощности (к.с.)
            power_hp_raw = response.xpath(
                "//*[contains(text(), 'к.с.')]/text()").get()
            power_hp = None
            if power_hp_raw:
                match_hp = re.search(r"(\d+)\s*к\.с\.", power_hp_raw)
                if match_hp:
                    power_hp = int(match_hp.group(1))

            # Извлечение мощности (кВт)
            power_kw_raw = response.xpath(
                "//*[contains(text(), 'кВт')]/text()").get()
            power_kw = None
            if power_kw_raw:
                match_kw = re.search(r"(\d+)\s*кВт", power_kw_raw)
                if match_kw:
                    power_kw = int(match_kw.group(1))

            # Извлечение ссылки на фото
            photo_url = response.xpath(
                "//img[@class='outline m-auto']/@src").get()

            self.logger.info(f'Extracted data for {brand} {model}: Price: {price}, Region: {region}, City: {city}, Year: {year}, Color: {color}, Body Type: {body_type}, Fuel Type: {fuel_type}, Transmission Type: {transmission_type}, Drive Type: {drive_type}, Eco Standard: {eco_standard}, Owners Count: {owners_count}, VIN: {vin}, Car Number: {car_number}, Accident: {accident}, Mileage: {mileage}, Power (HP): {power_hp}, Power (kW): {power_kw}, Photo URL: {photo_url}')

            yield {
                'price': price,
                'region': region,
                'city': city,
                'brand': brand,
                'model': model,
                'seller_name': seller_name,
                'year': year,
                'color': color,
                'body_type': body_type,
                'fuel_type': fuel_type,
                'transmission_type': transmission_type,
                'drive_type': drive_type,
                'eco_standard': eco_standard,
                'owners_count': owners_count,
                'vin': vin,
                'car_number': car_number,
                'accident': accident,
                'mileage': mileage,
                'power_hp': power_hp,  # Добавляем мощность в к.с.
                'power_kw': power_kw,   # Добавляем мощность в кВт
                'photo_url': photo_url,  # Добавляем ссылку на фото
            }
        except Exception as e:
            self.logger.error(f'Error parsing car data: {e}')

    def extract_price(self, price_str):
        if price_str:
            return int(re.sub(r"[^\d]", "", price_str))
        return None

    def extract_year(self, year_str):
        if year_str:
            match = re.search(r'\b\d{4}\b', year_str)
            return match.group(0) if match else None
        return None

    def extract_type(self, response, type_list):
        for item in type_list:
            if item.lower() in response.text.lower():
                return item
        return None
