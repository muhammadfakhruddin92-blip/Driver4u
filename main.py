
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Driver4UWidget(BoxLayout):
    result_text = StringProperty("")

    def calculate_fare(self, passenger, pickup, destination, fare_per_km):
        try:
            distance = 12.5  # Dummy distance in KM
            fare = float(fare_per_km)
            total_fare = distance * fare

            summary = f"Passenger: {passenger}\n" \ 
                      f"From: {pickup}\n" \ 
                      f"To: {destination}\n" \ 
                      f"Distance: {distance} KM\n" \ 
                      f"Total Fare: RM {total_fare:.2f}"

            self.result_text = summary
        except:
            self.result_text = "⚠ Please fill in all fields correctly."

class Driver4UApp(App):
    def build(self):
        return Driver4UWidget()

if __name__ == "__main__":
    Driver4UApp().run()
