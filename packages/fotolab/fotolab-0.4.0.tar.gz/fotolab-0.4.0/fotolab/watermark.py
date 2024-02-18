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

"""Watermark subcommand."""

import argparse
import logging
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFont

log = logging.getLogger(__name__)

POSITIONS = ["top-left", "top-right", "bottom-left", "bottom-right"]


def build_subparser(subparsers) -> None:
    """Build the subparser."""
    watermark_parser = subparsers.add_parser(
        "watermark", help="watermark an image"
    )

    watermark_parser.set_defaults(func=run)

    watermark_parser.add_argument(
        dest="image_filename",
        help="set the image filename",
        type=str,
        default=None,
        metavar="IMAGE_FILENAME",
    )

    watermark_parser.add_argument(
        "-t",
        "--text",
        dest="text",
        help="set the watermark text (default: '%(default)s')",
        type=str,
        default="kianmeng.org",
        metavar="WATERMARK_TEXT",
    )

    watermark_parser.add_argument(
        "-p",
        "--position",
        dest="position",
        choices=POSITIONS,
        help="set position of the watermark text (default: '%(default)s')",
        default="bottom-left",
    )

    watermark_parser.add_argument(
        "-fs",
        "--font-size",
        dest="font_size",
        type=int,
        default=12,
        help="set the font size of watermark text (default: '%(default)s')",
        metavar="FONT_SIZE",
    )

    watermark_parser.add_argument(
        "-fc",
        "--font-color",
        dest="font_color",
        type=str,
        default="white",
        help="set the font color of watermark text (default: '%(default)s')",
        metavar="FONT_COLOR",
    )

    watermark_parser.add_argument(
        "-ow",
        "--outline-width",
        dest="outline_width",
        type=int,
        default=2,
        help=(
            "set the outline width of the watermark text "
            "(default: '%(default)s')"
        ),
        metavar="OUTLINE_WIDTH",
    )

    watermark_parser.add_argument(
        "-oc",
        "--outline-color",
        dest="outline_color",
        type=str,
        default="black",
        help=(
            "set the outline color of the watermark text "
            "(default: '%(default)s')"
        ),
        metavar="OUTLINE_COLOR",
    )


def run(args: argparse.Namespace) -> None:
    """Run watermark subcommand."""
    log.debug(args)

    image_file = Path(args.image_filename)

    original_image = Image.open(args.image_filename)
    watermarked_image = original_image.copy()

    draw = ImageDraw.Draw(watermarked_image)

    font = ImageFont.truetype("arial.ttf", args.font_size)

    (left, top, right, bottom) = draw.textbbox(
        xy=(0, 0), text=args.text, font=font
    )
    text_width = right - left
    text_height = bottom - top
    (position_x, position_y) = calculate_position(
        watermarked_image, text_width, text_height, args.position
    )

    draw.text(
        (position_x, position_y),
        args.text,
        font=font,
        fill=ImageColor.getrgb(args.font_color),
        stroke_width=args.outline_width,
        stroke_fill=ImageColor.getrgb(args.outline_color),
    )

    if args.overwrite:
        new_filename = image_file.with_name(image_file.name)
    else:
        new_filename = image_file.with_name(f"watermark_{image_file.name}")

    watermarked_image.save(new_filename)


def calculate_position(image, text_width, text_height, position) -> tuple:
    """Calculate the boundary coordinates of the watermark text."""
    padding = 10
    if position == "top-left":
        position_x = 0 + padding
        position_y = 0 + padding
    elif position == "top-right":
        position_x = image.width - text_width - padding
        position_y = 0 + padding
    elif position == "bottom-left":
        position_x = 0 + padding
        position_y = image.height - text_height - padding
    elif position == "bottom-right":
        position_x = image.width - text_width - padding
        position_y = image.height - text_height - padding

    return (position_x, position_y)
