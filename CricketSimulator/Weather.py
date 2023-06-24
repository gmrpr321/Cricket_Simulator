class Weather:
    def __init__(self, condition, temperature, wind_speed):
        """
        Initialize the weather conditions.
        """
        self.condition = condition
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = None
        self.precipitation = None

    def update_conditions(
        self, condition, temperature, wind_speed, humidity=None, precipitation=None
    ):
        """
        Update the weather conditions.
        """
        self.condition = condition
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.precipitation = precipitation

    def display_conditions(self):
        """
        Display the current weather conditions.
        """
        print(
            f"Weather Conditions: {self.condition}, Temperature: {self.temperature}°C, Wind Speed: {self.wind_speed} mph"
        )
        if self.humidity is not None:
            print(f"Humidity: {self.humidity}%")
        if self.precipitation is not None:
            print(f"Precipitation: {self.precipitation}")

    def is_rainy(self):
        """
        Check if the weather conditions indicate rain.
        """
        return self.condition == "Rainy" or (
            self.precipitation is not None and self.precipitation > 0
        )

    def is_hot(self):
        """
        Check if the weather conditions indicate hot temperature.
        """
        return self.temperature > 30

    def is_windy(self):
        """
        Check if the weather conditions indicate strong wind.
        """
        return self.wind_speed > 20
