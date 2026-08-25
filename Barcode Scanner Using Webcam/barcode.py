import cv2
from pyzbar.pyzbar import decode
import requests

def get_product_details(barcode):
    # Open Food Facts API endpoint
    api_url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 1:
            return data['product']
        else:
            return None
    else:
        return None

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert frame to grayscale for faster processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find barcodes in the frame and decode them
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            product_details = get_product_details(barcode_data)
            if product_details:
                print(product_details)
            else:
                print("Product details not found")

            # Optionally, you can display the barcode on the frame
            cv2.putText(frame, barcode_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
