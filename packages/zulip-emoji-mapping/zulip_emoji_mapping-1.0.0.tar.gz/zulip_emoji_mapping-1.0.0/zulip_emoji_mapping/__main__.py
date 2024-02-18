from typing import NewType
from .emoji_names import EMOJI_NAME_MAPS

Emoji = NewType("Emoji", str)
EmojiName = NewType("EmojiName", str)


class EmojiNotFound(Exception): ...


class ZulipEmojiMapping:
    @staticmethod
    def get_emoji_name(emoji: Emoji) -> EmojiName | None:
        """Get Zulip's emoji name

        Args:
            emoji (Emoji): emoji

        Returns:
            EmojiName | None: The emoji name

        Example:
            >>> ZulipEmojiMapping.get_emoji_name("🐈")
            'cat'
        """
        emoji_code_parts = []
        for c in emoji:
            part = "{:X}".format(ord(c))
            # Ignore variation selector
            if part == "FE0F":
                continue
            emoji_code_parts.append(part)

        emoji_code_zulip = "-".join(emoji_code_parts)
        emoji_code_zulip = emoji_code_zulip.lower()
        if emoji_code_zulip not in EMOJI_NAME_MAPS:
            raise EmojiNotFound(f"No such emoji: {emoji_code_zulip}")

        return EMOJI_NAME_MAPS[emoji_code_zulip]["canonical_name"]

    @staticmethod
    def get_emoji_by_name(name: EmojiName) -> Emoji | None:
        """Get an emoji by it's Zulip canonical name or alias

        Args:
            name (Emoji): name or alias

        Returns:
            EmojiName | None: emoji if found

        Example:
            >>> ZulipEmojiMapping.get_emoji_by_name("family_man_girl_boy")
            👨‍👧‍👦
        """
        for code, data in EMOJI_NAME_MAPS.items():
            if name != data["canonical_name"] and name not in data["aliases"]:
                continue

            emoji = []
            for part in code.split("-"):
                emoji.append(chr(int(part, 16)))
            return "".join(emoji)

        raise EmojiNotFound(f"Couldn't find emoji: {name}")
