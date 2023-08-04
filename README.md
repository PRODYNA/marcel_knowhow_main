 ```
 __  __                    _   _  __                    _                   
|  \/  | __ _ _ __ ___ ___| | | |/ /_ __   _____      _| |__   _____      __
| |\/| |/ _` | '__/ __/ _ \ | | ' /| '_ \ / _ \ \ /\ / / '_ \ / _ \ \ /\ / /
| |  | | (_| | | | (_|  __/ | | . \| | | | (_) \ V  V /| | | | (_) \ V  V / 
|_|  |_|\__,_|_|  \___\___|_| |_|\_\_| |_|\___/ \_/\_/ |_| |_|\___/ \_/\_/  
                                                                            

```
Marcel Know How Main Project
===============================
This repo is the conceptual main project for the Marcel Know How Project. It contains of 
- General documentation
- A python script to create AI content (questions and images) populated to the frontend and database
- References to the other repos

# General Purpose
The project aims to provide knowledge to a persona named Marcel. Marcel starts at his company as a 
Sales representative. Although he is an experienced salesperson with many years of experience in 
selling, he only has a base knowledge of IT services.
Since his company focuses on providing custom enterprise software solutions, one of Marcel's tasks 
is to gain general knowledge about the latter area.
The Marcel Knowledge project reflects many exemplary services his company provides in a simplified
and documented form.
With this project, Marcel receives an open reference for look-up, which his company and he can
extend in multiple ways.
Since the "how to get things running" is well documented and resettable, Marcel can even experiment
with aspects of the project on his on machine 
(e.g., removing or shifting buttons or modifying the AI-generated content generation).
See: [local setup guide](./docs/local_setup.md) 

# Scenario of the Project
Marcel's company received the order to build an MVP (Minimal Viable Product) for a fictional 
business case (details below). The project has already started and is in a developed state to be 
looked at with certain limitations (as also listed below).

# Relevant Aspects for a Salesperson their Reflections in this Project
## Business view
As a salesperson it is one of the most important things is to understand what kind of business 
factors drive the customer.

Fictional Business Case: A customer wants to provide an online quizz for theme of European history 
to attract users. If the customer gains more then 1'000'000 users he wants to monetize by offering a 
Pro subscriptions for other themes paying 5 Dollar/yearly subscription with the expectation of 
1% conversion.

- What will the production cost? 
- What will be the yearly costs? 
- What are typical questions besides costs?


## Project Organization and Management (10-15%)
How to manage and plan the project? What kind of approach will we use? Do we need trainings?


## Design and Conception (15-20%)
How to "catch" the user?
How do we create the User Experience?
How do we get feedback from the customer and the customer's users?
Where and how do we  document?
How can the product be found?
What kind of users do we have?
How can we design the product (especially the UI) to achieve which goals (e.g., a hip/conservative impression?)
How can we assess the quality?
How do we interact with development?


## Data View (10-20%)
What kind of data do we need?
Where do we get it from?
How can we move the source data into what we want?
What kind of (user) data/insights do we want?
Can we create or reuse data?
Where can AI help us?


## Software Engineering (30-40%)
What kind of technologies are used and what's the impact?
What kind of people do we have and the customer?
Do we need trainings or reviews?
Do we work cross-cutting/fullstack?
Which components do we want and what is the impact?
How can we develop independently from each other a big system?
What can we automize?
How can we ensure "code quality"?
Where can we use AI (for automization)?
Data safety and protection?


## DevOps (10-15%)
Where will it run (Cloud? Which cloud)?
How can we integrate the development with the shipping (CI/CD, GitOps)?
If we run in the cloud how can we check the costs?
Can wie optimize costs (FinOps)?
How can we monitor and log the system?


## Managed Services
What do we need to achieve the promised readiness?
Do we know the system?
Is montioring, logging, networking setup up?
Do we and the customer know the contacts?


# Limitations / TODOs

# Non-Techical Limitations
The artifacts of the following areas are not yet part of the project:
- No project planning related artifects
- No project management related artifects
- No design and conception related artifects

## Architectural and Technical Compromises
- No Security
- No Personalization
- No Internationalization (i18n)
- No General Architecture documents.
- No unit, integration or end-to-end tests
- No 100% clean separation of concerns (e.g., this repo contains the AI generator script)

# Which Repos belong to the Marcel Know How Project?
- [Marcel Knowhow Main](https://github.com/PRODYNA/marcel_knowhow_main)
- [Marcel Knowhow Frontend](https://github.com/PRODYNA/marcel_knowhow_frontend)
- [Marcel Knowhow Backend](https://github.com/PRODYNA/marcel_knowhow_backend)
- [Marcel Knowhow Database](https://github.com/PRODYNA/marcel_knowhow_db)


# Guide for local tool installation
Please follow the [local setup guide](./docs/local_setup.md) to install the tools needed for the project.