import re
from modules import helpers
from functools import *
from pprint import pp

versions = helpers.getVersions()
latestVersion = helpers.getLatestVersion(versions)

includedFiles = [
  ".html",
  ".htm",
]

excludedFolders = [
  ".git",
  latestVersion,
]

print("Adding version in the titles of archived versions")
for version in filter(lambda version : version != latestVersion, versions):
  replacementMap = [
    (r"(<title.*?>)", r"\g<1>" + re.escape(version) + r" - "),
    (r"(<meta[^>]*?property=\"og:title\"[^>]*?content=\")([^>]*?>)", r"\g<1>" + re.escape(version) + r" - \g<2>"),
  ]

  helpers.findReplaceRegex(f"./{version}", replacementMap, includedFiles, excludedFolders)