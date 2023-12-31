import requests

def search_open_redirect_bugs(query, url):
    access_token = '412543438'

    headers = {'Authorization': f'token {412543438}'}
    base_url = 'https://api.github.com'

    search_url = f'{base_url}/search/code?q={query}+in:file+language:python+repo:{url}'
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        total_count = json_response['total_count']
        items = json_response['items']

        print(f'Total hasil: {total_count}\n')

        for item in items:
            repo_name = item['repository']['full_name']
            file_name = item['name']
            file_path = item['path']
            file_url = item['html_url']

            print(f'Repo: {repo_name}')
            print(f'File: {file_path} ({file_name})')
            print(f'URL: {file_url}\n')
    else:
        print(f'Permintaan gagal dengan kode status: {response.status_code}')


search_query = 'open+redirect'


target_url = input('Masukkan URL web yang ingin dicari bug open redirect-nya: ')

search_open_redirect_bugs(search_query, target_url)
