document.addEventListener('DOMContentLoaded', function () {
    const apiKey = 'a6a8b624ba6a56466d5e92b6c455b41f';
    const getWeatherButton = document.getElementById('get-weather');
    const cityInput = document.getElementById('city-input');
    const weatherInfo = document.getElementById('weather-info');

    getWeatherButton.addEventListener('click', function () {
        const city = cityInput.value.trim();
        if (city === '') {
            alert('Please enter a city name.');
            return;
        }

        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=a6a8b624ba6a56466d5e92b6c455b41f
        `;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const weatherInfoText = `Weather in ${data.name}: ${data.weather[0].main}, ${data.main.temp}°K`;
                weatherInfo.textContent = weatherInfoText;
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
            });
    });
});

