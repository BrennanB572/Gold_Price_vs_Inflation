![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/62c67771-86cf-4acf-989d-6999e2971786)


# ASU Data Analytics Project 1: Gold Price Prediction VS Inflation 2013 - 2021

## Sources Used:
Currency Specific Gold Valuations [ Yahoo Finance ]: 
- United States: https://finance.yahoo.com/quote/USD%3DX/history?p=USD%253DX![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/4c558ba4-627e-4eeb-bf2a-be679717fdaa)
- China: https://finance.yahoo.com/quote/CNYUSD%3DX/history?p=CNYUSD%253DX![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/4475262a-ee8c-42f3-934b-f13661f64c5b)
- Europe: https://finance.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX&guccounter=1![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/002c5590-6855-4540-a99e-3ddd4dd4b265)
- Russia: https://au.finance.yahoo.com/quote/RUBUSD%3DX/history?period1=1356998400&period2=1672444800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/cb61f335-8cf1-44ea-9631-2a0e38b7046e)


Inflation Rates:
- All Countries: Gold Price Prediction | LSTM | 96% Accuracy - https://www.kaggle.com/code/farzadnekouei/gold-price-prediction-lstm-96-accuracy/output

# Overview
- The Gold Price vs. Inflation 2013 - 2021 main goal is to identify Gold vs Inflation trends for the United States, Russia, China and Europe from 2013 - 2021. The end goal analysis is to answer 6 key questions:
  1. Where is the money lowest inflation?
  2. What currency experience the highest inflation?
  3. What currency experience the lowest inflation?
  4. Is it profitable to move money?
  5. What currency has the consistent value range for the longest time?
  6. What currency has the least consistent value range for the longest time?

# Hypothesis
- Below are the 4 main hypothesis for this project:
   1. Highest Inflation Country: Team Decision - United States
   2. Lowest Inflation Country: Team Decision - Russia
   3. Currency vs. Gold Hypothesis - As the currency deflates the currencies ability to purchase gold increases. If inflation is in a nonstandard range then currency will be safer kept in gold over time.

## Team Roster / Roles
#### Juan Herrera Sebastian - [ Code Architect ] 
- Juan was responsible for handling the A to Z code structure.
- Country Assignment: Russia / Ruble Analysis
#### Brennan Bradley - [ Version Control Architect ]
- Brennan was responsible for handling file organization and github merges.
- Country Assignment: United States / Dollar Analysis
#### Christian B. - [ Code Adaptation Specialist ]
- Christian was responsible for handling code commenting and code direction for accomplishing end analysis.
- Country Assignment: Europe / Euro Analysis
#### Ritika Changulani - [ Presentation Design Lead ] 
- Ritika took ownership of ensuring deadlines were accomplished and handled presentation updates/design.
- Country Assignment: China / Yen Analysis

## Research Questions / Analysis Conclusion
1. Where is the money lowest inflation?
2. What currency experience the highest inflation?
3. What currency experience the lowest inflation?
4. Is it profitable to move money?
5. What currency has the consistent value range for the longest time?
6. What currency has the least consistent value range for the longest time? 

## Analysis Results

### Analysis Overview Plot

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/50a58c32-0311-44b0-bd4d-f3839f08df4b)


### Russia / Ruble Analysis

- YoY Currency Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/84de2f3a-749d-4576-929a-403f500dd4c3)

- YoY Percentage Change Plot: 

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/49e6e727-b2af-49fa-96ae-d23202f35d83)

- Currency Percent Change YoY:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/b4e3aac0-6b3c-497b-b848-3185aed8eca1)

- If one was to immediately swap Ruble to gold upon obtaining the funds one would have avoided a -40% loss in purchasing power while only exposing funds to a risk of 8% in 2014.

### United States / Dollar Analysis

- YoY Currency Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/e2d51b6d-bb21-408d-a2c0-5c4939b9354c)

- YoY Percentage Change Plot: 

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/b124b89e-db80-4f0a-b16b-3ea127569252)

- Currency Percent Change YoY:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/259a7b22-ef35-43f8-bc8c-04d3b4a1d8fd)

- Lowest Percent Change Year was 2020 where there was a -11% change.
- Highest Percent Change Year was 2015 where there was a 26% change.
- If one were to sell Dollars into Gold during 2015, they would have seen a 55% increase in their currency value accumulated over those 6 years.

### Europe / Euro Analysis

- YoY Currency Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/9ae8375f-cbb3-4aef-bf98-174a1a014cfb)

- YoY Perecentage Change Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/1e81dcd6-56b1-4575-bdb8-4532a86778d1)

- Currency Percent Change YoY:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/2d497989-018e-45c9-958d-e2804cc45580)

- If an individual with Euros had chosen to invest in gold in 2013, they would have avoided a 23% depreciation by the year 2021.

### China / Yen Analysis

- YoY Currency Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/4336c676-81fa-413e-b4d8-7de2ce963bc6)

- YoY Percent Change Plot:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/aee58238-17c7-42e8-b653-31e8366d7e2e)

- Currency Percent Change YoY:

![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/114636599/084bf9ee-aa96-4a1d-92e7-534cbae15a3b)

- In the Gold Value In Yen Over the Years, the Adjusted Gold Value in Yen (the orange line) increases slowly in steps from $8,864.16 to $10,339.42. The orange line is a stable increase.
Whereas The Gold Value in Yen (the blue line) has an unstable change. 
In the Percent Change in Gold Value (Yen) Over Years, the gold value (blue line) is stable. Whereas the Yen value (orange line) has an unstable change.
![image](https://github.com/BrennanB572/Gold_Price_vs_Inflation/assets/153463563/b43a1be9-ebb2-4fcc-9d0e-2de9f35d6192)













