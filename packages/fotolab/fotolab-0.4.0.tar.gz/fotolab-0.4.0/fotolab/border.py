# Copyright (C) 2024 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Border subcommand."""

import argparse
import logging
from pathlib import Path

from PIL import Image, ImageColor, ImageOps

log = logging.getLogger(__name__)


def build_subparser(subparsers) -> None:
    """Build the subparser."""
    border_parser = subparsers.add_parser("border", help="add border to image")

    border_parser.set_defaults(func=run)

    border_parser.add_argument(
        dest="image_filename",
        help="set the image filename",
        type=str,
        default=None,
        metavar="IMAGE_FILENAME",
    )

    border_parser.add_argument(
        "-c",
        "--color",
        dest="color",
        type=str,
        default="black",
        help="set the color of border (default: '%(default)s')",
        metavar="COLOR",
    )

    border_parser.add_argument(
        "-w",
        "--width",
        dest="width",
        type=str,
        default=10,
        help="set the width of border (default: '%(default)s')",
        metavar="WIDTH",
    )


def run(args: argparse.Namespace) -> None:
    """Run border subcommand."""
    log.debug(args)

    image_file = Path(args.image_filename)

    original_image = Image.open(args.image_filename)

    bordered_image = ImageOps.expand(
        original_image, border=args.width, fill=ImageColor.getrgb(args.color)
    )

    if args.overwrite:
        new_filename = image_file.with_name(image_file.name)
    else:
        new_filename = image_file.with_name(f"border_{image_file.name}")

    bordered_image.save(new_filename)
