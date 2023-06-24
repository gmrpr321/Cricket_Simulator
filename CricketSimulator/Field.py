class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize the field with the given parameters.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
        self.weather_conditions = None

    def set_weather_conditions(self, weather_conditions):
        """
        Set the weather conditions for the field.
        """
        self.weather_conditions = weather_conditions

    def get_field_size(self):
        """
        Get the size of the field.
        """
        return self.size

    def get_fan_ratio(self):
        """
        Get the fan ratio for the field.
        """
        return self.fan_ratio

    def get_pitch_conditions(self):
        """
        Get the pitch conditions for the field.
        """
        return self.pitch_conditions

    def get_home_advantage(self):
        """
        Get the home advantage for the field.
        """
        return self.home_advantage

    def get_weather_conditions(self):
        """
        Get the weather conditions for the field.
        """
        return self.weather_conditions
