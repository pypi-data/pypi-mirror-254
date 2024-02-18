"""
A very simple PubSub message bus for the Invent framework.

Based on original pre-COVID work by [Nicholas H.Tollervey.](https://ntoll.org/)

Copyright (c) 2024 Invent contributors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


__all__ = [
    "Message",
    "subscribe",
    "publish",
    "unsubscribe",
]


# Defines how channels / messages are linked to handler functions.
_pubsub = {}


class Message:
    """
    Represents any Invent related messages sent to channels.

    The message's type ("click", "slide", "whatever") becomes the
    thing to which to listen for (i.e. the "when" when subscribing).
    """

    def __init__(self, message_type, **kwargs):
        self._type = message_type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        result = self._type + " "
        result += str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )
        return result


def subscribe(handler, to_channel, when):
    """
    Subscribe an event handler to a channel[s] to handle when a certain type of
    message[s] is received.

    The to_channel and when arguments can be either individual strings or a
    list of strings to indicate the channel[s] and message types (when).

    E.g.

    subscribe(handler=my_handler, to_channel=["foo", "bar", ], when="click")
    """
    if isinstance(to_channel, str):
        to_channel = [
            to_channel,
        ]
    if isinstance(when, str):
        when = [
            when,
        ]
    for channel in to_channel:
        if channel not in _pubsub:
            _pubsub[channel] = {}
        for name in when:
            message_handlers = _pubsub[channel].get(name, set())
            message_handlers.add(handler)
            _pubsub[channel][name] = message_handlers


def publish(message, to_channel):
    """
    Publish a message to a certain channel[s].

    The to_channel can be either an individual string of the name of a channel
    or a list of strings of channel names to which to publish the message.

    E.g.

    publish(message=my_message, to_channel=["foo", "bar", ])
    """
    if isinstance(to_channel, str):
        to_channel = [
            to_channel,
        ]
    for channel in to_channel:
        channel_info = _pubsub.get(channel, {})
        if message._type in channel_info:
            for handler in channel_info[message._type]:
                handler(message)


def unsubscribe(handler, from_channel, when):
    """
    Unsubscribe a handler from a channel[s] to stop it handling when a certain
    message[s] is received.

    The from_channel and when arguments can be either individual strings or a
    list of strings to indicate the channel[s] and message types (when).

    E.g.

    unsubscribe(handler=a_handler, from_channel=["foo", "bar", ], when="click")
    """
    if isinstance(from_channel, str):
        from_channel = [
            from_channel,
        ]
    if isinstance(when, str):
        when = [
            when,
        ]
    for channel in from_channel:
        channel_info = _pubsub.get(channel)
        if channel_info:
            for name in when:
                if name in channel_info and handler in channel_info[name]:
                    channel_info[name].remove(handler)
                else:
                    raise ValueError(
                        f"Cannot unsubscribe from unknown message type: {name}"
                    )

        else:
            raise ValueError(
                f"Cannot unsubscribe from unknown channel: {channel}"
            )
