import os
import toml

#load config.toml
cwd = os.getcwd()
path = os.path.join(cwd,'settings','config.toml')
config = toml.load(path)
#add config to locals
locals().update(config)
