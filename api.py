# api_test.py - Advanced version
import requests


def search_food(food_name):
    """Search for a food and return its nutrition data"""
    print(f"🔍 Searching for: {food_name}")

    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food_name}&json=1&page_size=3"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            products = data['products']

            if not products:
                print("❌ No products found")
                return None

            print(f"✅ Found {len(products)} results. Showing best match:")

            # Get the most relevant result (usually first one)
            product = products[0]

            # Extract useful nutrition info
            nutrition_info = {
                'name': product.get('product_name', 'Unknown'),
                'brand': product.get('brands', 'Unknown'),
                'calories': product.get('nutriments', {}).get('energy-kcal_100g', 'N/A'),
                'carbs': product.get('nutriments', {}).get('carbohydrates_100g', 'N/A'),
                'protein': product.get('nutriments', {}).get('proteins_100g', 'N/A'),
                'fat': product.get('nutriments', {}).get('fat_100g', 'N/A')
            }

            print(f"🍎 Food: {nutrition_info['name']}")
            print(f"🏷️  Brand: {nutrition_info['brand']}")
            print(f"🔥 Calories per 100g: {nutrition_info['calories']}")
            print(f"🍞 Carbs: {nutrition_info['carbs']}g")
            print(f"🥩 Protein: {nutrition_info['protein']}g")
            print(f"🥑 Fat: {nutrition_info['fat']}g")

            return nutrition_info

        else:
            print("❌ API request failed")
            return None

    except Exception as e:
        print(f"💥 Error: {e}")
        return None


# Test it
if __name__ == "__main__":
    while True:
        food = input("\nEnter a food to search (or 'quit' to exit): ")
        if food.lower() == 'quit':
            break
        search_food(food)