# maunium-stickerpicker - A fast and simple Matrix sticker picker widget.
# Copyright (C) 2020 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import argparse
from .pack import cmd


parser = argparse.ArgumentParser()

parser.add_argument("--config",
                    help="Path to JSON file with Matrix homeserver and access_token",
                    type=str,
                    default="config.json",
                    metavar="file")

parser.add_argument("--title",
                    help="Override the sticker pack displayname",
                    type=str,
                    metavar="title")

parser.add_argument("--id",
                    help="Override the sticker pack ID",
                    type=str,
                    metavar="id")

parser.add_argument("--add-to-index",
                    help="Sticker picker pack directory (usually 'web/packs/')",
                    type=str,
                    metavar="path")

parser.add_argument("path",
                    help="Path to the sticker pack directory",
                    type=str)


if __name__ == "__main__":
    cmd()
