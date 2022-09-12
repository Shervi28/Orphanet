"""

Credits to CharleyWargnier and his group that were the original creators of the following code.

You can find the code associated with the following repository URL below
|                                  |                                    |
v                                  v                                    v
https://github.com/streamlit/example-app-commenting


"""

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1rkMVLvh3JrBq_tbi4Ho0qjCDAP3vYdNuWOEjYpkJLNU"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
COMMENT_TEMPLATE_MD = """{} - {}
> {}"""