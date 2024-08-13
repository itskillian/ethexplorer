# Ethereum Address Explorer

A full stack web app that allows users to explore ethereum address balances and transactions.

## Features
- Eth address balances and transactions
- live Ethereum blockchain stats
- ETH/USD converter
- light/dark mode

### Technologies Used
- Django
- MySQL
- JavaScript
- HTML/CSS
- Django Template Language
- requests library to handle API calls

### Preview
- home page displays live ETH data pulled via API
- user can search for an ETH address from the home page, or the top bar

<img width="512" alt="Screenshot 2024-08-13 at 10 10 55 AM" src="https://github.com/user-attachments/assets/ec6dcd58-5139-4b42-a7d3-2b7622f8fc55">

- address results page displays transaction data sorted by date, and saves this data to the transaction database

<img width="512" alt="Screenshot 2024-08-13 at 10 14 11 AM" src="https://github.com/user-attachments/assets/81c15979-5916-4537-9872-d9bdb0c108a1">

- django sessions keep track of recent search history, and a page visit counter

<img width="508" alt="Screenshot 2024-08-13 at 10 58 30 AM" src="https://github.com/user-attachments/assets/fea595e6-427a-4ae6-bd92-5bec9ca794f1">

- theme selection defaults to OS preference, or user can manually select between light and dark mode

<img width="512" alt="Screenshot 2024-08-13 at 10 15 10 AM" src="https://github.com/user-attachments/assets/69e9e1c1-e76a-4ca5-950a-0192fd43a6c1">

- conversion page lets users convert between ETH and USD values interchangeably

<img width="1512" alt="Screenshot 2024-08-13 at 11 15 47 AM" src="https://github.com/user-attachments/assets/f6479447-6e7b-42b3-a590-64680818c9bc">


