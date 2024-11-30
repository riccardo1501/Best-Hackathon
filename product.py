from typing import List, Dict
import json

class Product:
    def __init__(self, 
                 titolo: str, 
                 descrizione: str, 
                 valutazione_recensioni: float, 
                 numero_recensioni: int, 
                 top_3_recensioni: List[Dict[str, str]], 
                 ultime_3_recensioni: List[Dict[str, str]], 
                 prezzo: float, 
                 sconto: int, 
                 consegna_stimata: str):
        self.titolo = titolo  # str
        self.descrizione = descrizione  # str
        self.valutazione_recensioni = valutazione_recensioni  # float
        self.numero_recensioni = numero_recensioni  # int
        self.top_3_recensioni = top_3_recensioni  # list of dicts
        self.ultime_3_recensioni = ultime_3_recensioni  # list of dicts
        self.prezzo = prezzo  # float
        self.sconto = sconto  # int (percentage)
        self.consegna_stimata = consegna_stimata  # str
    
    def __str__(self) -> str:
        # Formatted product details
        str_repr = f"Product Title: {self.titolo}\n"
        str_repr += f"Description: {self.descrizione}...\n"  # Limit description to first 150 chars for brevity
        str_repr += f"Final price: €{self.prezzo} (Discounted: {self.sconto}% off)\n"
        str_repr += f"Rating: {self.valutazione_recensioni} ({self.numero_recensioni} reviews)\n"
        str_repr += f"Estimated Delivery: {self.consegna_stimata}\n"
        
        # Top 3 reviews
        str_repr += "\nTop 3 Reviews:\n"
        for review in self.top_3_recensioni:
            str_repr += f"  - {review['utente']} (Rating: {review['valutazione']}/5): {review['recensione']} (Date: {review['data']})\n"
        
        # Latest 3 reviews
        str_repr += "\nLatest 3 Reviews:\n"
        for review in self.ultime_3_recensioni:
            str_repr += f"  - {review['utente']} (Rating: {review['valutazione']}/5): {review['recensione']} (Date: {review['data']})\n"
        
        return str_repr

def get_products(file_path: str) -> List[Product]:
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        products_data = json.load(file)

    # Create a list of Product objects from the data
    products = []
    for product_data in products_data:
        product = Product(
            titolo=product_data['titolo'],
            descrizione=product_data['descrizione'],
            valutazione_recensioni=product_data['valutazione_recensioni'],
            numero_recensioni=product_data['numero_recensioni'],
            top_3_recensioni=product_data['top_3_recensioni'],
            ultime_3_recensioni=product_data['ultime_3_recensioni'],
            prezzo=product_data['prezzo'],
            sconto=product_data['sconto'],
            consegna_stimata=product_data['consegna_stimata']
        )
        products.append(product)

    return products