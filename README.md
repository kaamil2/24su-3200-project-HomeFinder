# Summer 2024 CS 3200 Project: HomeFinder

## Created By

Created by: Brooke Blanton, Kaamil Thobani, Gabriela Prieto Colón, Evan Levy, Shawn Charles

## About

This project allows you to act as a realtor, potential buyer, or system admin for a homes website. This site provides buyers, sellers, and realtors with market data and predictive analytics to determine the best time to buy or sell a home.

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## Getting Started for Personal Exploration
1. Clone the repo to your computer. 
2. Set up the `.env` file in the `api` folder based on the `.env.template` file.
    - The root password should be "123"
3. Start the docker containers using the command "docker compose up -d" in the terminal.
4. Navigate to the SRC folder and type the command "streamlit run Home.py" in the terminal, this will take you to the site.
5. Once on the site, you can select which persona you want to act as (realtor, buyer, or system admin) and then select what you want
to do as that user. You can then log out and select a different persona to act as. To stop the app from running type control + c in the terminal.