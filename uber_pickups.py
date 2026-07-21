{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOq5yJm5dlMaLVzasn2QRD4"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LIjQ-9ZMR0_l",
        "outputId": "3c88f6b5-88d2-42f0-cf37-ee7431ad672a"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.59.2-py3-none-any.whl.metadata (9.6 kB)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.4.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.51)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.2)\n",
            "Requirement already satisfied: pandas<4,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow<25,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.16.0)\n",
            "Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.3.1)\n",
            "Requirement already satisfied: uvicorn>=0.30.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.51.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.8.0)\n",
            "Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.14.2)\n",
            "Requirement already satisfied: python-multipart>=0.0.10 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.0.32)\n",
            "Requirement already satisfied: websockets>=12.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (15.0.1)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.24.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio>=4.0.0->streamlit) (3.18)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2026.3)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.9)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.6.17)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.12/dist-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2026.6.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.59.2-py3-none-any.whl (10.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.3/10.3 MB\u001b[0m \u001b[31m75.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.4/11.4 MB\u001b[0m \u001b[31m95.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.3 streamlit-1.59.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "1lnuZHPkRUD1"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('Uber pickups in NYC')\n",
        "\n",
        "DATE_COLUMN = 'date/time'\n",
        "DATA_URL = ('https://s3-us-west-2.amazonaws.com/'\n",
        "            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')\n",
        "\n",
        "@st.cache_data\n",
        "def load_data(nrows):\n",
        "    data = pd.read_csv(DATA_URL, nrows=nrows)\n",
        "    lowercase = lambda x: str(x).lower()\n",
        "    data.rename(lowercase, axis='columns', inplace=True)\n",
        "    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])\n",
        "    return data\n",
        "\n",
        "data_load_state = st.text('Loading data...')\n",
        "data = load_data(10000)\n",
        "data_load_state.text(\"Done! (using st.cache_data)\")\n",
        "\n",
        "if st.checkbox('Show raw data'):\n",
        "    st.subheader('Raw data')\n",
        "    st.write(data)\n",
        "\n",
        "st.subheader('Number of pickups by hour')\n",
        "hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]\n",
        "st.bar_chart(hist_values)\n",
        "\n",
        "# Some number in the range 0-23\n",
        "hour_to_filter = st.slider('hour', 0, 23, 17)\n",
        "filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]\n",
        "\n",
        "st.subheader('Map of all pickups at %s:00' % hour_to_filter)\n",
        "st.map(filtered_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XSN-R3CRRdmj",
        "outputId": "ffe996fa-2047-446f-b173-80c685fe5ed0"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-07-21 20:05:09.979 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.143 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2026-07-21 20:05:10.144 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.145 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.149 No runtime found, using MemoryCacheStorageManager\n",
            "2026-07-21 20:05:10.151 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.153 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.154 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.155 No runtime found, using MemoryCacheStorageManager\n",
            "2026-07-21 20:05:10.157 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.839 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.840 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.841 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.843 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.843 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.845 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.847 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.848 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.850 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:10.852 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.923 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.924 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.925 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.927 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.929 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.931 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.932 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.933 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.937 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.939 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.940 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.953 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.954 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-07-21 20:05:12.955 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    }
  ]
}