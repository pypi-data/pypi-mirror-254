# Zulip emoji mapping

Get emojis by Zulip names

## Example

```python
>>> from zulip_emoji_mapping import ZulipEmojiMapping
>>> print(ZulipEmojiMapping.get_emoji_name("🙂"))
smile
>>> print(ZulipEmojiMapping.get_emoji_by_name("smile"))
🙂
>>> print(ZulipEmojiMapping.get_emoji_by_name("cat"))
🐈
```
