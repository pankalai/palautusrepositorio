from urllib import request
from project import Project
import toml


class ProjectReader:
	def __init__(self, url):
		self._url = url

	def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
		content = request.urlopen(self._url).read().decode("utf-8")
		content_dict = toml.loads(content)

		name = content_dict['tool']['poetry']['name']
		desc = content_dict['tool']['poetry']['description']
		lic = content_dict['tool']['poetry']['license']
		auth = content_dict['tool']['poetry']['authors']
		depend = list(content_dict['tool']['poetry']['dependencies'].keys())
		dev_depend = list(content_dict['tool']['poetry']['group']['dev']['dependencies'].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
		return Project(name, desc, lic, auth, depend, dev_depend)
