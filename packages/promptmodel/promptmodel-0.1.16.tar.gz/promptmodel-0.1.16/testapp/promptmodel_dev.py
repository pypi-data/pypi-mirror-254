"""This single file is needed to build the DevApp development dashboard."""

from promptmodel import DevApp

# Example imports
# from <dirname> import <objectname>
from main import dev as main_client

app = DevApp()

# Example usage
# This is needed to integrate your codebase with the prompt engineering dashboard
# app.include_client(<objectname>)
app.include_client(main_client)