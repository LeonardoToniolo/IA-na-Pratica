#import
from dotenv import load_dotenv
import json
import os
from datetime import datetime

import yfinance as yf
from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults

import streamlit as st

load_dotenv()

# creating Yahoo finance tool
def fetch_stock_price(ticket):
    stock = yf.download(ticket, start='2023-08-19', end='2024-08-19')
    return stock

yahoo_finance_tools = Tool(
    name="Yahoo Finance Tools",
    description="Fetches stock prices for {ticket} from the last year about a specific company from Yahoo Finance API",
    func= lambda ticket: fetch_stock_price(ticket)
)

# importing openai llm - gpt
os.environ['OPENAI_API_KEY'] = st.secrets('OPENAI_API_KEY')
llm = ChatOpenAI(model='gpt-3.5-turbo')

stockPriceAnalyst = Agent(
    role="Senior Stock Price Analyst",
    goal="Find the {ticket} stock price and analyses trends",
    backstory="""You're a highly experienced in analyzing the price of an specific stock 
    and make predictions about its future price.""",
    verbose=True,
    llm= llm,
    max_iter= 5,
    memory= True,
    tools=[yahoo_finance_tools],
    allow_delegation= False
)

getStockPrice = Task(
    description= "Analyze the stock {ticket} price history and create a trend analyses of up, down or sideways",
    expected_output= """ Specify the current stock price - up, down or sideways.
    eg. stock='AAPL, price UP' 
""",
    agent= stockPriceAnalyst
)

# importing search tool
search_tool = DuckDuckGoSearchResults(backend='news', num_results=10)

newsAnalyst = Agent(
    role= "Stock News Analyst",
    goal= """ Create a short summary of the market news related to the stock {ticket} company. 
    Specify the content trend - up, down or sideways with the news content.
    For each request stock asset, specify a number between 0 and 100, where 0 is extreme fear and 100 is 
    extreme greed.
    """,
    backstory=""" You're highly experienced in analyzing the market trends and news and have tracked assets for 
    more than 10 years. You're also master lever analyst in the traditional markets and have deep understanding of
    human psychology.

    You understand news, their titles and information, but you look those with a healthy dose of skepticism.
    You consider also the source of the news article
""",
    verbose=True,
    llm= llm,
    max_iter= 10,
    memory= True,
    tools=[search_tool],
    allow_delegation= False
)

get_news= Task(
    description= f"""Take the stock and always include BTC to it (if not requested).
    Use the search tool to search each one individually.

    The current date is {datetime.now()}.

    Compose the results into a helpfull report
    """,
    expected_output= """ A summary of the overall market and one sentence summary for each request asset.
Include a fear/greed score for each asset based on the news. Use format:
<STOCK ASSET>
<SUMMARY BASED ON NEWS>
<TREND PREDICTIONS>
<FEAR/GREED SCORE>  
""",
    agent= newsAnalyst
)

stockAnalystWrite= Agent(
    role= "Senior Stock Analyst Writer",
    goal= """ Analyze the trends price and news so you can write an insightfull compelling and informative 3 paragraph long newsletter based on the stock report 
    and price trend.
    """,
    backstory=""" You're wiedly accepted as the best stock analyst in the market. You Undestand complex concepts and
    create compelling stories and narratives that resonate with wider audiences.

    You understand macro factors and combine multiple theories - eg. cycle theory and fundamental analyses.
    You're able to hold multiple opnions when analyzing anything.
    """,
    verbose=True,
    llm= llm,
    max_iter= 5,
    memory= True,
    allow_delegation= True,
    tools=[search_tool]
)

writeAnalysis = Task(
    description= """ Use the stock price trend and the stock price news report to create analysis and write the newsletter 
    about the {ticket} company that is brief and highlights the most important points.
    Focus on the stock price trend, news and fear/greed score. what are the near future considerations?

    include previous analyses of stock trend and news summary.
    """,
    expected_output= """ And eloquent 3 paragraphs newsletter formated as markdown in an easy readable manner.it should contain:

    - 3 bullets executive summary 
    - Introduction - set the overall picture and spike up the interest 
    - main part provides the meat of the analysis including the news summary and fear/greed scores
    - summary - key facts and concrete future trend predictions - up, down or sideways.
""",
    agent= stockAnalystWrite,
    context=[getStockPrice, get_news]
)

crew = Crew(
    agents=[stockPriceAnalyst, newsAnalyst, stockAnalystWrite],
    tasks=[getStockPrice, get_news, writeAnalysis],
    verbose=True,
    process= Process.hierarchical,
    full_output=True,
    share_crew=False, 
    manager_llm=llm,
    max_iter=15
)

# results = crew.kickoff(inputs={'ticket': 'AAPL'})

with st.sidebar:
    st.header('Enter the stock to research')

    with st.form(key='research_form'):
        topic = st.text_input("select the ticket")
        submit_button = st.form_submit_button(label='Run Research')


if submit_button:
    if not topic:
        st.error("Please fill the ticket field")
    else: 
        results = crew.kickoff(inputs={'ticket': topic})

        st.subheader("Result of your research:")
        st.write(results["final_output"])