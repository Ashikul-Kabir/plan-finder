# Project Overview: Customized Internet Plan Finder
- *Objective:* As a student consultant for Company NAVI, I was tasked with developing a customized internet plan finder that would enable users to receive personalized broadband recommendations in real-time. The goal was to enhance customer satisfaction by aligning broadband plans with individual user needs, such as household size, age, income, device usage, and current internet speed.

- *Data Sources:* To build the plan recommendation system, I utilized publicly available datasets:

-- **FCC Broadband Dataset –** Provided by the Company, containing information on available internet service providers and internet speeds across the U.S. (excluding pricing and county data).
-- **Census Data –** Extracted from publicly accessible census information to create a new dataset for modeling, named the mirror_dataset. This dataset included demographic variables such as age, income, the number of devices in use, and current internet speed.

- *Key Challenges & Solutions:*

-- **Lack of County Information in FCC Dataset:** The FCC dataset lacked granular geographical data at the county level. To address this, I integrated FIPS code information to match the dataset with corresponding county data, allowing the system to filter internet providers and plans by county.
-- **No Pricing Data:** Although pricing information was not included, I focused on recommending providers and internet speeds tailored to user needs based on their input (county, age, income, and number of devices). The recommendation engine was trained using the mirror_dataset to predict optimal speeds using machine learning.
-- **Machine Learning Approach:** I built and trained a RandomForestRegressor model using the mirror_dataset, which included enriched data points representing user demographics and technical specifications. The model was designed to predict the most suitable internet speed based on input such as:
-- Age
-- Income
-- Number of devices used
-- Current internet speed

- *Filtering Process:* Once the model predicted the ideal internet speed for the user, I filtered the results using the FCC Broadband Dataset to find the most suitable internet plans offered by providers in the user's county. The filtering criteria were based on the user’s county, predicted internet speed, and available providers in their area.

- *UI/UX Design:* The final plan finder was deployed using Streamlit, a Python-based platform for creating interactive web applications. I incorporated custom HTML and CSS to design a clean, user-friendly interface that allowed users to input their details (e.g., county, age, income, number of devices) and receive tailored broadband plan recommendations. The web application displayed:

-- Provider Name
-- Download/Upload Speed
-- County Information

- *Business Impact:* This project provides the Company with a valuable tool to enhance user engagement and experience. By offering personalized broadband plan recommendations based on real-time input, they can:

-- Improve customer satisfaction through tailored recommendations.
-- Potentially increase conversions by matching users with the most suitable broadband plans.
-- Utilize the UI/UX framework for future enhancements, such as incorporating pricing data or expanding the input criteria to include more nuanced needs.

In essence, the solution leveraged publicly available data, machine learning, and intuitive web design to deliver a functional and scalable plan finder that meets both user needs and NAVI's business goals.
