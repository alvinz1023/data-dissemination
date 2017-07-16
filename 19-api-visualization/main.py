import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call for python projects ordered by stars; store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)

print("Status Code: ", response.status_code)

# Store API response in a variable
response_d = response.json()
repo_dics = response_d['items']

# Retrieve information from the repositories
names, stars = [], []
for repo_dic in repo_dics:
    names.append(repo_dic['name'])
    stars.append(repo_dic['stargazers_count'])

# Create visualization
style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects with Most Stars on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_stars.svg')
