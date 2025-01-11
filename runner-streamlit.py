import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Especificações de GPU.py"]
sys.exit(stcli.main())
