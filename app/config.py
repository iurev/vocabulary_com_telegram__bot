import yaml
from deepmerge import Merger
import os

config_path = "{}/config".format(os.getcwd())

default = yaml.load(open("{}/default.yml".format(config_path)))
try:
    private = yaml.load(open("{}/private.yml".format(config_path)))
except:
    raise Exception("Create config/private.yml to set up your config")

my_merger = Merger(
    # pass in a list of tuple, with the
    # strategies you are looking to apply
    # to each type.
    [
        (list, ["append"]),
        (dict, ["merge"])
    ],
    # next, choose the fallback strategies,
    # applied to all other types:
    ["override"],
    # finally, choose the strategies in
    # the case where the types conflict:
    ["override"]
)


config = my_merger.merge(default, private)
