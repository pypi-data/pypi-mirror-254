# supported regions: https://github.com/deedy5/duckduckgo_search#regions
from duckduckgo_search import DDGS

with DDGS() as ddgs:
   for r in ddgs.text('السعودية', region='xa-ar', safesearch='off', timelimit='y', max_results=10):
    #  print(r)
     pass

# https://python.langchain.com/docs/integrations/tools/ddg
# from langchain.utilities import DuckDuckGoSearchAPIWrapper 
# from langchain.tools import DuckDuckGoSearchRun


from duckduckgo_search import DDGS

with DDGS() as ddgs:
    for r in ddgs.answers("sun"):
        # print(r)
        pass


# Searching for pdf files
with DDGS() as ddgs:
    for r in ddgs.text('saudi arabia filetype:pdf', region='xa-ar', safesearch='off', timelimit='y', max_results=10):
        print(r)