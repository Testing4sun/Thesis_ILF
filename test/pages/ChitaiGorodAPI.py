import requests

base_url = "https://web-gate.chitai-gorod.ru/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjkxODk0OTksImlhdCI6MTc0MzI0NDc4MCwiZXhwIjoxNzQzMjQ4MzgwLCJ0eXBlIjoyMH0.AxdTV5Ir-MuiVYSY_ia86nzI3a6qPMRkQud4qslDFJY"


class ChitaiGorodUI:

    def get_projects_list(term: str):
        """
        Эта функция ищет список книг с введенным названием
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{token}",
            "Phrase": "{term}"
        }
        list = requests.get(base_url+'api/v2/search', headers=headers)
        return list.json()
