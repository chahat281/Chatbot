{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7fca61db-72bc-4c65-9bfd-9560dfe28667",
   "metadata": {},
   "outputs": [],
   "source": [
    "import zipfile\n",
    "with zipfile.ZipFile('Backend(LLM)-Assignment.zip','r') as zip_ref:\n",
    "    zip_ref.extractall()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d164577c-5ec1-424c-b64c-084e679ec19a",
   "metadata": {},
   "source": [
    "## Load libraries ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "243b13eb-9a07-4b02-8713-89af14ec93e7",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: faiss-cpu in c:\\users\\chahat\\anaconda3\\lib\\site-packages (1.9.0)\n",
      "Requirement already satisfied: numpy<3.0,>=1.25.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from faiss-cpu) (1.26.4)\n",
      "Requirement already satisfied: packaging in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from faiss-cpu) (24.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install faiss-cpu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1740a309-1519-4521-8ce8-e220ff5b4ab3",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: llama-index in c:\\users\\chahat\\anaconda3\\lib\\site-packages (0.12.0)\n",
      "Requirement already satisfied: langchain in c:\\users\\chahat\\anaconda3\\lib\\site-packages (0.3.7)\n",
      "Requirement already satisfied: streamlit in c:\\users\\chahat\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: PyMuPDF in c:\\users\\chahat\\anaconda3\\lib\\site-packages (1.24.13)\n",
      "Requirement already satisfied: llama-index-agent-openai<0.5.0,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.4.0)\n",
      "Requirement already satisfied: llama-index-cli<0.5.0,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.4.0)\n",
      "Requirement already satisfied: llama-index-core<0.13.0,>=0.12.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.12.0)\n",
      "Requirement already satisfied: llama-index-embeddings-openai<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.3.0)\n",
      "Requirement already satisfied: llama-index-indices-managed-llama-cloud>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.6.1)\n",
      "Requirement already satisfied: llama-index-legacy<0.10.0,>=0.9.48 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.9.48.post4)\n",
      "Requirement already satisfied: llama-index-llms-openai<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.3.0)\n",
      "Requirement already satisfied: llama-index-multi-modal-llms-openai<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.3.0)\n",
      "Requirement already satisfied: llama-index-program-openai<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.3.0)\n",
      "Requirement already satisfied: llama-index-question-gen-openai<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.3.0)\n",
      "Requirement already satisfied: llama-index-readers-file<0.5.0,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.4.0)\n",
      "Requirement already satisfied: llama-index-readers-llama-parse>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (0.4.0)\n",
      "Requirement already satisfied: nltk>3.8.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index) (3.9.1)\n",
      "Requirement already satisfied: PyYAML>=5.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (6.0.1)\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (2.0.34)\n",
      "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (3.10.5)\n",
      "Requirement already satisfied: langchain-core<0.4.0,>=0.3.15 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (0.3.19)\n",
      "Requirement already satisfied: langchain-text-splitters<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (0.3.2)\n",
      "Requirement already satisfied: langsmith<0.2.0,>=0.1.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (0.1.143)\n",
      "Requirement already satisfied: numpy<2.0.0,>=1.26.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (1.26.4)\n",
      "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (2.32.3)\n",
      "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain) (8.2.3)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (23.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.11.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: jsonpatch<2.0,>=1.33 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-core<0.4.0,>=0.3.15->langchain) (1.33)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.17->langchain) (0.27.0)\n",
      "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.17->langchain) (3.10.11)\n",
      "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.17->langchain) (1.0.0)\n",
      "Requirement already satisfied: openai>=1.14.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-agent-openai<0.5.0,>=0.4.0->llama-index) (1.54.4)\n",
      "Requirement already satisfied: dataclasses-json in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (0.6.7)\n",
      "Requirement already satisfied: deprecated>=1.2.9.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (1.2.15)\n",
      "Requirement already satisfied: dirtyjson<2.0.0,>=1.0.8 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (1.0.8)\n",
      "Requirement already satisfied: filetype<2.0.0,>=1.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (1.2.0)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (2024.6.1)\n",
      "Requirement already satisfied: nest-asyncio<2.0.0,>=1.5.8 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (1.6.0)\n",
      "Requirement already satisfied: networkx>=3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (3.3)\n",
      "Requirement already satisfied: tiktoken>=0.3.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (0.8.0)\n",
      "Requirement already satisfied: tqdm<5.0.0,>=4.66.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (4.66.5)\n",
      "Requirement already satisfied: typing-inspect>=0.8.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (0.9.0)\n",
      "Requirement already satisfied: wrapt in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-core<0.13.0,>=0.12.0->llama-index) (1.14.1)\n",
      "Requirement already satisfied: llama-cloud>=0.1.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-indices-managed-llama-cloud>=0.4.0->llama-index) (0.1.5)\n",
      "Requirement already satisfied: beautifulsoup4<5.0.0,>=4.12.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-readers-file<0.5.0,>=0.4.0->llama-index) (4.12.3)\n",
      "Requirement already satisfied: pypdf<6.0.0,>=5.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-readers-file<0.5.0,>=0.4.0->llama-index) (5.1.0)\n",
      "Requirement already satisfied: striprtf<0.0.27,>=0.0.26 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-readers-file<0.5.0,>=0.4.0->llama-index) (0.0.26)\n",
      "Requirement already satisfied: llama-parse>=0.5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from llama-index-readers-llama-parse>=0.4.0->llama-index) (0.5.14)\n",
      "Requirement already satisfied: joblib in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nltk>3.8.1->llama-index) (1.4.2)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nltk>3.8.1->llama-index) (2024.9.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.20.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (2024.8.30)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from SQLAlchemy<3,>=1.4->langchain) (3.0.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from beautifulsoup4<5.0.0,>=4.12.3->llama-index-readers-file<0.5.0,>=0.4.0->llama-index) (2.5)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: anyio in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (4.2.0)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.0.2)\n",
      "Requirement already satisfied: sniffio in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.3.0)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (0.14.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.15->langchain) (2.1)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from openai>=1.14.0->llama-index-agent-openai<0.5.0,>=0.4.0->llama-index) (1.9.0)\n",
      "Requirement already satisfied: jiter<1,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from openai>=1.14.0->llama-index-agent-openai<0.5.0,>=0.4.0->llama-index) (0.7.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from typing-inspect>=0.8.0->llama-index-core<0.13.0,>=0.12.0->llama-index) (1.0.0)\n",
      "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from dataclasses-json->llama-index-core<0.13.0,>=0.12.0->llama-index) (3.23.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install llama-index langchain streamlit PyMuPDF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f9253589-515b-4936-ac56-df768ff67225",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: langchain-community in c:\\users\\chahat\\anaconda3\\lib\\site-packages (0.3.7)\n",
      "Requirement already satisfied: PyYAML>=5.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (6.0.1)\n",
      "Requirement already satisfied: SQLAlchemy<2.0.36,>=1.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (2.0.34)\n",
      "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (3.10.5)\n",
      "Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (0.6.7)\n",
      "Requirement already satisfied: httpx-sse<0.5.0,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (0.4.0)\n",
      "Requirement already satisfied: langchain<0.4.0,>=0.3.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (0.3.7)\n",
      "Requirement already satisfied: langchain-core<0.4.0,>=0.3.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (0.3.19)\n",
      "Requirement already satisfied: langsmith<0.2.0,>=0.1.125 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (0.1.143)\n",
      "Requirement already satisfied: numpy<2.0.0,>=1.26.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (1.26.4)\n",
      "Requirement already satisfied: pydantic-settings<3.0.0,>=2.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (2.6.1)\n",
      "Requirement already satisfied: requests<3,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (2.32.3)\n",
      "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-community) (8.2.3)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (2.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (23.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.11.0)\n",
      "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from dataclasses-json<0.7,>=0.5.7->langchain-community) (3.23.1)\n",
      "Requirement already satisfied: typing-inspect<1,>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from dataclasses-json<0.7,>=0.5.7->langchain-community) (0.9.0)\n",
      "Requirement already satisfied: langchain-text-splitters<0.4.0,>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain<0.4.0,>=0.3.7->langchain-community) (0.3.2)\n",
      "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain<0.4.0,>=0.3.7->langchain-community) (2.8.2)\n",
      "Requirement already satisfied: jsonpatch<2.0,>=1.33 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-core<0.4.0,>=0.3.17->langchain-community) (1.33)\n",
      "Requirement already satisfied: packaging<25,>=23.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-core<0.4.0,>=0.3.17->langchain-community) (24.1)\n",
      "Requirement already satisfied: typing-extensions>=4.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langchain-core<0.4.0,>=0.3.17->langchain-community) (4.11.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.125->langchain-community) (0.27.0)\n",
      "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.125->langchain-community) (3.10.11)\n",
      "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from langsmith<0.2.0,>=0.1.125->langchain-community) (1.0.0)\n",
      "Requirement already satisfied: python-dotenv>=0.21.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pydantic-settings<3.0.0,>=2.4.0->langchain-community) (0.21.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain-community) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain-community) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain-community) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain-community) (2024.8.30)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from SQLAlchemy<2.0.36,>=1.4->langchain-community) (3.0.1)\n",
      "Requirement already satisfied: anyio in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.125->langchain-community) (4.2.0)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.125->langchain-community) (1.0.2)\n",
      "Requirement already satisfied: sniffio in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.125->langchain-community) (1.3.0)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.125->langchain-community) (0.14.0)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.17->langchain-community) (2.1)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain<0.4.0,>=0.3.7->langchain-community) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain<0.4.0,>=0.3.7->langchain-community) (2.20.1)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain-community) (1.0.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install -U langchain-community"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e2ad6f8b-e512-495f-8441-dc0c179fff1e",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: sentence-transformers in c:\\users\\chahat\\anaconda3\\lib\\site-packages (3.3.1)\n",
      "Requirement already satisfied: transformers<5.0.0,>=4.41.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (4.46.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (4.66.5)\n",
      "Requirement already satisfied: torch>=1.11.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (2.5.1)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.5.1)\n",
      "Requirement already satisfied: scipy in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.13.1)\n",
      "Requirement already satisfied: huggingface-hub>=0.20.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (0.26.2)\n",
      "Requirement already satisfied: Pillow in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sentence-transformers) (10.4.0)\n",
      "Requirement already satisfied: filelock in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (3.13.1)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (2024.6.1)\n",
      "Requirement already satisfied: packaging>=20.9 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (24.1)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (6.0.1)\n",
      "Requirement already satisfied: requests in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (2.32.3)\n",
      "Requirement already satisfied: typing-extensions>=3.7.4.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.20.0->sentence-transformers) (4.11.0)\n",
      "Requirement already satisfied: networkx in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.1.4)\n",
      "Requirement already satisfied: setuptools in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (75.1.0)\n",
      "Requirement already satisfied: sympy==1.13.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (1.13.1)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from sympy==1.13.1->torch>=1.11.0->sentence-transformers) (1.3.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from tqdm->sentence-transformers) (0.4.6)\n",
      "Requirement already satisfied: numpy>=1.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (1.26.4)\n",
      "Requirement already satisfied: regex!=2019.12.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (2024.9.11)\n",
      "Requirement already satisfied: tokenizers<0.21,>=0.20 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (0.20.3)\n",
      "Requirement already satisfied: safetensors>=0.4.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (0.4.5)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from scikit-learn->sentence-transformers) (1.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from scikit-learn->sentence-transformers) (3.5.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jinja2->torch>=1.11.0->sentence-transformers) (2.1.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.20.0->sentence-transformers) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.20.0->sentence-transformers) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.20.0->sentence-transformers) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.20.0->sentence-transformers) (2024.8.30)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install sentence-transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a94c4674-9863-4045-8103-192aa19fe15a",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: ipywidgets in c:\\users\\chahat\\anaconda3\\lib\\site-packages (7.8.1)\n",
      "Requirement already satisfied: comm>=0.1.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (0.2.1)\n",
      "Requirement already satisfied: ipython-genutils~=0.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (0.2.0)\n",
      "Requirement already satisfied: traitlets>=4.3.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (5.14.3)\n",
      "Requirement already satisfied: widgetsnbextension~=3.6.6 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (3.6.6)\n",
      "Requirement already satisfied: ipython>=4.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (8.27.0)\n",
      "Requirement already satisfied: jupyterlab-widgets<3,>=1.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipywidgets) (1.0.0)\n",
      "Requirement already satisfied: decorator in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (5.1.1)\n",
      "Requirement already satisfied: jedi>=0.16 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (0.19.1)\n",
      "Requirement already satisfied: matplotlib-inline in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (0.1.6)\n",
      "Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (3.0.43)\n",
      "Requirement already satisfied: pygments>=2.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (2.15.1)\n",
      "Requirement already satisfied: stack-data in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (0.2.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipython>=4.0.0->ipywidgets) (0.4.6)\n",
      "Requirement already satisfied: notebook>=4.4.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from widgetsnbextension~=3.6.6->ipywidgets) (7.2.2)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jedi>=0.16->ipython>=4.0.0->ipywidgets) (0.8.3)\n",
      "Requirement already satisfied: jupyter-server<3,>=2.4.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.14.1)\n",
      "Requirement already satisfied: jupyterlab-server<3,>=2.27.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.27.3)\n",
      "Requirement already satisfied: jupyterlab<4.3,>=4.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (4.2.5)\n",
      "Requirement already satisfied: notebook-shim<0.3,>=0.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.2.3)\n",
      "Requirement already satisfied: tornado>=6.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (6.4.1)\n",
      "Requirement already satisfied: wcwidth in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from prompt-toolkit<3.1.0,>=3.0.41->ipython>=4.0.0->ipywidgets) (0.2.5)\n",
      "Requirement already satisfied: executing in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from stack-data->ipython>=4.0.0->ipywidgets) (0.8.3)\n",
      "Requirement already satisfied: asttokens in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from stack-data->ipython>=4.0.0->ipywidgets) (2.0.5)\n",
      "Requirement already satisfied: pure-eval in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from stack-data->ipython>=4.0.0->ipywidgets) (0.2.2)\n",
      "Requirement already satisfied: anyio>=3.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (4.2.0)\n",
      "Requirement already satisfied: argon2-cffi>=21.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (21.3.0)\n",
      "Requirement already satisfied: jinja2>=3.0.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (3.1.4)\n",
      "Requirement already satisfied: jupyter-client>=7.4.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (8.6.0)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (5.7.2)\n",
      "Requirement already satisfied: jupyter-events>=0.9.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.10.0)\n",
      "Requirement already satisfied: jupyter-server-terminals>=0.4.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.4.4)\n",
      "Requirement already satisfied: nbconvert>=6.4.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (7.16.4)\n",
      "Requirement already satisfied: nbformat>=5.3.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (5.10.4)\n",
      "Requirement already satisfied: overrides>=5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (7.4.0)\n",
      "Requirement already satisfied: packaging>=22.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (24.1)\n",
      "Requirement already satisfied: prometheus-client>=0.9 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.14.1)\n",
      "Requirement already satisfied: pywinpty>=2.0.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.0.10)\n",
      "Requirement already satisfied: pyzmq>=24 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (25.1.2)\n",
      "Requirement already satisfied: send2trash>=1.8.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.8.2)\n",
      "Requirement already satisfied: terminado>=0.8.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.17.1)\n",
      "Requirement already satisfied: websocket-client>=1.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.8.0)\n",
      "Requirement already satisfied: async-lru>=1.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.0.4)\n",
      "Requirement already satisfied: httpx>=0.25.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.27.0)\n",
      "Requirement already satisfied: ipykernel>=6.5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (6.28.0)\n",
      "Requirement already satisfied: jupyter-lsp>=2.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.2.0)\n",
      "Requirement already satisfied: setuptools>=40.1.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (75.1.0)\n",
      "Requirement already satisfied: babel>=2.10 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.11.0)\n",
      "Requirement already satisfied: json5>=0.9.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.9.6)\n",
      "Requirement already satisfied: jsonschema>=4.18.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (4.23.0)\n",
      "Requirement already satisfied: requests>=2.31 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.32.3)\n",
      "Requirement already satisfied: six in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from asttokens->stack-data->ipython>=4.0.0->ipywidgets) (1.16.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (3.7)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.3.0)\n",
      "Requirement already satisfied: argon2-cffi-bindings in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (21.2.0)\n",
      "Requirement already satisfied: pytz>=2015.7 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from babel>=2.10->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2024.1)\n",
      "Requirement already satisfied: certifi in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx>=0.25.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2024.8.30)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpx>=0.25.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx>=0.25.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.14.0)\n",
      "Requirement already satisfied: debugpy>=1.6.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipykernel>=6.5.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.6.7)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipykernel>=6.5.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.6.0)\n",
      "Requirement already satisfied: psutil in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from ipykernel>=6.5.0->jupyterlab<4.3,>=4.2.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (5.9.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jinja2>=3.0.3->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.10.6)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-client>=7.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.9.0.post0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-core!=5.0.*,>=4.12->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (3.10.0)\n",
      "Requirement already satisfied: pywin32>=300 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-core!=5.0.*,>=4.12->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (305.1)\n",
      "Requirement already satisfied: python-json-logger>=2.0.4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.0.7)\n",
      "Requirement already satisfied: pyyaml>=5.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (6.0.1)\n",
      "Requirement already satisfied: rfc3339-validator in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.1.4)\n",
      "Requirement already satisfied: rfc3986-validator>=0.1.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.1.1)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (4.12.3)\n",
      "Requirement already satisfied: bleach!=5.0.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (4.1.0)\n",
      "Requirement already satisfied: defusedxml in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.7.1)\n",
      "Requirement already satisfied: jupyterlab-pygments in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.1.2)\n",
      "Requirement already satisfied: mistune<4,>=2.0.3 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.0.4)\n",
      "Requirement already satisfied: nbclient>=0.5.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.8.0)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.5.0)\n",
      "Requirement already satisfied: tinycss2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.2.1)\n",
      "Requirement already satisfied: fastjsonschema>=2.15 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.16.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests>=2.31->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (3.3.2)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from requests>=2.31->jupyterlab-server<3,>=2.27.1->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.2.3)\n",
      "Requirement already satisfied: webencodings in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from bleach!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (0.5.1)\n",
      "Requirement already satisfied: fqdn in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.5.1)\n",
      "Requirement already satisfied: isoduration in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (20.11.0)\n",
      "Requirement already satisfied: jsonpointer>1.13 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.1)\n",
      "Requirement already satisfied: uri-template in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.3.0)\n",
      "Requirement already satisfied: webcolors>=24.6.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (24.11.1)\n",
      "Requirement already satisfied: cffi>=1.0.1 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.17.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.5)\n",
      "Requirement already satisfied: pycparser in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (2.21)\n",
      "Requirement already satisfied: arrow>=0.15.0 in c:\\users\\chahat\\anaconda3\\lib\\site-packages (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.9.0->jupyter-server<3,>=2.4.0->notebook>=4.4.1->widgetsnbextension~=3.6.6->ipywidgets) (1.2.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install ipywidgets"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e04e762d-94b1-4cc1-88c6-57386e71f9f5",
   "metadata": {},
   "source": [
    "## Parse PDFs and Create Embeddings ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "34ed0283-15ed-4cf5-a752-ed93de315ee1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FAISS index created with 3 documents.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import fitz  # PyMuPDF\n",
    "from langchain.embeddings import HuggingFaceEmbeddings\n",
    "import faiss\n",
    "import numpy as np\n",
    "\n",
    "# Path to your PDFs\n",
    "pdf_folder = \"pdf files\"\n",
    "\n",
    "def extract_text_from_pdf(pdf_path):\n",
    "    \"\"\"Extract text from a PDF file.\"\"\"\n",
    "    pdf = fitz.open(pdf_path)\n",
    "    text = \"\"\n",
    "    for page in pdf:\n",
    "        text += page.get_text()\n",
    "    return text\n",
    "\n",
    "# Parse all PDFs\n",
    "documents = {}\n",
    "for pdf_file in os.listdir(pdf_folder):\n",
    "    if pdf_file.endswith(\".pdf\"):\n",
    "        pdf_path = os.path.join(pdf_folder, pdf_file)\n",
    "        documents[pdf_file] = extract_text_from_pdf(pdf_path)\n",
    "\n",
    "# Initialize embeddings model\n",
    "embeddings_model = HuggingFaceEmbeddings(model_name=\"sentence-transformers/all-MiniLM-L6-v2\")\n",
    "\n",
    "# Generate embeddings and create a FAISS index\n",
    "texts = list(documents.values())\n",
    "names = list(documents.keys())\n",
    "\n",
    "\n",
    "# Generate embeddings and convert to NumPy array\n",
    "embeddings = np.array([embeddings_model.embed_query(text) for text in texts])\n",
    "\n",
    "# Create FAISS index\n",
    "dimension = embeddings.shape[1]\n",
    "faiss_index = faiss.IndexFlatL2(dimension)\n",
    "faiss_index.add(embeddings)\n",
    "\n",
    "print(f\"FAISS index created with {faiss_index.ntotal} documents.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "365c8a05-daca-4f4c-adf8-2062ae3b2455",
   "metadata": {},
   "source": [
    "## Query the Vector Store ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "36a568b7-0ec2-453e-8274-2ea10c4c59bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Document: tsla-20231231-gen.pdf, Similarity Score: 1.634941816329956\n",
      "Document: uber-10-k-2023.pdf, Similarity Score: 1.6772297620773315\n",
      "Document: goog-10-k-2023 (1).pdf, Similarity Score: 1.945066213607788\n"
     ]
    }
   ],
   "source": [
    "def query_faiss_index(query, top_k=3):\n",
    "    \"\"\"Retrieve the most relevant documents from the FAISS index.\"\"\"\n",
    "    query_vector = np.array(embeddings_model.embed_query(query)).reshape(1, -1)\n",
    "    \n",
    "    # Ensure top_k does not exceed the number of documents\n",
    "    top_k = min(top_k, faiss_index.ntotal)\n",
    "    \n",
    "    distances, indices = faiss_index.search(query_vector, top_k)\n",
    "    results = []\n",
    "    \n",
    "    for i in range(len(indices[0])):\n",
    "        idx = indices[0][i]\n",
    "        if idx != -1:  # Ensure valid index\n",
    "            results.append((names[idx], distances[0][i]))\n",
    "    \n",
    "    return results\n",
    "\n",
    "# Test the function\n",
    "query = \"What are the risk factors associated with Google and Tesla?\"\n",
    "results = query_faiss_index(query)\n",
    "for name, distance in results:\n",
    "    print(f\"Document: {name}, Similarity Score: {distance}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8bce8382-3937-4e22-bd2a-51767683805c",
   "metadata": {},
   "source": [
    "## Build the Chatbot ##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d09165d8-2d94-4db0-a334-479b5ab1756a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-19 10:01:39.894 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Chahat\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-11-19 10:01:39.894 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"Content Engine: Compare and Analyze PDFs\")\n",
    "st.write(\"Upload your PDFs, query their content, and find comparative insights.\")\n",
    "\n",
    "# Upload PDFs\n",
    "uploaded_files = st.file_uploader(\"Upload PDF documents\", type=\"pdf\", accept_multiple_files=True)\n",
    "if uploaded_files:\n",
    "    for uploaded_file in uploaded_files:\n",
    "        documents[uploaded_file.name] = extract_text_from_pdf(uploaded_file)\n",
    "        texts = list(documents.values())\n",
    "        names = list(documents.keys())\n",
    "        embeddings = [embeddings_model.embed_query(text) for text in texts]\n",
    "        embeddings = np.array(embeddings)\n",
    "        faiss_index.add(embeddings)\n",
    "\n",
    "# Query\n",
    "user_query = st.text_input(\"Enter your query:\")\n",
    "if user_query:\n",
    "    results = query_faiss_index(user_query)\n",
    "    st.write(\"Results:\")\n",
    "    for name, distance in results:\n",
    "        st.write(f\"Document: {name}, Similarity Score: {distance}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c015e724-212e-4491-93d7-ebb5d9ebd917",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "b9a04c6b-2b1b-4911-948f-334e36d1911c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "2b018e2d-3818-49ae-91ca-432905015459",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "165a0f14-f2bb-4d9a-a95e-16eb6b3567c3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "af0d0f56-1cb5-4a77-b9b3-6160295af5c4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "4528be44-4a17-4903-a3ef-dda901d3b881",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "701bc0f8-95f7-4c32-b638-b156cf0eeb56",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "52b358a2-c42e-4938-bac6-ec0f375a2188",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "fa243b63-272c-4e85-be80-67d77d8060c6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8537c41d-5402-41be-ae45-82d0c873a104",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c422f618-f1b9-4587-bc6d-a317483ef025",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "4b963804-2df3-465e-bc9a-5424c68bbdca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
