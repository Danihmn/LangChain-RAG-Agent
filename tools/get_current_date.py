import datetime

from langchain_core.tools import tool


@tool(
    "get_current_date",
    description="Get current date, in format 'today is YYYY-mm-dd'",
    response_format="content"
)
def get_current_date():
    date = datetime.datetime.now()
    return "today is " + date.strftime("%Y-%m-%d")
